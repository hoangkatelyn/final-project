# Consider using Spotipy, get track audio features!!
from authlib.integrations.requests_client import OAuth2Session
from keys import CLIENT_ID, CLIENT_SECRET
import pprint
import json

# get user's top 10 artists from Spotify (long-term) then provide book recommendations. decided this way because a lot of
# the stuff on the web api is now deprecated

# should we be calling any of these functions in another function like hw6?

def get_genres(resp):
    stuff = resp.json()
    artistLst = stuff["items"]
    lst = []
    for artist in artistLst:
        genres = artist["genres"]
        if len(genres) > 0:
            for genre in genres:
                lst.append(genre)
    return lst

# analyze_genres(genres)
# takes a list of genres
# uses if, else, elif to match genres to keywords to search Open Library Subject API
# returns a new list of keywords

# get_books_data
# consider splitting this up into different methods mayhaps

# first, use the list of keywords to look through Subject API
# the Subject API returns titles, author, and related subjects associated with the chosen subject
# get list of book titles
#
# after, use list of book titles to call for information about books using Search API ex:https://openlibrary.org/search.json?title=the+lord+of+the+rings
# return list/map of book information (title, author, cover_edition_key)
# cover_edition_key is also known as OLID to get covers using cover API
#
# next, get the cover by using the list/map of book information obtained previously.
# use cover_edition_key and return a call like this https://covers.openlibrary.org/b/olid/OL7440033M-S.jpg
# 1st part is they type of identifier
# next is the OLID
# final is the size of the image -S, -M, -L
# more info on https://openlibrary.org/developers/api
