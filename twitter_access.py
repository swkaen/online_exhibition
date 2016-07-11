# -*- coding: utf-8 -*-
import json
import urllib.request
import os
import sys
import re
from twitter import *
import time

# with open("secret.json") as f:
#     secret_json = json.load(f)

previous_user = ""

def twitter_access(secret_json):
    t = Twitter(auth=OAuth(secret_json["access_token"],
                       secret_json["access_token_secret"],
                       secret_json["consumer_key"],
                       secret_json["consumer_secret"]))
    return t

def get_my_profile(twitter_OAuth):
    return twitter_OAuth.account.verify_credentials()

def get_user_profile(twitter_OAuth, name):
    return  twitter_OAuth.users.show(screen_name=name)

def get_user_time_line(twitter_OAuth, name):
    return twitter_OAuth.statuses.user_timeline(screen_name=name, count=200)

def get_friends_list(twitter_OAuth):
    return twitter_OAuth.statuses.mentions_timeline()

#screen_name -> time_line
def protected_checker(twitter_OAuth, name):
    try:
        time_line = get_user_time_line(twitter_OAuth, name)
        return time_line
    except:
        print('this user has been protected:(')
        return 0
#time_line -> friends_list
def friends_finder(time_line):
    mention_count = {}
    friends = []
    #print('getting user stream...')
    #print('find best friend...')
    for mention in time_line:
        mention_screen_name = mention['in_reply_to_screen_name']
        if mention_screen_name is not None:
            keys = mention_count.keys()
            if mention_screen_name in keys :
                mention_count[mention_screen_name] = mention_count[mention_screen_name] + 1
            else:
                mention_count.update({mention_screen_name:1})
    for k, v in sorted(mention_count.items(), key=lambda x:x[1], reverse=True):
        friends.append(k)
    return friends

#friends_list -> time_line*3
def finder_counter(twitter_OAuth, friends_list):
    list = []
    screen_names = []
    for friend in friends_list:
        friend_time_line = protected_checker(twitter_OAuth, friend)
        if friend_time_line != 0 and len(list) > 3:
            list.append(friend_time_line)
    return list



def image_saver(user_profile):
    user_name = user_profile["screen_name"]
    user_img_url = user_profile["profile_image_url"].replace('_normal', "")
    print(user_img_url)
    with open(user_name + '.png', 'wb') as f:
        img = urllib.request.urlopen(user_img_url).read()
        f.write(img)
        print("="*100)
        print("done!")
        print("="*100)


if __name__ == '__main__':

    MY_SCREEN_NAME = 'lelehanto'
    secret_json = {
  "access_token": "102966386-TxS8sXOlncQAEF1llRVDsWFKMHFyDvKNMi6R7e73",
  "access_token_secret": "RoFcg4KrimWSpvCGJ75Sr0lnaZpJRMPVQKBJujOQIX9zv",
  "consumer_key": "9zH6DJt1IMZBjG0nhDjIxIH0m",
  "consumer_secret": "uPHVy4KTWOy1C5rpQC3q2jPBfppoDGYEY18nfxnkycUGoqDx9V"}

    t = twitter_access(secret_json)
    profile = get_user_profile(t, MY_SCREEN_NAME)
    image_saver(profile)



