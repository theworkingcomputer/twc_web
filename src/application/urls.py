"""
urls.py

URL dispatch route mappings and error handlers

"""
from flask import render_template

from application import app
from application import views


## URL dispatch rules
# App Engine warm up handler
# See http://code.google.com/appengine/docs/python/config/appconfig.html
app.add_url_rule('/_ah/warmup', 'warmup', view_func=views.warmup)

# Home page
app.add_url_rule('/', 'home', view_func=views.home)
app.add_url_rule('/home', 'home', view_func=views.home)


# Contact page
app.add_url_rule('/contact', 'contact', view_func=views.contact)


# IT Services page
app.add_url_rule('/itservices', 'itservices', view_func=views.itservices)


# Disability Services page
app.add_url_rule('/disability', 'disability', view_func=views.disability)


# Hooptedoodle animation page
app.add_url_rule('/hooptedoodle', 'hooptedoodle', view_func=views.hooptedoodle)


# Special Projects and Products page
app.add_url_rule('/specials', 'specials', view_func=views.specials)


# Presentative group-blog teaser page
app.add_url_rule('/presentative', 'presentative', view_func=views.presentative)


# Neohermes Desktop teaser page
app.add_url_rule('/neohermes', 'neohermes', view_func=views.neohermes)


# Time and Travel tracker page
app.add_url_rule('/timeandtravel', 'timeandtravel', view_func=views.timeandtravel)


# DNA Music page
app.add_url_rule('/dnamusic', 'dnamusic', view_func=views.dnamusic)


# Python to Excel spreadsheet writer
app.add_url_rule('/pyxcel', 'pyxcel', view_func=views.pyxcel)


# 'About' page for the Working Computer
app.add_url_rule('/about', 'about', view_func=views.about)


# Web pages and services page
app.add_url_rule('/web_pages', 'web_pages', view_func=views.web_pages)


# Contrived admin-only view example
app.add_url_rule('/admin_only', 'admin_only', view_func=views.admin_only)


## Error handlers
# Handle 404 errors
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


# Handle 500 errors
@app.errorhandler(500)
def server_error(e):
    return render_template('500.html'), 500
