# Consider using Spotipy, get track audio features!!
from authlib.integrations.requests_client import OAuth2Session
from keys import CLIENT_ID, CLIENT_SECRET
import pprint

scope = "user-top-read"

client = OAuth2Session(CLIENT_ID, CLIENT_SECRET, scope=scope, redirect_uri="https://katelynhoang.pythonanywhere.com/")
authorization_endpoint = "https://accounts.spotify.com/authorize"
uri, state = client.create_authorization_url(authorization_endpoint)
print("Please go to this URL and follow the prompts: {}".format(uri))

authorization_response = input("Once you are redirected by your browser, copy the URL from your browser's address bar and enter it here: ")

token_endpoint = "https://accounts.spotify.com/api/token"
token = client.fetch_token(token_endpoint, authorization_response=authorization_response)
api_endpoint = "https://api.spotify.com/v1"
resp = client.get(api_endpoint + "/me/top/artists?time_range=long_term&limit=5")
pprint.pprint(resp.text)



