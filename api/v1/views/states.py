#!/usr/bin/python3
"""state api handler."""
import models
from . import app_views
from models.state import State
from flask import jsonify, abort, request


@app_views.route("/states")
def show_states():
    """retrive all states from storage."""

    all_states = models.storage.all(State)
    states_list = []
    for key in all_states.keys():
        states_list.append(key.to_dict())

    return jsonify(states_list)

@app_views.route("/states/state_id")
def this_state(state_id):
    """Retirves a state with specific id."""

    state = models.storage.get(State, state_id)
    if state == None:
        return 404
    return jsonity(state.to_dict())


@app_views.route("/states/state_id", methods=["DELETE"])
def delete_this_state(state_id):
    """removes a state with secified id from storage"""

    state = models.storage.get(State, state_id)
    if state == None:
        abort(404)
    state.delete()
    return {}, 200

@app_views.route("/states", methods=["POST"])
def create_state():
    """create a new instance if state class and saves it"""

    state_info = request.get_json()
    if request.headers['Content-Type'] != 'application/json':
        abort(400)
    if 'name' not in state_info:
        abort(400)
    new_state = State(**state_info)
    new_state.save()
    return jsonify(new_state.to_dict()), 201


@app_views.route("/states/state_id", mothods=["PUT"])
def eddit_this_state(state_id):
    """Eddit and esistring state and stave changes"""

    state = models.storage.get(State, state_id)
    if state == None:
        about(404)
    if request.headers['Content-Type'] != 'application/json':
        abort(400)
    new_data = request.get_json()
    new_state = state
    for key in new_data.keys():
        new_state.__dict__[key] = new_data[key]

    state.delete()
    new_state.save()
    return jsonify(new_state.to_dict()), 200
