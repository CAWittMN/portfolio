# Flask app of a portfolio website that uses chatGPT-3 to answer questions about the portfolio owner
import os
import openai
from flask import Flask
from forms import ContactForm


app = Flask(__name__)

app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")
openai.api_key = os.environ.get("OPENAI_API_KEY")

@app.route("/")
def home():
    