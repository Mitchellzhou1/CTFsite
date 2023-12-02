from flask import Flask, render_template, request, session, url_for, redirect, make_response
import pymysql.cursors
from app import app, get_conn
import string, random
import login
#
app.secret_key = 'Q3I3Pm1lc3NpQ3I3Pm1lc3NpQ3I3Pm1lc3Np'
# app.config['SESSION_COOKIE_HTTPONLY'] = True

# Index page


valid_credentials = {
    "username": "user",
    "password": "password"
}
@app.route('/')
def index():
    print(session)
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')

    # Check if the provided credentials match the valid credentials
    if username == valid_credentials['username'] and password == valid_credentials['password']:
        # Successful login, you can redirect the user to a different page
        return redirect(url_for('index'))
    else:
        # Failed login, you can render the login page with an error message
        return render_template('login.html', error="Invalid credentials")




if __name__ == "__main__":
    app.run('0.0.0.0', 5800, debug=False)


