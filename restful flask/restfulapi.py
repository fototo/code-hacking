#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Tutorial de http://publish.luisrei.com/articles/flaskrest.html

from flask import Flask, url_for, request, json, Response, jsonify

app = Flask(__name__)


@app.route('/')
def api_root():
    return 'Welcome stranger!\n'

@app.errorhandler(404)
def not_found(error=None):
    message = {
        'status': 404,
        'message': 'mauro: Not Found ' + request.url
    }

    resp = jsonify(message)
    resp.status_code = 404

    return resp


@app.route('/articles')
def api_articles():
    return 'List of ' + url_for('api_articles') + '\n'


# @app.route('/articles/<int:articleid>')
# @app.route('/articles/<float:articleid>')
# @app.route('/articles/<path:articleid>')
# default is string
@app.route('/articles/<articleid>')
def api_article(articleid):
    return 'You are reading ' + articleid + '\n'


@app.route('/hello')
def api_hello():
    if 'name' in request.args:
        return 'Hello ' + request.args['name']
    else:
        return 'hello stranger!'


@app.route('/echo', methods = ['GET', 'POST', 'PATCH', 'PUT', 'DELETE'])
def api_echo():
    return 'echo: ' + request.method + '\n'


@app.route('/messages', methods = ['POST'])
def api_message():
    if request.headers['Content-Type'] == 'text/plain':
        return 'Text message: ' + request.data

    elif request.headers['Content-Type'] == 'application/json':
        return 'Json message: ' + json.dumps(request.json)

    else:
        return '415 Unsupported Media Type'


@app.route('/response')
def api_response():
    response = Response('my response is awesome',
                        status=200,
                        mimetype='application/json')
    # a linha anterior pode ser substituida pelas seguintes:
    # response = jsonify(data)
    # response.status_code = 200
    response.headers['Mauro'] = 'Santos'
    return response


@app.route('/users/<int:userid>', methods = ['GET'])
def api_user(userid):
    users = {1: 'john', 2: 'steve', 3: 'bill'}

    if userid in users.keys():
        return jsonify({userid: users[userid]})
    else:
        return not_found()


@app.route('/headers')
def api_headers():
    response = ''
    for v, value in request.headers:
        response += '<b>%s:<br></b>%s<p>\n' % (v, value)
    return response


# LOGIN
from functools import wraps


def checkAuth(username, password):
    return username == 'admin' and password == 'root'

def authenticate():
    message = {'Message': 'Authenticate.'}
    resp = jsonify(message)

    resp.status_code = 401
    resp.headers['WWW-Authenticate'] = 'Basic realm="Example"'

    return resp

def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth:
            return authenticate()

        elif not checkAuth(auth.username, auth.password):
            return authenticate()

        return f(*args, **kwargs)
    return decorated


@app.route('/secrets')
@requires_auth
def api_hello():
    return 'Shhh this is top secret spy stuff'


@app.route('/auth')
def api_auth():
    return authenticate()


# LOGGING
import logging

file_handler = logging.FileHandler('app.log')
app.logger.addHandler(file_handler)
app.logger.setLevel(logging.INFO)

@app.route('/hello', methods = ['GET'])
def api_hello():
    app.logger.info('informing')
    app.logger.warning('warning')
    app.logger.error('screaming bloody murder!')

    return "check your logs\n"

if __name__ == '__main__':
    app.debug = True
    app.run()
