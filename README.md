## URL Shortener README


**API Endpoint for URL shortening :** `/api/v1/shorten-url` <br/>

**Sample request body :** `{"url": "https://www.google.com"}` <br/>

**Sample response body :** `{"shortened_url": "https://www.example.com/d42f79"}`

**Sample cURL :** `curl --location --request POST 'localhost:5000/api/v1/shorten-url' \ --header 'Content-Type: application/json' \  --data-raw '{"url": "https://www.google.com"}'` <br/>




The code has URL validator to accept only valid URLs. The API will fetch a shortened URL if it exists for a certain URL or create a new one if it does not exist.
Memcached is used as caching solution and it has its own container.
The project has a docker-compose file having the API service and the memcached service. <br/>

API request screenshot from Postman : <br/>
![screenshot](https://github.com/Deltapimol/url_shortener_assignment/blob/master/screenshot/API_Request.png)

