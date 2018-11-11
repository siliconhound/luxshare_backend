from app.models.user import User
from functools import wraps
from flask import jsonify

def user_exists(f):

    @wraps(f)
    def f_wrapper(*args, **kwargs):
        username = kwargs["username"]
        user = User.first(username=username)

        if user is None:
            return jsonify({"message": f"user {username} not found"}), 404

        del kwargs["username"]
        kwargs["user"] = user

        return f(*args, **kwargs)

    return f_wrapper

    