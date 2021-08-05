import uuid
from flask import Flask, request, jsonify, make_response
from pymemcache.client import base
import validators

app = Flask(__name__)


API_URL_PREFIX = "/api/v1"
MEMCACHED_CLIENT = base.Client(('memcached_container', 11211))
SAMPLE_WEBSITE = "https://www.example.com/"

def random_string():
    """Random string generator"""
    return uuid.uuid4().hex[:6]

@app.route(f"{API_URL_PREFIX}/shorten-url", methods=['POST'])
def url_shortener():
    """URL Shortener View"""
    input_data =request.get_json()
    original_url = input_data['url']
    try:
        if validators.url(original_url) == True:
            if MEMCACHED_CLIENT.get(original_url) is None:
                shortened_url = SAMPLE_WEBSITE + random_string()
                MEMCACHED_CLIENT.set(original_url, shortened_url)
                return make_response(jsonify({"shortened_url":shortened_url}), 200)
            else:
                shortened_url = MEMCACHED_CLIENT.get(original_url)
                return make_response(jsonify({"shortened_url":shortened_url.decode("utf-8")}), 200)
        else:
            return make_response(jsonify({"ERROR":"Invalid URL"}), 400)
    except Exception as e:
        return make_response(jsonify({"ERROR":e}), 500)
        
if __name__ == "__main__":
    app.run(host='0.0.0.0')