import os
from flask import Flask, render_template, session, redirect
from config import Config
from app.models.user import db, User
from app.routes.auth import auth_bp
from app.routes.profile import profile_bp
from app.routes.recommend import recommend_bp
from app.routes.recommend_profile import recommend_profile_bp
from app.routes.like_push import like_push_bp
from flask_migrate import Migrate


def create_app():
    app = Flask(
        __name__,
        template_folder=os.path.join(os.path.dirname(__file__), "..", "templates"),
        static_folder=os.path.join(os.path.dirname(__file__), "..", "static"),
        static_url_path="/static",
    )
    app.config.from_object(Config)
    db.init_app(app)

    with app.app_context():
        db.create_all()

    # Blueprint登録
    app.register_blueprint(auth_bp)
    app.register_blueprint(profile_bp)
    app.register_blueprint(recommend_bp)

    @app.route("/main")
    def main():
        if "user_id" not in session:
            return redirect("auth.top")
        current_user = User.query.get(session["user_id"])
        if not current_user:
            return redirect("auth.top")
        recommended = (
            User.query.filter(
                User.language == current_user.language,
                User.dev_field == current_user.dev_field,
                User.id != current_user.id,
            )
            .limit(6)
            .all()
        )
        return render_template("main/main.html", profiles=recommended)

    @app.route("/users")
    def users():
        if "user_id" not in session:
            return redirect("auth.top")
        all_users = User.query.all()
        return render_template("users.html", users=all_users)

    return app
