# coding:utf-8

import pynder

fb_id = ""
fb_token = ""

# session = pynder.Session(fb_id, fb_token)
session = pynder.Session(fb_token)

session.matches() # get users you have already been matched with

# 緯度と経度を指定
LAT = 
LON = 

session.update_location(LAT, LON) # updates latitude and longitude for your profile
session.profile  # your profile. If you update its attributes they will be updated on Tinder.
users = session.nearby_users() # returns a list of users nearby

for user in users:
    print(user.name)
    print(user.schools)
    print(user.bio)
    print(user.age)
    user.like()
