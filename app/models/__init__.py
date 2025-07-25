from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from .user import User
from .likes import Likes
from .chat_messages import ChatMessage
