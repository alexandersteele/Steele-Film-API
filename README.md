# Description #

Author: Alexander Steele

This a project that implements a Flask web service that combines the JSON data from the CineList API and OMDB API. CineList provides data on nearby Cinemas (given a postcode), OMDB provides film data (given a title). Also provided is an AngularJS client to access the Flask Film API.


# Server Prerequisites #

The web service server requires multiple Flask prerequisites, to install these type this command in the "flask_web_server" directory:

pip install -r requirements.txt
pip install -r requirements.txt --user (if denied due to permissions)

You will also need to sign up to recieve an OMDB API key, once recieved you should open "views.py" in the "flask_web_server/app" directory and replace all instances of "YOUR_API_KEY" with your key.


# Running the API Service #

To run the python API service ensure you are using python3 and then type this command in the "flask_web_server" directory:

python run.py


# Running the Web Client #

The  web client has no prerequisites, to run it type this command in the "web_client" directory:

python -m http.server 8000

# Accessing the Client #

Navigate in a web browser to the address:

http://0.0.0.0:8000/

or

http://localhost:8000/
