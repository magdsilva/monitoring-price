# Monitor de Cotações

Este repositório contém um sistema de monitoramento de cotações de moedas e ações utilizando Flask e Selenium. O aplicativo busca cotações em tempo real de ativos financeiros e expõe essas informações por meio de uma API RESTful.
Funcionalidade feita apenas com intuito didático, mostrando a integração de uma consulta com o crawler e web scraping + API.
Fiquem a vontade para contribuir e fazer testes.

## Funcionalidades

- **Obter cotações de diferentes ativos** (exemplo: Dólar, Euro, Ações Petrobras).
- **API RESTful** que retorna as cotações em formato JSON.
- Suporte para consulta de múltiplas cotações ao mesmo tempo ou de cotações específicas.

## Tecnologias

- **Flask**: Framework para criar APIs RESTful em Python.
- **Selenium**: Biblioteca para automação de navegadores, utilizada para buscar os dados de cotação.
- **ChromeDriver**: Usado para controlar o navegador Chrome em modo headless (sem interface gráfica).

## Requisitos

Certifique-se de ter as seguintes dependências instaladas:

- **Python 3.x** (recomendado 3.7 ou superior)
- **Google Chrome** (navegador)
- **ChromeDriver**: Baixe o [ChromeDriver](https://chromedriver.chromium.org/downloads) que seja compatível com a versão do seu Google Chrome. Alternativamente, use o WebDriver Manager para gerenciar a versão do ChromeDriver.

### Dependências Python

Crie e ative um ambiente virtual, se necessário, e instale as dependências:

### Como testar
- Clone o repositório
- Instale as dependências (pip install -r requirements.txt)
- Execute o servicos Flask (python run.py)
- Teste os endpoints:
- ** GettAll: http://localhost:5000/cotacoes
- ** GettEspecífico: http://localhost:5000/cotacoes/<moeda>


- 
```bash
pip install -r requirements.txt

