# Consider using Spotipy, get track audio features!!
from authlib.integrations.requests_client import OAuth2Session
from keys import CLIENT_ID, CLIENT_SECRET
import pprint
import json
import urllib.request

def get_genres(resp):
    stuff = json.loads(resp)
    print(stuff)
    artistLst = stuff["items"]
    lst = []
    for artist in artistLst:
        genres = artist["genres"]
        if len(genres) > 0:
            for genre in genres:
                lst.append(genre)
    return lst

def book_keywords(genres):
    keywords = []
    for genre in genres:
        if "r&b" in genre:
            keywords.append("romance")
            keywords.append("love")
        elif "hyperpop" in genre:
            keywords.append("queer")
        elif "bedroom pop" in genre:
            keywords.append("coming+of+age")
        elif "pop" in genre:
            keywords.append("comedy")
            keywords.append("happy")
        elif "rage rap" in genre:
            keywords.append("dystopia")
        elif "hip hop" or "rap" in genre:
            keywords.append("action")
            keywords.append("poetry")
        elif "country" in genre:
            keywords.append("western")
            keywords.append("farm")
        elif "rock" or "punk" or "metal" in genre:
            keywords.append("rebellion")
            keywords.append("counterculture")
        elif "electronic" or "electro" or "techno" in genre:
            keywords.append("sci-fi")
            keywords.append("futurism")
        elif "jazz" or "house" or "funk" or "disco" in genre:
            keywords.append("retro")
            keywords.append("dance")
        elif "classical" or "piano" in genre:
            keywords.append("classical")
            keywords.append("history")
        elif "christian" in genre:
            keywords.append("jesus")
            keywords.append("christianity")
    unique_keywords = list(set(keywords))
    return unique_keywords

def get_cover(olid):
    if olid is None:
        return None
    return "https://covers.openlibrary.org/b/olid/" + olid + "-M.jpg"

def get_url(olid):
    if olid is None:
        return None
    return "https://openlibrary.org/olid/" + olid

def get_books(lst_keywords):
   books = {}
   index = 0
   for i in range(10):
       if index < len(lst_keywords):
           genre = lst_keywords[index]
       else:
           index = 0
           genre = lst_keywords[index]
       APIcall = "http://openlibrary.org/search.json?q=" + genre
       with urllib.request.urlopen(APIcall) as response:
           resp = response.read()
           resp_str = resp.decode("utf-8")
       data = json.loads(resp_str)
       works = data["docs"]
       result = works[i]
       title = result["title"]
       author = result["author_name"][0]
       cover = ""
       if len(result["cover_edition_key"]) != 0:
           cover = result["cover_edition_key"]
       else:
           cover = None
       if title not in books.keys():
           books[title] = {"author": author, "cover": cover}
       index += 1
   return books