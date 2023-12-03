from flask import Flask, render_template, request, session, url_for, redirect, make_response
from app import app, get_conn
import jwt
import string, random
#
app.secret_key = 'Q3I3Pm1lc3NpQ3I3Pm1lc3NpQ3I3Pm1lc3Np'

secret_key = 'cristianoronaldo'
# app.config['SESSION_COOKIE_HTTPONLY'] = True

# Index page

cursor = get_conn().cursor()
initial = True

curr_user = {}


def check_cookie():
    global curr_user
    try:

        cookie = request.cookies.get("session")
        decoded_token = jwt.decode(cookie, secret_key, algorithms=['HS256'])
        curr_user = decoded_token
        make_response(redirect(url_for('index')))

        query = f"SELECT * FROM users WHERE name = '{decoded_token['name']}'"
        cursor.execute(query)
        curr_user = cursor.fetchone()

    except jwt.ExpiredSignatureError:
        print("JWT token has expired.")
    except jwt.InvalidTokenError as e:
        print("Invalid JWT token:", e)


def JWT(name):
    payload = {
        'name': name
    }
    token = jwt.encode(payload, secret_key, algorithm='HS256')
    return token


def authenticate(username, password):
    global curr_user
    try:
        query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
        cursor.execute(query)

        curr_user = cursor.fetchone()
        if curr_user:
            return True
        else:
            return False
    except Exception:
        return False


@app.route('/')
def index():
    global initial
    check_cookie()
    name = curr_user['name'] if curr_user else ''
    res = make_response(render_template('index.html', name=name))
    if initial:
        res.set_cookie("session",
                       "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYW1lIjoiIn0.QgLEITyTJp_ult6CHUXxOGjc4vXgJtfwg5HRCDmzGSg")
        initial = False
    print(curr_user)
    return res


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        is_auth = authenticate(username, password)
        if is_auth:
            res = make_response(redirect(url_for('index')))
            res.set_cookie("session", JWT(curr_user['name']))
            return res
        else:
            message = "Sorry, this user is doesn't exist"
            return render_template('login.html', error=message)

    return render_template('login.html')


@app.route('/logout')
def logout():
    global curr_user
    res = make_response(redirect(url_for('index')))
    res.set_cookie("session",
                   "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYW1lIjoiIn0.QgLEITyTJp_ult6CHUXxOGjc4vXgJtfwg5HRCDmzGSg")
    check_cookie()
    return res


@app.route('/post_message', methods=['POST'])
def post_message():
    if curr_user:
        content = request.form['content']
        message = {'user': curr_user['name'], 'content': content}
        ##update DATABASE!!!!

        return render_template('index.html', messages=messages)
    else:
        return make_response(redirect(url_for('index')))


if __name__ == "__main__":
    app.run('0.0.0.0', 5800, debug=False)


