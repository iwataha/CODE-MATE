from flask import Blueprint, render_template, session, jsonify
from app.models.user import User
from app.models.likes import Likes

# likes_view_bpは、いいねの送信と受信を表示するためのBlueprintです。
# いいねを送信したユーザーと受信したユーザーの情報を取得し、テンプレートに渡します。
likes_view_bp = Blueprint('likes_view', __name__)

@likes_view_bp.route('/likes/sent')
def get_likes_sent():
    user_id = session.get("user_id")
    if not user_id:
        return jsonify({"error": "not logged in"}), 401

    likes = Likes.query.filter_by(from_user=user_id,matched=False).all()
    like_sent = []
    for l in likes:
        u = User.query.get(l.to_user)
        if u:
            like_sent.append({
                "id": u.id,
                "name": u.name,
                "email": u.email,
                "language": u.language,
                "dev_field": u.dev_field,
                "experience": u.experience,
                "introduction": u.introduction,
                "image_path": u.image_path,
            })
    #return jsonify(like_sent)
    return render_template("auth/likes_sent.html", like_sent=like_sent)


@likes_view_bp.route('/likes/received')
def get_likes_received():
    user_id = session.get("user_id")
    if not user_id:
        return jsonify({"error": "not logged in"}), 401

    likes = Likes.query.filter_by(to_user=user_id,matched=False).all()
    like_received = []
    for l in likes:
        u = User.query.get(l.from_user)
        if u:
            like_received.append({
                "id": u.id,
                "name": u.name,
                "email": u.email,
                "language": u.language,
                "dev_field": u.dev_field,
                "experience": u.experience,
                "introduction": u.introduction,
                "image_path": u.image_path,
            })
    return render_template("auth/likes_received.html", like_received=like_received)