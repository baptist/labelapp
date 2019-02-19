from flask import Flask, render_template, g
from flask_socketio import SocketIO

from datetime import datetime

import config
import sqlite3


# Define the WSGI application object
app = Flask(__name__, instance_path=config.instance_path)

# Configurations
app.config.from_object('config')
app.config.from_envvar('FLASKR_SETTINGS', silent=True)


# Initiate socketio
socketio = SocketIO(app, async_mode="threading")


# Sample HTTP error handling
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

@app.template_filter('strftime')
def _jinja2_filter_datetime(date):
    return date.strftime("%d %b %Y %H:%M")


from app.info.controllers import mod_inf as module_info

app.register_blueprint(module_info)

