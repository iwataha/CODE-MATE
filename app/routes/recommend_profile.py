from flask import Blueprint, render_template
from app.models.user import User

# ユーザープロフィール表示にユーザー情報を渡すファイル

recommend_profile_bp = Blueprint("recommend_profile", __name__)


@recommend_profile_bp.route("/user/<int:user_id>")
def recommend_profile(user_id):
    user = User.query.get_or_404(user_id)
    return render_template("user_register.html", user=user)
