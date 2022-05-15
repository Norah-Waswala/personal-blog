
from flask import render_template,request,redirect,url_for
from . import main
# from ..requests import get_movies,get_movie,search_movie

# from ..models import Review

@main.route('/')
def index():
    return render_template("index.html")