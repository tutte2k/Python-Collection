from numpy import NaN
import requests
from bs4 import BeautifulSoup
import pandas as pd
import time as t
import os
import numpy as np
from time import time, sleep


URL = "https://dura-online.com/?online"
batch = 0
while True:
    characters = []
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    table = soup.find_all('table')[1]
    children = table.findChildren("tr", recursive=False)
    unixSeconds = int(t.time())
    children.remove(children[0])
    for child in children:
        name = child.text.rstrip().lstrip().split('\n')[0]
        level = child.text.rstrip().lstrip().split('\n')[1]
        vocation = child.text.rstrip().lstrip().split('\n')[2]
        online = True
        unix = unixSeconds
        timespan = 0
        duration = 0
        color = 0
        characters.append([name, level, vocation, online,
                        unix, timespan, duration, color, batch])
    
    df = pd.DataFrame(characters)
    df.to_csv('MICHAELQUEPASA.csv', mode='a', index=False,header=False)

    print(f'batch {batch} done')
    batch+=1
    sleep(10 - time() % 10)







