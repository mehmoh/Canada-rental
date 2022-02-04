# -*- coding: utf-8 -*-
"""
Created on Thu Feb  3 23:57:03 2022

@author: mehdi
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Jan 31 02:32:04 2022

@author: mehdi
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Jan 30 18:11:17 2022

@author: mehdi
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Jan 30 18:08:41 2022

@author: mehdi
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Jan 29 14:30:31 2022

@author: mehdi
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd

def extract(page):
    headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36'}
    url=f'https://www.point2homes.com/CA/Houses-For-Rent/QC/Montreal.html?page={page}'
    r=requests.get(url,headers)
    soup=BeautifulSoup(r.content,'html.parser')
    return soup

def transform(soup):
    divs=soup.find_all('div',class_='item-cnt clearfix')    
    for item in divs:
        address=item.find('div',class_='item-address').text.strip().split(',')[0]
        bedroom=item.find('li',class_='ic-beds').text.strip().split(' ')[0]
        bathroom=item.find('li',class_='ic-baths').text.strip().split(' ')[0]
        size_sqf=item.find('li',class_='ic-sqft').text.strip().split(' ')[0].replace(',','')
        price=item.find('div',class_='price has-rental-term').text.strip().split(' ')[0].replace(',','').replace('$','')
        rental={'price':price,
               'Address':address,
               'bedroom':bedroom,
               'bathroom':bathroom,
               'size_sqf':size_sqf,
               'types':'House',
               'city':'Montreal',
               'province':'Quebec'
                
            }
        rentallist.append(rental)

    return 
rentallist=[]

for i in range(1,24):
    try:
        print(f'getting page,{i}')
        c=extract(i)
        transform(c)
    except:
        print('there is an error in that page')
        pass

print(len(rentallist))

df=pd.DataFrame(rentallist)
print(df)

df.to_csv("Montreal_house.csv")

