from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains

chrome_option= webdriver.ChromeOptions()
chrome_option.add_argument ("--disable-notifications")
driver= webdriver.Chrome(chrome_option)
sleep(1)
driver.get ('https://kenh14.vn/')
driver.maximize_window()
sleep(5) 


#Musik = driver.find_element(By.XPATH,'//a[@href="/musik.chn"]')
#Musik.click()
#sleep(4)

#Vietnam = driver.find_element(By.XPATH,'//*[@id="admWrapsite"]/div[2]/div[3]/div/div[2]/div/ul/li[4]/a')
#print(f'title:{Vietnam.text}')
#Vietnam.click()
#sleep(5)

#Newspaper = driver.find_element(By.XPATH,'//div//h3/a[@href="/hoang-thuy-linh-se-moi-den-vau-lam-khach-moi-vietnamese-concert-20230919141715243.chn"]')
#print(f'title:{Newspaper.text}')
#Newspaper.click()
#sleep(5)

#scrolldown
#driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#sleep(2)

Search= driver.find_element(By.ID,'searchinput')
Search.send_keys('rap viet',Keys.ENTER) #Enter
sleep(5)

#Iconsearch= driver.find_element(By.XPATH,'//a[@href="javascript:void(0);"]')
#Iconsearch.click ()
#sleep(3)

#FullBody = driver.find_element(By.XPATH, '//*[@id="form1"]/div[3]/div[3]/div[1]/div/div/div[1]/div[2]')
#List = FullBody.find_elements(By.XPATH, '//div[2]/h3')
#for i in List:
    #x= i.find_element (By.TAG_NAME,'a')
    #print (x.text) 
    #print (x.get_attribute('href'))
    #print ('===============')
#sleep(3)

#FullBody = driver.find_element(By.XPATH, '//*[@id="form1"]/div[3]/div[3]/div[1]/div/div/div[1]/div[2]')

#Image = FullBody.find_elements(By.XPATH, '//div[1]/a/img')
#for img in Image:
    #print (img.get_attribute('src'))
    #print ('================')
#driver.save_screenshot ('ABC.png')
#Image= urllib.urlretrieve(source)

# Print number of images
#Image = driver.find_elements(By.TAG_NAME,'img')
#print(f'There are {len(Image)} images.')

#linktext= driver.find_element(By.XPATH,'//div[1]/a/img')
#action= ActionChains(driver)
#action.context_click(linktext).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform()
#sleep(10)

#dot= driver.find_element(By.XPATH,'//*[@id="k14-main-menu-wrapper"]/div/div/ul/li[15]')
#action= ActionChains(driver)
#hoveron= action.move_to_element(dot).perform()
#sleep(5)

driver.back()
print("Current Page title after back: " + driver.title)
sleep(5)

driver.refresh()
driver.forward()