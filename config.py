import threading
import os
import sys

from os import environ



if not sys.platform[:3] == 'win':
    base = "/home/baptist/projects/"
else:
    base = "C://Users/Administrator/Desktop/projects/"

instance_path = base + 'recordapp/app/instance'
tmp_path = base + 'recordapp/app/static/tmp'
record_path = base + 'recordapp/app/static/recordings'
video_path = base + 'recordapp/app/static/labeled'
checked_path = base + 'recordapp/app/static/checked'


change_rate_motion_in, change_rate_motion_out = 0.1, 0.5  # necessary reaction (in seconds) to force status change
buffer_length = 2  # amount of seconds to hold in buffer when no motion is detected

"""
Helper class to enable communication between multiple threads.
"""


class Globals(object):
    dataLock = threading.Lock()
    record_thread = threading.Thread()
    stream_thread = threading.Thread()
    is_recording = False
    status_changed = False


# Statement for enabling the development environment
DEBUG = True

# Define the application directory
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

REDIS_HOST = "127.0.0.1"
REDIS_PORT = 6379
broker_url = environ.get('REDIS_URL', "redis://{host}:{port}/0".format(host=REDIS_HOST, port=str(REDIS_PORT)))

# Secret key for signing cookies
SECRET_KEY = "secret"

base_labels = ['drumming', 'no gesture', 'other gestures', 'shaking', 'swiping left', 'swiping right', 'thumb down',
              'thumb up', 'standing up', 'sitting down', 'bowing', 'clapping hands']

gesture_labels = ['drumming', 'shaking', 'swiping_left', 'swiping_right', 'thumb_down', 'thumb_up', 'other_gestures']# #os.listdir(vars['GFILES_LOCATION'])
events_labels = ['standing_up', 'sitting_down', 'going_out_of_room', 'entering_room', 'putting_on_cloth', 'putting_off_cloth', 'other_events']
labels = gesture_labels + events_labels
colors = ['#e6194b', '#3cb44b', '#ffe119', '#4363d8', '#f58231', '#911eb4', '#AAA', '#f032e6', '#bcf60c', '#fabebe', '#008080', '#e6beff', '#9a6324', '#aaaaaa']