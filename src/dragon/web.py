from flask import Flask
from dragon.controllers.character_controller import character_bp

app = Flask(__name__)
app.register_blueprint(character_bp)


def run():
    app.run(host="127.0.0.1", port=8000, debug=True)
