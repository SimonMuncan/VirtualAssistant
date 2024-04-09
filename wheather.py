import requests, geocoder

class Weather():
    #Method to get current weather information
    def checkCurrentWeather():
        # API endpoint for current weather
        url = "https://ai-weather-by-meteosource.p.rapidapi.com/current"
        # Get user's location based on IP address
        g = geocoder.ip('me')
        lat = g.lat
        lon = g.lng
        # Query parameters
        querystring = {"lat":lat,"lon":lon,"timezone":"auto","language":"en","units":"auto"}
        # Headers for API request
        headers = {
	        "X-RapidAPI-Key": "613fa57601msh56fa4a7e7a50b5cp1d7c22jsn333fa9d8aa13",
	        "X-RapidAPI-Host": "ai-weather-by-meteosource.p.rapidapi.com"
        }
        # Send request to the API
        response = requests.get(url, headers=headers, params=querystring).json()
        # Extract and return the current weather summary
        return response['current']['summary']