import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from colorama import Fore
from colored import fg
import time

data = json.load(open("data.json"))

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://www.higherlowergame.com")
time.sleep(1)

btnStart = driver.find_element(By.XPATH, '//*[@id="root"]/div/span/section/div[2]/div/button[1]')
btnStart.click()
time.sleep(1)

while True:
    txtLeft = driver.find_element(By.XPATH, '//*[@id="root"]/div/span/span/div/div[2]/div[1]/div[1]/div/div[1]/p[1]').text.split("“")[1].split("”")[0].strip()
    txtRight = driver.find_element(By.XPATH, '//*[@id="root"]/div/span/span/div/div[2]/div[1]/div[2]/div/div[1]/p[1]').text.split("“")[1].split("”")[0].strip()
    numLeft = driver.find_element(By.XPATH, '//*[@id="root"]/div/span/span/div/div[2]/div[1]/div[1]/div/div[2]/p[1]').text

    btnHigher = driver.find_element(By.CSS_SELECTOR, '#root > div > span > span > div > div.game > div.term-actions > button.game-button.term-actions__button.term-actions__button--higher')
    btnLower = driver.find_element(By.CSS_SELECTOR, '#root > div > span > span > div > div.game > div.term-actions > button.game-button.term-actions__button.term-actions__button--lower')

    btnHigher.click() if data[txtLeft] < data[txtRight] else btnLower.click()
    time.sleep(4)