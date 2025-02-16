from flask import Flask

app = Flask(__name__)

from app.routes.cotacao_routes import cotacao_bp

app.register_blueprint(cotacao_bp)
