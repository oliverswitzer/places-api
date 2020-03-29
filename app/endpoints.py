from flask import (
    Blueprint, flash, redirect, render_template, request, url_for
)

bp = Blueprint('app', __name__)

@bp.route('/', methods=('GET', 'POST'))
def index():
    return "Hello, yo!"