from app import db
from . import bp
from .common import user_exists
from app.models.user import User
from flask import jsonify, request

@bp.route("/user/<string:username>")
def get_user(username):
  pass


@bp.route("/user/<string:username>", methods=["PATCH"])
@user_exists
def edit_user(user):
  data = request.get_json()

  if not data:
    return jsonify({"message": "no data found"}), 422

  user.update(data)
  db.session.commit()

  return jsonify({"message": "user data saved"})

  


@bp.route("/user/<string:username>/posts")
@user_exists
def get_user_posts(user):
  pass


@bp.route("/user/<string:username>/comments")
def get_user_comments(username):
  pass
