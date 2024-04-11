import os
from flask import Flask, request, make_response, send_file
from scraper import scrap_recipe

app = Flask(__name__)

RECIPE_FOLDER = "/recipes"

@app.route('/')
def hello_world():
    if "url" not in request.args:
        return make_response(f"MISSING URL", 400)
    url = request.args["url"]
    try:
        result = scrap_recipe(url)
        if result is None:
            make_response(f"Error parsing url", 500)
        else:
            make_response(f"${result}")
    except:
        make_response(f"Error parsing url", 500)


if __name__ == '__main__':
    app.run()
