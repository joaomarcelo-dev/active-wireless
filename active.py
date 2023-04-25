from selenium import webdriver;
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
import os

options = Options()
options.page_load_strategy = 'eager'
driver = webdriver.Chrome(options=options)

driver = webdriver.Chrome()

driver.get("http://10.0.0.1/#/login")

sleep(2)

use_login = driver.find_element(By.XPATH, '//*[@id="login-user"]');
use_login.send_keys('technet');

password_login = driver.find_element(By.XPATH, '//*[@id="login-password"]');
password_login.send_keys('tech1010');

button_login = driver.find_element(By.XPATH, '//*[@id="button-login"]');
button_login.send_keys(Keys.RETURN);

sleep(8)


driver.find_element(By.XPATH, '//*[@id="card-networks-list"]').click();

sleep(5)

netWorks = ["wifi-1", "wifi-2"]

for netWork in netWorks:
  os.system('clear')
  driver.execute_script(f"const redeTest = document.querySelector('#{netWork} .toggle-circle'); redeTest.click(); console.log(redeTest)")
  print('============================================================')
  print(f'|| Rede ({netWork}) desativada!!                          ||')
  print('============================================================')
  sleep(50)
  driver.execute_script("location.reload()")
  sleep(10)


os.system('clear')
print('=====================================')
print('|| Todas as redes foram alteradas  ||')
print('||           Com exito!!!          ||')
print('||                                 ||')
print('||        Tenha um bom dia ;)      ||')
print('=====================================')

sleep(5)

