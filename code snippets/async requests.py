import requests
import grequests

urls = [
    'http://www.heroku.com',
    'http://tablib.org',
    'http://httpbin.org',
    'http://python-requests.org',
    'http://www.heroku.com',
    'http://tablib.org',
    'http://httpbin.org',
    'http://python-requests.org',
    'http://www.heroku.com',
    'http://tablib.org',
    'http://httpbin.org',
    'http://python-requests.org',
    'http://kennethreitz.com'
]


#
rs = (grequests.get(u) for u in urls)
print grequests.map(rs)

#
rs = (requests.get(u, return_response=False) for u in urls)
print grequests.map(rs)

#
print map(lambda u: requests.get(u), urls)
