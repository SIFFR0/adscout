import os

from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/search')
def search():
    query = request.args.get('q', '')
    
    url = "https://www.facebook.com/ads/library/api/search/"
    params = {
        'search_terms': query,
        'ad_type': 'ALL',
        'ad_reached_countries[]': 'SE',
        'content_languages[]': 'sv',
        'limit': 10
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Accept': 'application/json',
        'Accept-Language': 'sv-SE,sv;q=0.9,en;q=0.8',
    }
    
    response = requests.get(url, params=params, headers=headers)
    
    # Return whatever we get back
    try:
        return jsonify(response.json())
    except:
        return jsonify({"raw": response.text[:2000], "status": response.status_code})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)), debug=False)