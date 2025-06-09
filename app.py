from flask import Flask
import functions
import keys
import os
app = Flask(__name__)
import json

from flask import Flask, redirect, session, url_for
from authlib.integrations.flask_client import OAuth

from keys import SECRET_KEY, CLIENT_ID, CLIENT_SECRET

app = Flask(__name__)
app.secret_key = SECRET_KEY

oauth = OAuth(app)
oauth.register(
    name="spotify",
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    authorize_url="https://accounts.spotify.com/authorize",
    access_token_url="https://accounts.spotify.com/api/token",
    api_base_url="https://api.spotify.com/v1/",
    client_kwargs={'scope': 'user-top-read'}
)

@app.route("/")
def index():
    try:
        token = session["spotify-token"]
    except KeyError:
        return redirect(url_for("login"))
    print(dir(oauth.spotify))
    data = oauth.spotify.get("/me/top/artists?time_range=long_term&limit=10", token=token).text
    return json.loads(data)

@app.route("/login")
def login():
    redirect_uri = url_for('authorize', _external=True)
    print(redirect_uri)
    return oauth.spotify.authorize_redirect(redirect_uri)


@app.route("/spotify-authorize")
def authorize():
    token = oauth.spotify.authorize_access_token()
    session["spotify-token"] = token
    return token

if __name__ == "__main__":
    app.run(debug=True)