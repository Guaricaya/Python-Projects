from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import *
from time import sleep as s
# -----------------------Configurações_do_bot------------------------#
# caminho para executar navegadores baseados no Google Chrome, para funionar o path deve ser atualizado na varaiavel brave_path.
brave_path = "C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe"
option = Options()
option.headless = True  # Opera em segundo plano o valor defualt opera em primeiro plano
# Caso queira entrar normalmente pelo chrome basta comentar essa linha
# option.binary_location = brave_path
driver = webdriver.Chrome(options=option)
# driver.maximize_window()  # Maximiza a tela
# -----------------------Configurações_do_bot------------------------#


url = "https://www.google.com/"
driver.get(url)
# Achando um elemento com o find_element
element = driver.find_element(By.NAME, "q")
element.click()  # clickando no elemento
element.send_keys("webdriver" + Keys.ENTER)  # digitando com o send_keys.
# Clica procurando um Classe
driver.find_element(By.CLASS_NAME, 'gb_d').click()
print(driver.find_element(By.PARTIAL_LINK_TEXT, 'Fazer').text)
# Clica procurando um texto entre links
driver.find_element(By.PARTIAL_LINK_TEXT, 'Fazer').click()
email = "rafaelbarros240@gmail.com"
s(1)
driver.find_element(By.NAME, "identifier").send_keys(email)
s(2)
driver.back()  # Volta para a pagina anterior
x = [] #Lista para armazenar os elementos 
item = 2 #Indice de busca
try:
    while True:
        x.append(driver.find_element(
            By.XPATH, f'//*[@id="hdtb-msb"]//div[{item}]/a').text)
        item += 1
except NoSuchElementException:
    print("Acabou o varredura")
     

print(x)




driver.close() # Fecha o navegador
