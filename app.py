# Import Flask Library
import string, random
from flask import Flask, render_template, request, session, url_for, redirect, make_response
import pymysql.cursors

app = Flask(__name__)

# Configure MySQL
def get_conn():
    # return pymysql.connect(
    #    host="localhost",
    #    port=8889,
    #    user='root',
    #    password='root',
    #    db='pentesting',
    #    charset='utf8mb4',
    #    cursorclass=pymysql.cursors.DictCursor)

    return pymysql.connect(host="localhost",
                       port=8889,
                       user='root',
                       password='root',
                       db='pentesting',
                       charset='utf8mb4',
                       cursorclass=pymysql.cursors.DictCursor)


