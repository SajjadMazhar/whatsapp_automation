from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome(executable_path="/home/navgurukul/Desktop/selenium/chromedriver")
driver.maximize_window()
driver.get("https://web.whatsapp.com/")

input("Press enter to continue")

user = driver.find_element_by_css_selector("span[title='+91 88206 87769']")
user.click()

textInput=driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]")
for i in range(10):
    textInput.send_keys("Happy Birthday")
    time.sleep(1)
    textInput.send_keys(Keys.RETURN)