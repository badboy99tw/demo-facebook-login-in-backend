import os

import requests
from flask import Flask, abort, request

app = Flask(__name__)

FACEBOOK_OAUTH_API = "https://www.facebook.com/v3.3/dialog/oauth"
FRONTEND_LOGIN_API = "http://localhost:5000/redirect/facebook"
BACKEND_LOGIN_API = "http://backend:5000/login/facebook"
CLIENT_SECRET = "CSRF Token"


@app.route("/")
def home():
    return (
        "<!DOCTYPE html>"
        "<html>"
        "<head>"
        "<title>Facebook Client Server Login Flow</title>"
        '<meta charset="UTF-8">'
        "</head>"
        "<body>"
        '<a href="{fb_api}?client_id={app_id}&redirect_uri={redirect_uri}&state={state}">LOGIN!</a>'
        "</body>"
        "</html>"
    ).format(
        fb_api=FACEBOOK_OAUTH_API,
        app_id=os.environ.get("FACEBOOK_APP_ID"),
        redirect_uri=FRONTEND_LOGIN_API,
        state=CLIENT_SECRET,
    )


@app.route("/redirect/facebook")
def login():
    if request.args.get("state") != CLIENT_SECRET:
        return abort(400)

    res = requests.post(
        BACKEND_LOGIN_API,
        data={"code": request.args["code"], "redirect_uri": FRONTEND_LOGIN_API},
    )
    return "Hi, %s" % res.json()["name"]
