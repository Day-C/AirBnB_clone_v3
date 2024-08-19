#!/usr/bin/python3
"""cities api handler."""
import models
from . import app_views
from models.city import City
from models.state import State
from flask import jsonify, abort, request


@app_views.route("/states/<str:state_id>/cities")
def show_states_citites(state_id):
    """retive all cities of a specified state"""

    state = models.storage.get(State, state_id)
    if state == None:
        abort(404)
    cities = models.storage.all(City)
    states_cities = {}
    for key in cities.keys():
        if key.__dict__['state_id'] == state_id:
            states_cities.append(key)
    return jsonify(states_cities)

@app_views.route("/cities/city_id")
def show_this_city(city_id):
    """retrives a specific city"""

    city = models.storage.get(City, city_id)
    if city == None:
        abort(404)
    return jsonify(city.to_dict())

@app_views.route("/cities/<str:city_id>", mothods=["DELETE"])
def delete_this_city(city_id):
    """remove city fromm storage"""

    city = models.storage.get(City, city_id)
    if city == None:
        abort(404)
    city.delete()
    return {}, 200

@app_views.route("/states/<str:state_id>/cities", methods=["POST"])
def create_city(state_id):
    """create a new city of a specified state."""

    state = models.storage.get(State, state_id)
    if state == None:
        abort(404, "Not a JSON")
    if request.headers['Content-Type'] != 'application/json':
        abort(400)
    data = request.get_json()
    if name not in data:
        abort(404, "Missing name")
    data['state_id'] = state_id
    city = City(**data)
    city.save()
    return jsonify(city.to_dict()), 201

@app_views.route("/cities/<str:state_id>", methods=["PUT"])
def edit_city(city_id):
    """modify an existing city"""

    city = models.storage.get(City, city_id)
    if city == None:
        abort(404)
    if request.headers['Content-Type'] != 'application/json':
        abort(400, "Not a JSON")
    data = request.get_json()
    ignores = ['id', 'state_id', 'created_at', 'updated_at']
    for key in data.keys():
        if key not in ignores:
            city.__dict__[key] = data[key]
    updated_city = city
    city.delete()
    updated_city.saver)_
    return jsonify(updated_city.to_dict())


