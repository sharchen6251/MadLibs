#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  7 16:48:42 2019

@author: sharchen
"""

from tkinter import *

class Madlib:
    """ methods for collecting the inputs from the user """
    def __init__(self, filename):
        """ initializes the stories """
        self.story = filename
        self.wordlist = self.readFileIntoWordList(self.story)
        self.dict = {}
        
        
    def readFileIntoWordList(self, filename):
        """ reads a text file and returns a list of words with punctuation removed """
   
        file = open(filename)       # opens the filename
        words = []                  # creates an empty line
        
        for line in file:               # for each line
            line = line[:-1]            # cuts off the endline
            words += line.split(' ')        # splits each line at the space
        
     
        return words
        
        
        file.close()
        
    
    def create_dictionary(self):
        """ create the dictionary of blanks and inputted words """
        
        number_of_blanks = 0
        
        allwords = self.readFileIntoWordList(self.story)        # gets the story
        
        for word in allwords:               
            if word != '' and word[0] == '[':           # if it has a bracket 
                number_of_blanks += 1
                if word[-1] != ']':                 # if the last letter of the word is not the bracket
                    self.dict[str(number_of_blanks)] = word[1:-2]   # takes off the bracket and the punctuation
                else:                                               # if it doesn't end with a punctuation
                    self.dict[str(number_of_blanks)] = word[1:-1]    # takes off the bracket

    def replace_words(self):
        """ gets the input from the user to replace blanks """
        
        for k in self.dict.keys():                          # looks at all the keys
            if self.dict[k] == 'noun':                  # if the value is noun 
                self.dict[k] = input("Enter a noun: ")      # the value changes to the inputted noun
                
            elif self.dict[k] == 'number':                  # if the value is number
                self.dict[k] = input("Enter a number: ")    # the value changes to the inputted number
                
            elif self.dict[k] == 'verb':                    # if the value is a verb
                self.dict[k] = input("Enter a verb: ")      # the value changes to the inputted verb
            
            elif self.dict[k] == 'adjective':               # if the value is an adjective
                self.dict[k] = input("Enter an adjective: ")    # the value changes to the inputted adjective
            
            elif self.dict[k] == 'place':
                self.dict[k] = input("Enter a place: ")
        
        
    def get_story(self):
        """ prints the story on the screen """
        
        return self.wordlist
                    
    def finshStory(self):
        """finshes story"""
        allwords = self.readFileIntoWordList(self.story)        # gets the story
        return self.replace_words(allwords)
        
if __name__ == '__main__' :
    w = Madlib('wedding.txt')
    w.create_dictionary()
    w.replace_words()
    w.get_story()
    
#    print(w.wordlist)
    print(w.dict)
    
     

