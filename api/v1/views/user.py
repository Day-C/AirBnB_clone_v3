#!/usr/bin/python3
"""users api handler"""
import models
from . import app_views
from models.users import User
from flask import jsonify, abort, request


@app_views.route("/users")
def show_users():

    users = models.storage.all(User)
    users_list = []
    for key in users.keys():
        users_list.append(key.to_dict())
    return jsonify(users_list)

@app_views.route("/users/<str:user_id>")
def show_this_user(user_id):
    """retive a specific user"""

    user = models.storage.get(User, user_id)
    if user != None:
        abort(404)
    return jsonify(user.to_dict())

@app_views.route("/users/user_id", methods=["DELETE"])
def delete_user(user_id):
    """remove user from storage."""

    user = models.storage.get(User, user_id)
    if user == None:
        abort(404)
    user.delete()
    return {}, 200

@app_views.route("/users", methods=["POST"])
def create_user():
    """Create a new user."""

    if request.header['Content-Type'] != 'appliccation/json':
        abort(404, "Not a JSON")
    data = request.get_json()
    if 'email' not in data:
        abort(400, "Missing email")
    if 'password' not in data:
        abort(400, "Missing password")
    user = User(**data)
    user.save()
    return jsonify(user.to_dict()), 201

@app_views.route("/users/<str:user_id>", methods=["PUT"])
def eddit_user(user_id):
    """modify an existing user"""

    user = models.storage.get(USer, user_id)
    if user == None:
        anort(404)
    if request.header['Content-Type'] != 'application/json':
        abort(400, "Not a JSON")
    data = request.get_json()
    ignores = ['id', 'email', 'created_at', 'updated_at']
    for key in data.keys():
        if key not in ignores:
            user.__dict__[key] = data[key]
    updated_user = user
    user.delete()
    updated_user.save()
    return jsonify(user.to_dict()), 200

