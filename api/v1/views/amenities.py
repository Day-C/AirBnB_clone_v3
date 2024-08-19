#!/usr/bin/python3
"""Amenity api handler"""
import models
from . import app_views
from models.amenity import Amenity
from flask import jsonify, abort, request


@app_views.route("/amenities")
def show_amenities():
    """retive all amenities from storage"""

    amenities = models.storage.all(Amenity)
    amens = []
    for key in amenities.keys():
        amens.append(key.to_dict())
    return jsonify(amens)

@app_views.route("/amenities/<str:amenity_id")
def show_this_amenity(amenity_id):
    """Retive a specific ameeniit"""

    amenity = models.storage.get(Amenity, amenity_id)
    if amenity == None:
        abort(404)
    return jsonify(amenity.to_dict())

@app_views.route("/amenities/amenity_id", methods=["DELETE"])
def delete_this_amenity(amenity_id):
    """Remove an amenity from storage"""

    amenity = models.storage.get(Amenity, amenity_id)
    if amenity == None:
        abort(404)
    amenity.delete()
    return {}, 200


@app_views.route("/amenities", methods=["POST"])
def create_an_amenity():
    """Create new amenity"""

    if request.headers['Content-Type'] == 'application/json':
        abort(404, "Not a JSON")
    data = request.get_json()
    if 'name' not in data:
        abort(400, "Missing name")
    amenity = Amenity(** data)
    amenity.save()
    return jsonify(amenity.to_dict()), 201

@app_views.route("/amenities/<str:amenity_id", methods=["PUT"])
def edit_amenity(amenity_id):
    """modify an existing amenity"""

    amenity = models.storage.get(Amenity, amenity_id)
    if amenity == None:
        abort(404)
    if request.headers['Content-Type'] != 'application/json':
        abort(404, "Not a JSON")
    data = request.get_json()
    ignores = ["id", "created_a", "updated_at"]
    for key in datta.keys():
        if key not in ignores:
            amenity.__dict__[key] = data[key]
    updated_amen = amenity
    amenity.delete()
    updated_amen.save()
    return jsonify(updated_amen.to_dict()), 201
