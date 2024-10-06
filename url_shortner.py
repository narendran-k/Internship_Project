import random
import string
import sqlite3
from flask import Flask, request, jsonify, redirect

app = Flask(__name__)
DATABASE = 'url_shortener.db'

# Create a connection to the SQLite database
def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

# Initialize the database
def init_db():
    with get_db_connection() as conn:
        conn.execute('''
            CREATE TABLE IF NOT EXISTS urls (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                original_url TEXT NOT NULL,
                short_url TEXT NOT NULL UNIQUE
            )
        ''')
        conn.commit()

# Generate a random string of 6 characters
def generate_short_code():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=6))

# Route to shorten a URL
@app.route('/shorten', methods=['POST'])
def shorten_url():
    original_url = request.json.get('original_url')
    if not original_url:
        return jsonify({'error': 'Invalid URL'}), 400

    short_url = generate_short_code()
    
    with get_db_connection() as conn:
        conn.execute('INSERT INTO urls (original_url, short_url) VALUES (?, ?)', (original_url, short_url))
        conn.commit()

    return jsonify({'original_url': original_url, 'short_url': request.host_url + short_url})

# Route to redirect to the original URL
@app.route('/<short_url>', methods=['GET'])
def redirect_to_original(short_url):
    with get_db_connection() as conn:
        url = conn.execute('SELECT original_url FROM urls WHERE short_url = ?', (short_url,)).fetchone()
    
    if url is None:
        return jsonify({'error': 'URL not found'}), 404

    return redirect(url['original_url'])

# Main entry point
if __name__ == '__main__':
    init_db()
    app.run(port=5000, debug=True)
