# Create a virtual environment
# python3 -m venv .venv

# Activate the virtual environment
# .\.venv\bin\activate
# pip install flask

from flask import Flask, render_template 
import urllib.request, json # Import the library to make requests to the API

app = Flask(__name__) # Create the Flask app

@app.route("/") 
def get_list_characters_page():
    url = "http://rickandmortyapi.com/api/character/" 
    response = urllib.request.urlopen(url) 
    data = response.read() 
    dict = json.loads(data)

    # Render_template is a function that renders an HTML file
    # The first argument is the name of the file
    # The second argument is the data that will be passed to the HTML file
    return render_template("characters.html", characters=dict["results"]) 

@app.route("/profile/<id>") 
def get_profile(id):
    url = "http://rickandmortyapi.com/api/character/" + id
    response = urllib.request.urlopen(url) 
    data = response.read() 
    dict = json.loads(data)

    return render_template("profile.html", profile=dict) 

@app.route("/list") # Define the route 
def get_list_characters(): # Define the function that will be executed when the route is called
    url = "http://rickandmortyapi.com/api/character/" # URL of the API
    response = urllib.request.urlopen(url) # Make a request to the API
    characters = response.read() # Read the response
    dict = json.loads(characters) # Convert the response to a dictionary

    characters = []

    for character in dict["results"]: # Iterate over the results
        character = { # Create a dictionary with the data we want
            "name": character["name"],
            "status": character["status"],
        }
        characters.append(character) 

    return {"characters": characters} # Return the characters

# Templates is a folder that contains the HTML files