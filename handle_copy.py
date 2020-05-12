import time
import getpass
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
from selenium.webdriver.common.keys import Keys
import shutil

src='./helper_dir'
des='./csv_files'

l=os.listdir(path=src)
print(l)

for i in l:
	if(i[-5]!=')'):
		shutil.copy(src+'/'+i,des)
