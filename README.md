# django-url-shortener
a simple url shortener api built with django
## quick start:
setup a venv

    python -m venv env
    source env/bin/activate
    
install requirements:

    pip install -r req.txt

migrate 

    python manage.py migrate

start the app:

    python manage.py runserver

## example usage:
 shorten a url:
     
     curl -X POST http://127.0.0.1:8000/shorten/ -H "Content-Type: application/json" -d '{"original_url": "https://example.com/your-long-url"}'
 
 the respose would look like this:
    
    {"original_url":"https://example.com/your-long-url","short_code":"9pAnkC","created_at":"2024-11-01T10:14:47.200534Z"}
 list all shorten urls:
    
    curl -X GET http://127.0.0.1:8000/urls/

use a short url (ex: 9pAnkC):

    curl curl -X GET http://127.0.0.1:8000/9pAnkC/

this will redirect you to the original url.
    
