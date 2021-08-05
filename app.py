import uuid
from flask import Flask, request, jsonify, make_response
from pymemcache.client import base

app = Flask(__name__)


API_URL_PREFIX = "/api/v1"
MEMCACHED_CLIENT = base.Client(('localhost', 11211))


def random_string():
    """Random string generator"""
    return uuid.uuid4().hex[:6]

@app.route(f"{API_URL_PREFIX}/shorten-url", methods=['POST'])
def url_shortener():
    """URL Shortener View"""
    input_data =request.get_json()
    original_url = input_data['url']
    if MEMCACHED_CLIENT.get(original_url) is None:
        shortened_url = random_string()
        MEMCACHED_CLIENT.set(original_url, shortened_url)
        return make_response(jsonify({"shortened_url":shortened_url}), 200)
    else:
        MEMCACHED_CLIENT.get(original_url)
        return make_response(jsonify({"shortened_url":MEMCACHED_CLIENT.get(original_url)}), 200)
    
        
if __name__ == "__main__":
    app.run()