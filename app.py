import os
from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

META_TOKEN = "EAANlrkUIHyMBRapFSlw7yPzawNGUICpMN7bzruKoZBVex5eD63HdeleiCTZBQbSMTNmQMuUuS8qZCN7JoLenQkHvFcHkDJFdHkWbmxXaWdRJELuiDWlzydBF1805KZBH9LKZCB7rGVHz6mm1YYxBOFCB8XpfAYZBVTGMSF42ATbM05CTmVfDVUYRO90SgsjzNjxCixNmR9F4buIOB6G0JMrPeMtDGZAOtLFQaIJpYKZAQCOT4GeJggxAPZCZCNf9pj2UjxT4ZBz8xT5neDgpbjAqL6bU5A1LhzZAxBG1sdkSt9YZD"

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
    return jsonify(response.json())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)), debug=False)