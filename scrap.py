import time
import getpass
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
from selenium.webdriver.common.keys import Keys
import shutil
os.system('clear')

curpath=str(os.path.dirname(os.path.realpath(__file__)))
#path_temp=curpath+"/temperature.txt"

#path for download location
chromeOptions=Options()
chromeOptions.add_experimental_option("prefs",{"download.default_directory":curpath+"/helper_dir"})

#path for chromedriver file
driver = webdriver.Chrome('./chromedriver',chrome_options=chromeOptions)
url='https://hedreports.collegeboard.org/'
# un=input("Enter your username:")
un='iiit6997'
# passw=getpass.getpass()
passw='Ugiiit*20'  
driver.get(url)
username = driver.find_element_by_name("username")
username.send_keys(un)
password = driver.find_element_by_name("password")
password.send_keys(passw)
time.sleep(10)
login = driver.find_element_by_xpath("/html/body/main/div[2]/div/div/div/div/div/div/form/div[3]/button")
login.click()
# time.sleep(5)
print("login succes")

download=driver.find_element_by_xpath("/html/body/nav/div/ul[1]/li[4]/a")
print(download,type(download))
download.click()
time.sleep(15)
print("on download page")

d=driver.find_element_by_xpath("/html/body/main/div[2]/div/div[2]/div/table/tbody/tr[1]/td[6]/div[1]/a")


time.sleep(7)
d.click()

print("downloading success")
time.sleep(10)
driver.quit()








