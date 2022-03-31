import requests
import numpy as np
import time
import matplotlib.pyplot as plt
from matplotlib import animation
from bs4 import BeautifulSoup
import pandas as pd
import datetime
import smtplib
import csv
import re
from csv import DictWriter
import matplotlib.pyplot as plt
import numpy as np
import csv
import random
import time
import random
from itertools import count
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

URL='https://www.amazon.in/boAt-Bluetooth-Soundbar-Connectivity-Integrated/dp/B09LMCRWF2'
headers={"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36',"Regerer":''}


print("Fetching product data...")

page=requests.get(URL,headers=headers)         
soup=BeautifulSoup(page.content,'lxml')


title=soup.find(id="productTitle").get_text()
print(title.strip())
prices=[]

fieldnames = ["x_value", "total_1", "total_2"]

        
with open('data.csv', 'w') as csv_file:
            csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            csv_writer.writeheader()

def check_price():
       
        page=requests.get(URL,headers=headers)         
        soup=BeautifulSoup(page.content,'lxml')

        http_proxy  = "http://10.10.1.10:3128"
        https_proxy = "https://10.10.1.11:1080"
        ftp_proxy   = "ftp://10.10.1.10:3128"

        proxyDict = { 
                      "http"  : http_proxy, 
                      "https" : https_proxy, 
                      "ftp"   : ftp_proxy
                    }
           
        price=soup.find(class_='a-offscreen').get_text()
        converted_price=float(price[1:10].replace(",",""))

        time_stamp=datetime.datetime.now()
        time_stamp=time_stamp.strftime("%d-%m-%Y %H:%M:%S")
        print(time_stamp+" Price is now "+price)
        prices.append(converted_price)
 
        x_value = time_stamp
        total_1 = converted_price
        total_2 = 1000
        
            

        with open('data.csv', 'a') as csv_file:
                csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

                info = {
                    "x_value": x_value,
                    "total_1": total_1,
                    "total_2": total_2
                }
               

                csv_writer.writerow(info)

        

          
      
while(True):        
  check_price()

 
  
