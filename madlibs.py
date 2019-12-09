#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  7 16:48:42 2019

@author: sharchen
"""

class words:
    """ methods for collecting the inputs from the user """
    def __init__(self):
        """ initializes the stories """
        self.story = 'wedding.txt'
        self.wordlist = self.readFileIntoWordList(self.story)
        self.noun = input("Enter a noun: ")
        self.number = input("Enter a number: ")
        self.verb = input("Enter a verb: ")
        self.adjective = input("Enter an adjective: ")
        
    def readFileIntoWordList(self, filename):
        """ reads a text file and returns a list of words with punctuation removed """
   
        file = open(filename)       # opens the filename
        words = []                  # creates an empty line
    
        for line in file:               # for each line
            line = line[:-1]            # cuts off the endline
            words += line.split(' ')        # splits each line at the space
        
        return words
        
        
        file.close()
<<<<<<< HEAD
        
=======
# this is a test
# explitive yes
>>>>>>> 31819c880302dc6a8792b060c5fd75093e528eba
        
if __name__ == '__main__' :
    w = words()
    print(w.wordlist)
#        
#class story(words):
#    """ uses inputs from words class and adds it to the story
#    making a new story """
#    def __init_(self):
#        
<<<<<<< HEAD
#        
=======
#        
>>>>>>> 31819c880302dc6a8792b060c5fd75093e528eba
