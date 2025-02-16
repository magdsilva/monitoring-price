from app.utils.navegador import iniciar_navegador
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime

def pegar_cotacao(url, nome_ativo):
    driver = iniciar_navegador()
    driver.get(url)
    
    try:
        valor = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'span.base.yf-ipw1h0[data-testid="qsp-price"]'))
        ).text
        return {
            "CAPITAL": nome_ativo,
            "COTAÇÃO": valor,
            "FONTE": url,
            "CONSULTADO EM": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
    except Exception as e:
        return {"erro": f"Erro ao pegar a cotação de {nome_ativo}: {str(e)}"}
    finally:
        driver.quit()
