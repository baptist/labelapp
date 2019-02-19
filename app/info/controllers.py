from flask import render_template, Blueprint, request

from app import socketio
from config import *
from datetime import datetime

import shutil
import csv
import h5py
import glob
import numpy as np

mod_inf = Blueprint('info', __name__)

@mod_inf.route('/label/', defaults={'target': 'baptist', 'filename': '081120181729_session_01_baptist_gestures_room_01_radar1'}, methods=['GET'])
@mod_inf.route('/label/<target>/<filename>', methods=['GET'])
def label(target, filename):

    annotations = []
    previous_index = 0
    previous_label = len(labels) - 1
    # with open(os.path.join(record_path, target, filename + '.csv'), 'r') as annotation_file:
    with open(os.path.join(base + 'recordapp/app/static/recordings', target, filename + '.csv'), 'r') as annotation_file:
        for info in annotation_file.readlines():
            index, label = info.split(',')
            index, label = int(index), labels.index(label.strip()) if not label.strip() == 'end' else -1

            while previous_index < index:
                annotations.append(previous_label)
                previous_index += 1

            if not label == -1:
                annotations.append(label)

            previous_label = label
            previous_index += 1

    # Return empty header
    return render_template("label.html", async_mode=socketio.async_mode, target=target, filename=filename, annotations=annotations, labels=labels, colors=colors, num_pixels=4, num_frames_in_timeline=300, active_label='other_events')


@mod_inf.route('/annotate2', methods=['POST'])
def annotate():
    target = request.form['target']
    filename = request.form['filename']
    index = int(request.form['index'])

    label = request.form['label']
    annotate_for = int(request.form['annotate_for'])
    index_range = list(range(index - (annotate_for - 1) // 2, index + (annotate_for - 1) // 2 + 1))

    annotations = []

    with open(os.path.join(record_path, target, filename + '.csv'), 'r') as annotation_file:
        for info in annotation_file.readlines():
            i, l = info.split(',')
            i, l = int(i), l.strip() if not l.strip() == 'end' else -1

            annotations.append(label if i in index_range else l)

    with open(os.path.join(record_path, target, filename + '.csv'), 'w') as annotation_file:
        for i, l in enumerate(annotations):
            annotation_file.write("%d,%s\n"%(i,l))

    # Return empty header
    return "", 204

