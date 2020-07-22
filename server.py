import os
from bottle import route, run, static_file, request, template
from logic import cesar_code, cesar_decode, bruteforce


@route('/')
def send_index():
    return template('index', result=None)


@route('/style.css')
def send_css():
    return static_file('style.css', root='.')


@route('/icon.ico')
def send_icon():
    return static_file('icon.ico', root='.')


@route('/ShareTechMono-Regular.ttf')
def send_font():
    return static_file('ShareTechMono-Regular.ttf', root='.')


@route('/', method='POST')
def encryption():
    if request.forms.get('mode') == 'CODE':
        result = cesar_code(request.forms.get('text'), int(request.forms.get('key')))
    elif request.forms.get('mode') == 'DECODE':
        result = cesar_decode(request.forms.get('text'), int(request.forms.get('key')))
    else:
        result = None
    return template('index', result1=result)


@route('/bruteforce')
def send_crack_form():
    return template('bruteforce', options=None)


@route('/bruteforce', method='POST')
def crack_message():
    options = bruteforce(request.forms.get('message'))

    return template('bruteforce', options=options)


if os.environ.get('APP_LOCATION') == 'heroku':
    run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
else:
    run(host='localhost', port=8080)
