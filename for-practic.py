# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import time

# path = "C:\Program Files (x86)\chromedriver.exe"
# driver = webdriver.Chrome(path)
# driver.get('https://sadra.blog/')

# # search = driver.find_element_by_class_name('t-input-0-1-8')
# # search.send_keys('قورباغه')
# # search.send_keys(Keys.RETURN)

# link = driver.find_element_by_link_text("چرا رنج کشیدن شما وایرال میشود یا ۳۴ میلیون دنبال‌کننده Mrbeast از کجا آمده‌اند؟")
# link.click()

# # time.sleep(5)

# # element = driver.find_element_by_link_text("رزومه‌ی خود منه")
# # element.click()
# try:
#     element = WebDriverWait(driver, 15).until(
#         EC.presence_of_element_located((By.LINK_TEXT, "Mrbeast"))
#     )
#     element.click()
# except:
#     driver.quit()



# # time.sleep(15)
# # driver.quit


# =======================================================================================================
from random import betavariate
import requests
from bs4 import BeautifulSoup

url = requests.get('https://www.truecar.com/used-cars-for-sale/listings/?page=1')
ss = BeautifulSoup(url.text,'html.parser')
car = ss.find('div',attrs={'class':"card-content vehicle-card-body order-3"})
mileage = car.find('div', attrs={'data-test':"vehicleMileage"}).text
mileage = mileage.replace('miles','')
mileage = mileage.replace(',','')
print(mileage)







