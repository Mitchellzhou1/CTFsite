from flask import Flask, render_template, request, session, url_for, redirect, make_response
import pymysql.cursors
from app import app, get_conn
import string, random
import login

app.secret_key = 'Q3I3Pm1lc3NpQ3I3Pm1lc3NpQ3I3Pm1lc3Np'
app.config['SESSION_COOKIE_HTTPONLY'] = True

# Index page
@app.route('/')
def index():
    print(session)
    return make_response(render_template('index.html'))


if __name__ == "__main__":
    app.run('0.0.0.0', 5800, debug=False)


