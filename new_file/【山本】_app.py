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
from app.routes.profile_search import profile_search_bp #検索機能追加7/26




def create_app():
    app = Flask(
        __name__,
        template_folder=os.path.join(os.path.dirname(__file__), "..", "templates"),
        static_folder=os.path.join(os.path.dirname(__file__), "..", "static"),
        static_url_path="/static",
    )
    app.config.from_object(Config)
    db.init_app(app)

    # ✅ DBファイルとフォルダの自動作成
    db_path = app.config["SQLALCHEMY_DATABASE_URI"].replace("sqlite:///", "")
    db_dir = os.path.dirname(db_path)
    if not os.path.exists(db_dir):
        os.makedirs(db_dir, exist_ok=True)

    # ✅ DBがなければテーブルを作成
    if not os.path.exists(db_path):
        with app.app_context():
            db.create_all()
            print("✅ Database and tables created successfully.")

    # ✅ Blueprint登録
    app.register_blueprint(auth_bp)
    app.register_blueprint(profile_bp)
    app.register_blueprint(recommend_bp)
    app.register_blueprint(recommend_profile_bp)
    app.register_blueprint(like_push_bp)
    app.register_blueprint(profile_search_bp) #検索機能追加7/26

    # ✅ ホーム画面（おすすめ表示）
    @app.route("/home")
    def home():
        if "user_id" not in session:
            return redirect("auth.login")
        current_user = User.query.get(session["user_id"])
        if not current_user:
            return redirect("auth.login")

        recommended = (
            User.query.filter(
                User.language == current_user.language,
                User.dev_field == current_user.dev_field,
                User.id != current_user.id,
            )
            .limit(6)
            .all()
        )
        return render_template("main/home.html", profiles=recommended)

    # ✅ ユーザー一覧
    @app.route("/users")
    def users():
        if "user_id" not in session:
            return redirect("auth.login")
        all_users = User.query.all()
        return render_template("users.html", users=all_users)

    return app
