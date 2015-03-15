"""
views.py

URL route handlers

Note that any handler params must match the URL route params.
For example the *say_hello* handler, handling the URL route '/hello/<username>',
  must be passed *username* as the argument.

"""
from google.appengine.api import users
from google.appengine.runtime.apiproxy_errors import CapabilityDisabledError

from flask import render_template, flash, url_for

from flask_cache import Cache

from application import app
from decorators import login_required, admin_required
#from forms import ExampleForm
#from models import ExampleModel


# Flask-Cache (configured to use App Engine Memcache API)
cache = Cache(app)


def home():
    return render_template('home.html')


def contact():
    return render_template('contact.html')


def itservices():
    return render_template('itservices.html')


def disability():
    return render_template('disability.html')


def hooptedoodle():
    return render_template('hooptedoodle.html')


def specials():
    return render_template('specials.html')


def neohermes():
    return render_template('neohermes.html')


def dnamusic():
    return render_template('dnamusic.html')


def about():
    return render_template('about.html')


def presentative():
    return render_template('presentative.html')


def pyxcel():
    return render_template('pyxcel.html')


def timeandtravel():
    return render_template('timeandtravel.html')


def web_pages():
    return render_template('web_pages.html')


@admin_required
def admin_only():
    """This view requires an admin account"""
    return 'Super-seekrit admin page.'


@cache.cached(timeout=60)
def cached_examples():
    """This view should be cached for 60 sec"""
    examples = ExampleModel.query()
    return render_template('list_examples_cached.html', examples=examples)


def warmup():
    """App Engine warmup handler
    See http://code.google.com/appengine/docs/python/config/appconfig.html#Warming_Requests

    """
    return ''

