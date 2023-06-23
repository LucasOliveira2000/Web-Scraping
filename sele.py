import time
from selenium import webdriver
import pandas as pd
import openpyxl
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options


# Configurar as opções do Chrome para executar em modo headless
options = Options()
options.add_argument("--headless")  # Executar em modo headless
options.add_argument("--disable-dev-shm-usage")  # Resolver problema de memória compartilhada

# Colocar as opções ao criar a instância do navegador
driver = webdriver.Chrome(options=options)


driver.get("https://www.kabum.com.br/hardware/placa-de-video-vga")

# Lista para armazenar os dados
dados = []
pagina = 1
product = 1

# Loop para percorrer as páginas
while True:
    try:
        time.sleep(10)
        # Localizar produtos da página
        produtos = driver.find_elements(By.XPATH, "//div[@class='sc-d55b419d-7 ffpHYT productCard']")

        # Para cada produto dentro de produtos, faça
        for produto in produtos:
            try:
                nome_produto = produto.find_element(By.XPATH, ".//span[@class='sc-d99ca57-0 kUQyzS sc-d55b419d-16 fMikXK nameCard']").text
                print(nome_produto)
            except NoSuchElementException:
                nome_produto = "Nome do produto não encontrado"

            try:
                valor_produto = produto.find_element(By.XPATH, ".//span[@class='sc-3b515ca1-2 gybgF priceCard']").text
                print(valor_produto)
            except NoSuchElementException:
                valor_produto = "Valor do produto não encontrado"

            try:
                valor_cartao = produto.find_element(By.XPATH, ".//span[@class='sc-3b515ca1-1 bXmdMv oldPriceCard']").text
                print(valor_cartao)
                print('-' * 50)
            except NoSuchElementException:
                valor_cartao = "Valor do cartão não encontrado"

            print(f"quantidade de produto: {product}")
            product += 1

            # Adicionar os dados à lista
            dados.append({
                "Nome do Produto": nome_produto,
                "Valor do Produto": valor_produto,
                "Valor no Cartão": valor_cartao,
            })

        # Verificar se há próxima página e avançar
        proxima_pagina = driver.find_element(By.XPATH, "//a[@class='nextLink']")

        try:
            proxima_pagina.click()
            print(f"Página atual: {pagina}")
            pagina += 1
        except:
            break
            driver.quit()
            time.sleep(5)
            
    except Exception as e:
        print(f'Ocorreu um erro: {e}')

# Criar um DataFrame com os dados
df = pd.DataFrame(dados)

# Salvar o DataFrame em um arquivo Excel
df.to_excel(r"D:\Python Projetos\Web Scraping - Selenium \ dados_produtos.xlsx", index=False)




            
      





