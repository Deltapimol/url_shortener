import uuid
from flask import Flask, request, jsonify, make_response

app = Flask(__name__)


URL_MAPPINGS = dict()
API_URL_PREFIX = "/api/v1"


def random_string():
    """Random string generator"""
    return uuid.uuid4().hex[:6]

@app.route(f"{API_URL_PREFIX}/shorten-url", methods=['POST'])
def url_shortener():
    """URL Shortener View"""
    input_data =request.get_json()
    print(input_data['url'])
    original_url = input_data['url']
    if original_url in URL_MAPPINGS.keys():
        return make_response(jsonify({"shortened_url":URL_MAPPINGS.get(original_url)}), 200)
    else:
        shortened_url = random_string()
        URL_MAPPINGS[original_url] = shortened_url
        return make_response(jsonify({"shortened_url":shortened_url}), 200)
        
if __name__ == "__main__":
    app.run()