import os

import requests
from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/login/facebook", methods=["POST"])
def login():
    # get access token from code
    code = request.form["code"]
    redirect_uri = request.form["redirect_uri"]
    res = requests.get(
        "https://graph.facebook.com/v3.3/oauth/access_token",
        params={
            "client_id": os.environ.get("FACEBOOK_APP_ID"),
            "redirect_uri": redirect_uri,
            "client_secret": os.environ.get("FACEBOOK_APP_SECRET"),
            "code": code,
        },
    )
    access_token = res.json().get("access_token")

    # get user data
    res = requests.get(
        "https://graph.facebook.com/me",
        params={"fields": "id,name", "access_token": access_token},
    )
    return jsonify(**res.json())
