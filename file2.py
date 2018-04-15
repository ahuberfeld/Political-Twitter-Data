#!/usr/bin/env python3
import re

#In this file, we isolate the tags in the politicians' tweets and in President Trump's tweets

#We can run the same program on both the old and new tweets
#The politicians' tweets file has a column which lists all tags listed in each tweet
def tagSort(fileName):
    tweets = open(fileName+"Tweets.csv")
    tags = open(fileName+"Tags.txt", "w")

    pattern = re.compile(r"\{.+?\}") #in the file, the tags are surrounded by brackets

    found = ""
    line = tweets.readline()
    while line:
        fields = line.split(";") #the file is semicolon delimited
        
        if (len(fields)>4): #many of the tweets are incomplete and missing data, so that must be worked around
            found = fields[4] #the tags are listed in the 5th column
            
            if re.search(pattern, found):
                found = found.replace('\"{', "\n").replace('}\"', "").replace(",", "\n") #each tag is surrounded by brackets and we want to clean that up
                party = partySort(fields[1]) #what party does the politician who tweeted this belong to?
                words = found.split("\n") #print the tags and the politicians' political parties cleanly to a new file
                for word in words:
                    if word != "": #make sure no empty spaces are printed, because then only the party name will be printed and the data will be skewed
                        tags.write(word)
                        tags.write(" ")
                        if party is not None: #sometimes the party isn't listed
                            tags.write(party)
                            tags.write("\n")
                            
        line = tweets.readline()
    tweets.close()
    tags.close()

    
def partySort(idNum): #each tweet has a Twitter account number. The file PoliticianAccountInfo has a list of every politician's account number and party affiliation.
    polInfo = open("PoliticianAccountInfo.csv")
    line = polInfo.readline()
    while line:
        fields = line.split("|") # the data is pipe delimited
        if fields[0] == idNum: #when you found the account of the politician who tweeted the tag
            return fields[10] #return their political party
        line = polInfo.readline()



#The trump data doesn't have hashtags automatically pulled out, so we have to search for them
def trumpSort():
    tweets = open("trumpTweets.txt")
    trumpTags = open("trumpTags.txt", "w")

    pattern = re.compile(r"#\S*", re.IGNORECASE) #look for hashtags
    
    line = tweets.readline()
    while line:
        fields = line.split("|") #this is a pipe deliminated file
        if(len(fields)>1): #if the data on this line of the file is complete
            tags = re.findall(pattern, fields[0]) #find any tags listed
            for tag in tags: #if there were multiple tags in a tweet
                tag = tag.replace("#", "\n") #remove the hastag symbol and replace it with a newline character, that way it can be easily read and sorted
                trumpTags.write(tag) #write it to a file with all the tags
        line = tweets.readline()

    tweets.close()
    trumpTags.close()

tagSort("pre") #run the program fom pre-election politician data
tagSort("post")#run the program fom post-election politician data
trumpSort() #run the program for Trump's data

