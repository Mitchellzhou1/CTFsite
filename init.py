from flask import Flask, render_template, request, session, url_for, redirect, make_response
from app import app, get_conn
import string, random
#
app.secret_key = 'Q3I3Pm1lc3NpQ3I3Pm1lc3NpQ3I3Pm1lc3Np'
# app.config['SESSION_COOKIE_HTTPONLY'] = True

# Index page

cursor = get_conn().cursor()

valid_credentials = {
    "username": "user",
    "password": "password"
}

def authenticate(username, password):
    query = "SELECT * FROM users WHERE username = %s AND password = %s"
    cursor.execute(query, (username, password))

    user = cursor.fetchone()

    if not user:
        return False
    else:
        name = user['name']
        session['email'] = user['email']
        return True


@app.route('/')
def index():
    res = make_response(render_template('index.html'))
    res.set_cookie("session", "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjoiR3Vlc3QifQ.Yj7FTx2j2yC18jB01ovovVdr4yfcDcc0spVhsdkcCNk")

    return res

@app.route('/login', methods=['GET', 'POST'])  # Allow both GET and POST methods
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if authenticate(username, password):
            message = "Sorry, this user is doesn't exist"
            return render_template('login.html', error=message)
        else:
            return render_template('index.html')

    # This part handles the GET request when accessing the login page
    return render_template('login.html')




if __name__ == "__main__":
    app.run('0.0.0.0', 5800, debug=False)


