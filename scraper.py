#!/usr/bin/python
import time
import requests
from pprint import pprint
from BeautifulSoup import BeautifulSoup

# example scrape function
def google_this(search_string):
    params = {'q': search_string}
    response = requests.get("https://www.google.ca/search", params = params)
    soup = BeautifulSoup(response.text)
    results = soup.findAll("h3")

    google_results = []
    for result in results:
        for a in result.findAll("a"):
            href = a.get('href')
            text = a.text
            google_results.append((href, text))
    return google_results

class ECWeather:

    def __init__(self, url=None):
	self.sleep_seconds = 1 
	self.url = url if url else "http://climate.weather.gc.ca/advanceSearch/searchHistoricDataStations_e.html"\
		"?searchType=stnProv&timeframe=1&lstProvince=&optLimit=yearRange&StartYear=1840"\
		"&EndYear=2014&Year=2014&Month=9&Day=16&selRowPerPage=100&cmdProvSubmit=Search"

    def sleep():
	time.sleep(self.sleep_seconds)

    def run():
	"""
	this function is where the code starts, it walks through all the link params found on the initial search page, and gets the data for each one.

	"""
	data = []
	for link_params in self.get_all_link_params():
		pages_of_data = self.get_pages_of_data(link_params)
		data.append(data)
	return data

    def get_all_link_params():
	"""
	this function parses the search page, and builds a list of dictionaries, each dictionary representing a row, i.e.
		row = {
		  'station': "(AE) BOW SUMMIT",
		  'province': "AB",
		  'data_intervals': ['daily', 'monthly'],
		  'years': [1999, 2000, 2001],
		  'months': [1, 2, 3, 4],
		  'days': []
		}
	"""
        response = requests.get(self.url)
        soup = BeautifulSoup(response.text)
    	# I would find all div's with classes 'divTableRowEven' and 'divTableRowOdd'
	# and then pass each of those into another function to take them appart, and 
	rows = []  # TODO: populate rows
	all_params = []
	for row_element in rows:
	    all_params.append(self.get_link_params(row_element))

	# note this function only does one page, todo later, have it collect all pages of search results.
	return all_params


    def get_link_params(element):
	"""
	this function takes a soup element, and returns a dictionary like this:
		{
		  'station': "(AE) BOW SUMMIT",
		  'province': "AB",
		  'data_intervals': ['daily', 'monthly'],
		  'years': [1999, 2000, 2001],
		  'months': [1, 2, 3, 4],
		  'days': []
		}
	"""
	row_data = {}
	# TODO: fill in row_data
	return row_data

    def get_pages_of_data(link_params):
	"""
	this function will take all desired permutations and combinations of the link_params, and call get_page_of_data.
	then it will 
	"""

    def get_page_of_data(timeframe, province, station_id, daily_range, year, month, day):
	params = {
	  'timeframe': timeframe,  #2,
	  'Prov': province,  #"AB",
	  'StationID': station_id,  #10700
	  'dlyRange': daily_range,  #"1998-02-01|2007-11-30",
	  'Year': year,
	  'Month': month,
	  'Day': day
	}
	base_url = "http://climate.weather.gc.ca/climateData/dailydata_e.html"
	response = requests.get(base_url, params=params)
	if response.status_code == 200:
	    return response.text


ECWeather()
data = ecWeather.run()
for row in data:
    print row

