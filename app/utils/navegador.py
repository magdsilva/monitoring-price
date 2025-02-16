from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

def iniciar_navegador():
    options = webdriver.ChromeOptions()
    options.add_argument("--ignore-certificate-errors")
    options.add_argument("--incognito")
    options.add_argument("--disable-ssl-errors")
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-webgl")
    options.add_argument("--disable-software-rasterizer")
    options.add_argument("--no-proxy-server")
    options.headless = True
    
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    return driver
