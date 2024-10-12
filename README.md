# URL Shortening Service

## Overview
This is a RESTful API that allows users to shorten long URLs. The API provides endpoints to create, retrieve, update, and delete short URLs. It also provides statistics on the number of times a short URL has been accessed.

## Endpoints
* `POST /shorten`: This endpoint is used to create a short URL. It takes a long URL as input and returns a short URL.
* `GET /shorten/{shortUrl}`: This endpoint is used to retrieve the original long URL from a short URL.
* `PUT /shorten/{shortUrl}`: This endpoint is used to update a short URL. It takes a new long URL as input and updates the short URL.
* `DELETE /shorten/{shortUrl}`: This endpoint is used to delete a short URL.
* `GET /shorten/{shortUrl}/stats`: This endpoint is used to retrieve statistics on the number of times a short URL has been accessed.

## Usage
To use this service, you can send HTTP requests to the provided endpoints. Here are some examples:

* To create a short URL, send a POST request to `/shorten` with the long URL in the request body.
* To retrieve the original long URL from a short URL, send a GET request to `/shorten/{shortUrl}`.
* To update a short URL, send a PUT request to `/shorten/{shortUrl}` with the new long URL in the request body.
* To delete a short URL, send a DELETE request to `/shorten/{shortUrl}`.
* To retrieve statistics on the number of times a short URL has been accessed, send a GET request to `/shorten/{shortUrl}/stats`.

## Technologies
This service is built using Python and the Flask framework. It uses a SQLite database to store the short URLs and their statistics.

## Getting Started
To use this service, follow these steps:
1. Clone the project repository to your local machine.
2. Install the project dependencies by running `pip install -r requirements.txt`.
3. Start the service by running `python app.py`.
4. Send HTTP requests to the provided endpoints to create, retrieve, update, and delete short URLs, and to retrieve statistics on the number of times a short URL has been accessed.

## Directory Structure
The project directory structure is organized as follows:
* `app.py`: The Flask application file that handles HTTP requests and responses.
* `utils.py`: A utility file that contains helper functions for the service.
* `requirements.txt`: A file listing the project's dependencies.
* `README.md`: This file, which provides an overview of the project.

## Source
This project is inspired by the roadmap.sh project on [URL Shortening Service](https://roadmap.sh/projects/url-shortening-service).
