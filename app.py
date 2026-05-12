import os
from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

META_TOKEN = "EAANlrkUIHyMBRaHZBbRndcZAk75A6iZAQ10uBVA4jYmgrYmtU6SCagO8JWYYbrpuksrxNWgeYprwXS2rnUZBZC7PHnmxfVnG5Ci4qaThbV0adbDh6RfUegL5EisrgQamQar5Dd05g4iWCxWeVhZC3rg8GQiUKqJ21DTlZBZB4lExMIN4Hrz3I0kNZCXAZBEUEpc5rcCSd6GDsxZAEFfxHBcyZBynYUwCBlVwdzbHYXLPWLSp4kjXHAYVO24UkAZDZD"

@app.route('/')
def index():
    return send_from_directory(os.path.dirname(os.path.abspath(__file__)), 'index.html')

@app.route('/search')
def search():
    query = request.args.get('q', '')
    url = "https://graph.facebook.com/v19.0/ads_archive"
    params = {
        'access_token': META_TOKEN,
        'search_terms': query,
        'ad_type': 'ALL',
        'ad_reached_countries': ['SE'],
        'fields': 'ad_creative_body,ad_snapshot_url,page_name',
        'limit': 10
    }
    response = requests.get(url, params=params)
    data = response.json()

    if 'error' in data:
        return jsonify({"data": [], "demo": True})

    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)), debug=False)