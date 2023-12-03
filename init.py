from flask import Flask, render_template, request, session, url_for, redirect, make_response, jsonify
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

curr_user = {"name": "Guest"}

def check_cookie():
    global curr_user
    try:

        cookie = request.cookies.get("session")
        decoded_token = jwt.decode(cookie, secret_key, algorithms=['HS256'])
        print("decoded cookie" , decoded_token)
        curr_user = decoded_token
        make_response(redirect(url_for('index')))

        if curr_user['name'] != 'Guest':
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
def index(name=''):
    global initial
    name = curr_user['name'] if curr_user['name'] != 'Guest' else ''
    res = make_response(render_template('index.html', name=name))
    if initial:
        res.set_cookie("session",
                       "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYW1lIjoiR3Vlc3QifQ.zK7zYBE9t7NHZROgouNsDFxqf2uCzVlEeLpf08L3K5Y")
        initial = False
    print("curr_user:", curr_user)
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

    get_chat()
    return render_template('login.html')


@app.route('/logout')
def logout():
    global curr_user
    res = make_response(redirect(url_for('index')))
    res.set_cookie("session",
                   "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYW1lIjoiR3Vlc3QifQ.zK7zYBE9t7NHZROgouNsDFxqf2uCzVlEeLpf08L3K5Y")
    check_cookie()
    return res


@app.route('/submit_chat', methods=['POST'])
def submit_chat():
    global cursor
    message = request.form.get('message')
    name = curr_user['name']

    # Insert the message into the database (this is a simple illustration; use proper prepared statements in production)
    query = "INSERT INTO chatlog (name, message) VALUES (%s, %s);"
    cursor.execute(query, (name, message))
    print("query worked")
    get_conn().commit()
    print("query commited")
    get_chat()

    # Return a response indicating success
    return jsonify({'status': 'Message received'})

@app.route('/get_chat')
def get_chat():
    global cursor
    # Retrieve all chat messages from the database
    query = "SELECT * FROM chatlog"
    cursor.execute(query)
    chats = cursor.fetchall()
    print("Chat logs")
    for i in chats:
        print(i)

    return jsonify(chats)




if __name__ == "__main__":
    app.run('127.0.0.1', 5800, debug=False)


