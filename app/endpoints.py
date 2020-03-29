from flask import (
    Blueprint, flash, redirect, render_template, request, url_for
)
from flask_httpauth import HTTPTokenAuth
import os
import populartimes
import json

auth = HTTPTokenAuth(scheme='Token')
bp = Blueprint('app', __name__)

@auth.verify_token
def verify_token(token):
    api_token = os.environ.get('HTTP_AUTH_TOKEN')

    if token == api_token:
        return True
    return False

@bp.route('/places/<string:place_id>', methods=('GET', 'POST'))
@auth.login_required
def index(place_id):
    api_token = os.environ.get('GOOGLE_MAPS_API_TOKEN')
    response = populartimes.get_id(api_token, place_id)

    return json.dumps(response)