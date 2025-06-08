import requests

def get_movie_details(movie_name, api_key):
    url= f"http://www.omdbapi.com/?t={movie_name}&apikey={ 9265f3a}"
    response = requests.get(url)
    if response.get("Response") == "True":
        result = response.get("Plot", "N/A"), response.get("Poster", "N/A")
        plot = result[0]
        poster = result[1]
        return plot, poster

    return "N/A", "N/A"
