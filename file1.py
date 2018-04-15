#!/usr/bin/env python3
import re

#In this file, we sort the politicians' tweets into before Trump's election as President of the United States, and after the election

file = open("pol_tweets.csv")
post = open("postTweets.csv", "w")
pre = open("preTweets.csv", "w")
line = file.readline()

#create a regex to allow the tweets to be sorted by year, pre- or post-election
pattern1 = re.compile(r"201[0-5]-[0-9]{2}-[0-9]{2}") #all tweets from 2010-2015
pattern2 = re.compile(r"2016-0[0-9]-[0-9]{2}")#tweets from 2016 before the election, single digit months
pattern3 = re.compile(r'2016-10-[0-9]{2}')#tweets from October 2016, before the election
pattern4 = re.compile(r"2016-1[12]-[0-9]{2}") #all tweets from November and December of 2016, after the election
pattern5 = re.compile(r"201[7]-[0-9]{2}-[0-9]{2}") #all tweets in  2017


while line: #sort each tweet into its proper file
    if re.search(pattern1, line): pre.write(line)
    if re.search(pattern2, line): pre.write(line)
    if re.search(pattern3, line): pre.write(line)
    if re.search(pattern4, line): post.write(line)
    if re.search(pattern5, line): post.write(line)
    
    line  = file.readline()


file.close()
pre.close()
post.close()
