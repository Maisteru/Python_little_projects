import time
import subprocess
import os
from decouple import config
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from dotenv import load_dotenv

options = webdriver.ChromeOptions()
options.add_argument('--incognito')
driver = webdriver.Chrome("/Users/maisteru/Downloads/chromedriver", options=options)

load_dotenv('settings.env')

IP_NETWORK = os.getenv('IP_NETWORK')
IP_DEVICE = os.getenv('IP_DEVICE')

IP_NETWORK = config('IP_NETWORK')
IP_DEVICE = config('IP_DEVICE')

print(IP_NETWORK)
print(IP_DEVICE)
proc = subprocess.Popen(['ping', IP_DEVICE], stdout=subprocess.PIPE)
while True:
        line = proc.stdout.readline()
        #print(line)
        if not line:
            break
        else:
            None

        try:
            connected_ip = line.decode('utf-8').split()[3].replace(':','')
            if connected_ip == IP_DEVICE:
                subprocess.Popen(['say','Co tam kochanie?'])
                driver.get(config('SITE'))
                break
            else:
                print('Looking for device...')
            time.sleep(1)
        except:
            pass