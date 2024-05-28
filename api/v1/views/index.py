#!/usr/bin/python3
'''base for api.'''
from api.v1.views.__init__ import app_views
from flask import jsonify
from models.engine.db_storage import DBStorage

storage = DBStorage()
storage.reload()

status = [
        {
            "status": "OK"
        }
        ]


@app_views.route('/status')
def show_status():
    '''displau json.'''

    return jsonify(status)


@app_views.route('/stats')
def obj_count():
    '''Retrive and count number of each onject by type.'''

    # Retive all objects in the db
    all_objs = storage.all(None)
    cls_cnt = {}
    for obj in all_objs.keys():
        # Split the keys to get objects name
        name_id = obj.split('.')
        if name_id[0] in cls_cnt:
            cls_cnt[name_id[0]] = cls_cnt[name_id[0]] + 1
        else:
            cls_cnt[name_id[0]] = 1
    return jsonify(cls_cnt)
