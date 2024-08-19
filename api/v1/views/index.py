#!/usr/bin/python3
'''Endpoint toto display status and states data.'''
from . import app_views
from flask import jsonify
import models
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.review import Review
from models.place import Place
from models.state import State

classes = {"amenities": Amenity, "cities": City, "places": Place, "reviews": Review, "states": State, "users": User}

@app_views.route('/status')
def show_status():
    '''Displau status data in json format.'''

    stus = {"status": "OK"}
    return jsonify(stus)


@app_views.route('/stats')
def obj_count():
    '''Retrive and count number of each onject by type.'''

    results = {}
    for key in classes.keys():
        results[key] = models.storage.count(classes[key])

    return jsonify(results)
