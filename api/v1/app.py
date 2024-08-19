#!/usr/bin/python3
''' Falsk instance.'''
from .views import app_views
from flask import Flask, jsonify
from models import storage


app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def close_session(exception):
    # Teardown callback.

    storage.close()


@app.errorhandler(404)
def page_not_found(e):
    return jsonify({"error": "Not found"}), 404


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, threaded=True)
