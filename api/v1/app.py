#!/urs/bin/python3
''' Falsk instance.'''
from api.v1.views.__init__ import app_views
from flask import Flask, jsonify
from models.engine.db_storage import DBStorage

storage = DBStorage()
storage.reload()

app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def close(exception):
    #Teardown callback.
    
    storage.close()


@app.errorhandler(404)
def page_not_found(e):
    return jsonify({"error": "Not found"})


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, threaded=True)
