"""Building an app factory and make routes and configurations"""

from decouple import config
from dotenv import load_dotenv
from flask import Flask, render_template, request
from .random_generator import RandomWiki

load_dotenv()

#Making the app factory
def create_app():
    app = Flask(__name__)

    app.config['ENV'] = config('ENV')

    @app.route('/')
    def homepage():
        return render_template('base.html', title='Homepage')

    @app.route('/randomize')
    def get_random(message=""):
        title= f"Paragraph from Wikipedia Article: {RandomWiki()[0]}"
        message = RandomWiki()[1]
        return render_template('randomize.html',title=title, message=message)

    return app