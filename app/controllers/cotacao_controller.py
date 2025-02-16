from flask import jsonify
from app.usecases.cotacao_usecase import pegar_cotacao

def cotacoes():
    ativos = [
        {"url": "https://finance.yahoo.com/quote/BRL=X", "nome": "DÓLAR"},
        {"url": "https://finance.yahoo.com/quote/EURBRL=X", "nome": "EURO"},
        {"url": "https://finance.yahoo.com/quote/PETR4.SA/", "nome": "AÇÕES PETROBRÁS"}
    ]
    
    resultados = []
    for ativo in ativos:
        cotacao = pegar_cotacao(ativo["url"], ativo["nome"])
        resultados.append(cotacao)
    
    return jsonify(resultados)

def cotacao_especifica(moeda):
    ativos = {
        "dolar": {"url": "https://finance.yahoo.com/quote/BRL=X", "nome": "DÓLAR"},
        "euro": {"url": "https://finance.yahoo.com/quote/EURBRL=X", "nome": "EURO"},
        "petrobras": {"url": "https://finance.yahoo.com/quote/PETR4.SA/", "nome": "AÇÕES PETROBRÁS"}
    }
    
    if moeda not in ativos:
        return jsonify({"erro": f"Moeda '{moeda}' não encontrada. Use 'dolar', 'euro' ou 'petrobras'."}), 404
    
    ativo = ativos[moeda]
    cotacao = pegar_cotacao(ativo["url"], ativo["nome"])
    
    return jsonify(cotacao)
