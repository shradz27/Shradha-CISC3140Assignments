# app.py
from flask import Flask  # import flask
import requests
import json

app = Flask(__name__)  # create an app instance


@app.route("/")  # at the end point /
def hello():  # call method hello
    response = requests.get('http://www.omdbapi.com/?apikey=92582e55&i=tt0120338')
    movie = json.loads(response.text)
    print(movie)
    return '''
    <html>
        <head>
            <title>Home Page - Microblog</title>
        </head>
        <body>
            
            <h1>''' + movie['Title'] + '''</h1>
            <h4>Release Date : ''' + movie['Released'] + '''</h4>
            <h4>Runtime : ''' + movie['Runtime'] + '''</h4>
            <h4>Genre : ''' + movie['Genre'] + '''</h4>
            <h4>Awards : ''' + movie['Awards'] + '''</h4>
            <img src="''' + movie['Poster'] + '''"/>
            <p>''' + movie['Plot'] + '''</p>
        </body>
    </html>'''
    return "Hello World!"  # which returns "hello world"


if __name__ == "__main__":  # on running python app.py
    app.run()  # run the flask app
