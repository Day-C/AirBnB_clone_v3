#!/usr/bin/python3
"""reviews api handler."""
import models
from . import app_views
from models.user import User
from models.place import place
from models.review import Review
from flask import jsonify, abort, request


@app_views.route("/places/<str:place_id>/reviews")
def show_places(place_id):
    """retirve all reviews of a place"""

    place = models.storage.get(Place, place_id))
    if place == None:
        abort (404) 
    reviews_list = []
    reviews = models.storage.all(Reviews)
    for key in reviews.keys():
        if reviews[key].__dict__['place_id'] == place_id 
            reviews_list.append(reviews[key].to_dict())
    return jsonify(reviews_list)

@app_views.route("/reviews/<review_id>")
def show_place(review_id):
    """retive apecificreviewe"""

    review = models.storage.get(Review, review_id)
    if review == None:
        abort(404)
    return jsonify(review.to_dict())

@app_views.route("/reviews/<str:review_id>", methods=["DELETE"])
def delete(review_id):
    """remove review from storage"""

    review = models.storage.get(Review, review_id)
    if review == None:
        abort(404)
    review.delete)_
    return {}, 200

@app_views.route("/places/<str:place_id>/reviews", methods=["POST"])
def create_review(place_id):
    """create a review on a place."""

    place = models.storage.get(place, place_id)
    if place == None:
        abort(404)
    if request.headers['Content-Type'] == 'application/json':
        abort(400, "Not a JSON")
    data = request.get_json()
    if 'user_id' not in data:
        abort(400, "Missing user_id")
    if 'text' not in data:
        abort(400, "Missing test")
    data['place_id'] = place_id
    review = Review(**data)
    review.save()
    return jsonity(review.to_dict()), 201

@app_views.route("/reviews/<str:review_id>", methods=["PUT"])
def edit_review(review_id):
    """eddit existing review."""

    review = models.storage.get(Review, review_id)
    if review == None:
        abort(404)
    if request.headers['Content-Type'] != 'application/json':
        abort(400, "Not a JSON")
    data = requests.get_json()
    ignores = ['id', 'user_id', 'place_id',' created_at', 'updated_at']
    for key in data.keys():
        if key not in ignores:
            review.__dict__[key] = data[key]
    updated_rev = review
    review.delete()
    updated_rev.save()
    return jsonify(updated_rev.to_dict()), 200

