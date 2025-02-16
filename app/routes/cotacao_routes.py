from flask import Blueprint
from app.controllers.cotacao_controller import cotacoes, cotacao_especifica

cotacao_bp = Blueprint('cotacao', __name__)

cotacao_bp.route('/cotacoes', methods=['GET'])(cotacoes)
cotacao_bp.route('/cotacoes/<moeda>', methods=['GET'])(cotacao_especifica)
