from app.routes.app import create_app  # , socketio
from config import Config

app = create_app()
app.config.from_object(Config)

if __name__ == "__main__":
    # socketio.run(app, debug=True, use_reloader=False)
    app.run(debug=True, use_reloader=False)
