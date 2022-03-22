# -*- coding: utf-8 -*-
"""
Created on Fri Jun 25 20:30:03 2021

@author: xFranco99
"""

import time
import pyautogui
from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#Path WebDriver
webDriverPath = 'path\chromedriver.exe'

#apri chrome web driver
driver = webdriver.Chrome(webDriverPath)
driver.maximize_window()

#apri whatsapp web e premi un tasto dopo aver scannerizzato il QR
driver.get('https://web.whatsapp.com/')


WebDriverWait(driver, 20).until(
                EC.presence_of_element_located(
                    (By.XPATH,
                     '//*[@id="app"]/div[1]/div/div[2]/div[1]/div/div[3]/label/input'))).click()

input('Premi un tasto per continuare: ')

#semaforo
#(serve per evitare che il programma spammi meme finchè non si cambia frase)
ok = 0

while True:

    #dammi l'ultimo messaggio testuale, se c'è un problema ricomincia il loop
    try:
        txt = driver.find_elements_by_xpath(
            "//div[@class='copyable-text']")[-1].text
        
        #evita case sensitive
        txt = txt.upper().strip()
    except:
        pass
    
    #stampa l'ultimo messaggio
    print(txt)
    
    #se l'ultimo messaggio è "cringe" manda il catto cringe
    if ('CRINGE' in txt):
        
        #se il semaforo è 0 manda il catto e metti il semaforo a 1
        if ok == 0:
            
            Reply = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located(
                    (By.XPATH,
                     '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]')))
            
            Reply.click()
        
            #invia con pyautogui l'oggetto copiato in precedenza
            pyautogui.hotkey('ctrl', 'v')
            time.sleep(1)
            pyautogui.press('enter')
            
            ok = 1
    else:
        
        #altrimenti rimetti il semaforo a 0
        ok = 0
        