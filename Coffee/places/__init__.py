from flask import Blueprint

places = Blueprint('places', __name__, template_folder='templates')

from coffee.places.views import *
