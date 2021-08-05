## URL Shortener README


**API Endpoint for URL shortening :** `/api/v1/shorten-url`
**Sample request body :** `{"url": "https://www.google.com"}`
**Sample cURL :** `curl --location --request POST 'localhost:5000/api/v1/shorten-url' \
--header 'Content-Type: application/json' \ 
--data-raw '{"url": "https://www.google.com"}'`
**Sample response body :** `{"shortened_url": "3c6c02"}`


Memcached is used as caching solution and it has its own container.
The project has a docker-compose file having the API service and the memcached service.
API Output screenshot: