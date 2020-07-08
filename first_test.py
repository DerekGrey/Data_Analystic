a = 199
b = 2
print(a+b)

import pandas as pd
import numpy as np

fire_case = pd.read_csv("fire_in_Seoul_2010_2018 - 복사본.csv",
                                thousands=',',
                                encoding='utf-8'
                                ) #thousands는 천단위로 읽었다는 코드

print(fire_case)
print(fire_case.head())

import googlemaps

gmaps_key = 'AIzaSyCxF9p0e18rdjf1MXyTVK3evaKUeRXmFG0' #키 값 넣기
gmaps = googlemaps.Client(key=gmaps_key)