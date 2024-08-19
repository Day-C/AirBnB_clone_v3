#!/usr/bin/python3
"""places api handler."""
import models
from . import app_views
from models.user import User
from models.city import City
from models.place import place
from flask import jsonify, abort, request


@app_views.route("/cities/<str:city_id>/places")
def show_places(city_id):
    """retirve all places in a city"""

    city = models.storage.get(City, city_id)
    if city == None:
        abort (404)
    places_list = []
    places = models.storage.all(Place)
    for key in places.keys():
        places_list.append(places[key].to_dict())
    return jsonify(places_list)

@app_views.route("/places/<place_id>")
def show_place(place_id):
    """retive apecific place"""

    place = models.storage.get(Place, place_id)
    if place == None:
        abort(404)
    return jsonify(place.to_dict())

@app_views.route("/places/<str:place_id>", methods=["DELETE"])
def delete_place(place_id):
    """remove a specified place from storage."""

    place = models.storage.get(Place, place_id)
    if place == None:
        abort(404)
    place.delete()
    return {}, 200

@app_views.route("/cities/<str:city_id>/places", methods=["POST"])
def create_place(city_id):
    """Create a new place"""

    if request.headers['Content-Type'] != 'application/json':
        abort(404, "Not a JSON")
    data = request.get_json()
    if 'user_id' not in data:
        abort(400, "Missing user_id")
    user = models.storage.get(User, data['user_id'])
    if user == None:
        abort(404)
    if 'name' not in data:
        abort(404, "Missing name")
    data['city_id'] = city_id
    place = Place(**data)
    place.save()
    return jsonify(place.to_dict()), 201

@app_views.route("/places/<str:place_id>", methods=["PUT"])
def edit_place(place_id):
    """Modify and already existing place"""

    place = models.storage.get(Place, place_id)
    if place  == None:
        abort(404)
    if request.headers['Content-Type'] != 'application/json':
        abort(400, "Not a JSON")
    data = request.get_json()
    ignores = ["id", "user_id", "city_id", "create_at", "updared_at"]
    for key in data.keys():
        if key not in ignores:
            place.__dict__[key] = data[key]
    updated_plc = place
    place.delete()
    updated_plc.save()
    return jsonify(updated_plc.to_dict()), 200
