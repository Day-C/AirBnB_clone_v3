#!/usr/bin/python3
'''States api actions.'''
from api.v1.views.__init__ import app_views
from models.state import State


all_instances = State()
all_dict_instances = all_instances.to_dict()


@app_views.route('api/v1/states', method=['GET'])
def show_states():
    '''Retives the list if all states.'''

    return jsonify(all_states)
