from flask import flash, json
import requests
import json
from app import app


# Root OMDB API Endpoint
@app.route('/', methods=['GET'])
def getTasks():
	r = requests.get("http://www.omdbapi.com/?t=toy+story&apikey=" + "YOUR_API_KEY", verify=False).text # Default OMDB request
	return r # Returns request JSON as text


# CineList API Endpoint
@app.route('/<postcode>', methods=['GET'])
def getCinemas(postcode):

	r = requests.get("https://api.cinelist.co.uk/search/cinemas/postcode/" + postcode, verify=False).text # API request with only CineList postcode
	return r # Returns request JSON as text


# CineList and OMDB API Endpoint
@app.route('/<postcode>/<film>', methods=['GET'])
def getFilm(postcode, film):

	filmData = requests.get("http://www.omdbapi.com/?t=" + film + "&apikey="+ "YOUR_API_KEY", verify=False).text # OMDB API request
	cinemaData = requests.get("https://api.cinelist.co.uk/search/cinemas/postcode/" + postcode, verify=False).text # CineList API request

	a = json.loads(filmData) # Converts OMDB data to JSON
	b = json.loads(cinemaData) # Converts CineList data to JSON
	data = { 'film' : a, 'cinema' : b } # Merges OMDB data with CineList data with given keys

	return json.dumps(data) # Converts JSON to text and returns
