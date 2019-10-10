# app.py
from flask import Flask,render_template  # import flask
import requests
import json

app = Flask(__name__)  # create an app instance


@app.route("/")  # at the end point /
def hello():  # call method hello
    response = requests.get('http://www.omdbapi.com/?apikey=92582e55&i=tt0120338')
    movie = json.loads(response.text)
    print(movie)
    return render_template('page.html', content=movie)


if __name__ == "__main__":  # on running python app.py
    app.run()  # run the flask app
