# timestamp

This repository hosts the software for a cryptographic timestamp program. The program consists of a webserver, which signs messages and hashes sent to it with the time.

It also has an api for the client side so users can easily use the webserver without having to know the underlying details.

Dependencies:
pyca/cryptography: https://github.com/pyca/cryptography

Django web framework: https://www.djangoproject.com/

Python requests module: http://docs.python-requests.org/en/master/

How to run Webserver:

1. Install django for python https://www.djangoproject.com/
2. cd to the Webserver/myapp folder
3. Run with python3 manage.py runserver

How to run Client demo

1. cd to ClientAPI/ folder
2. run with python3 timestampAppDemo.py


API Documentation:

timestamp.signTime(message, url):

- Returns the signature of the message/hash in string form by querying server with url in string form

timestamp.verifyTime(message, signature, date):

- Returns a boolean of whether the verification process succeeded or failed
- Takes arguments of the message/hash that you are verifying, the signature (in string form as returned from server) and the date in the form YYYY-MM-DD
