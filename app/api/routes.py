from app.models.user import User
from app import db
from . import bp
from flask import jsonify

@bp.route("/user/<string:username>")
def get_user(username):
  # print("get me "+username)
  # return jsonify(User.first(username=username))
  # return "hola " + username
  pass

@bp.route("/user/<string:username>", methods=["PATCH"])
def edit_user(username):
  pass

@bp.route("/user/<string:username>/posts")
def get_user_posts(username):
  pass

@bp.route("/user/<string:username>/comments")
def get_user_comments(username):
  pass