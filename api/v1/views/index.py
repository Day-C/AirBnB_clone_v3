#!/usr/bin/python3
'''Endpoint toto display status and states data.'''
from api.v1.views.__init__ import app_views
from flask import jsonify
from models.engine.db_storage import DBStorage


storage = DBStorage()
storage.reload()


@app_views.route('/status')
def show_status():
    '''Displau status data in json format.'''

    return jsonify({"status": "OK"})


@app_views.route('/stats')
def obj_count():
    '''Retrive and count number of each onject by type.'''

    all_objs = storage.all(None)
    cls_cnt = {}
    for obj in all_objs.keys():
        name_id = obj.split('.')
        if name_id[0] in cls_cnt:
            cls_cnt[name_id[0]] = cls_cnt[name_id[0]] + 1
        else:
            cls_cnt[name_id[0]] = 1
    return jsonify(cls_cnt)
