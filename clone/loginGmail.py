from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

options= webdriver.ChromeOptions()
driver= webdriver.Chrome(options=options)
driver.get ('https://accounts.google.com/')

driver.find_element(By.ID,"identifierId").send_keys("Cathy.traninc@gmail.com")
sleep(5)
driver.find_element(By.ID,"identifierNext").click ()
sleep(3)
driver.find_element(By.NAME,"Passwd").send_keys("tranhongcam306")         
sleep(3)  
driver.find_element(By.ID,"passwordNext").click ()

print ("logged is successfully")