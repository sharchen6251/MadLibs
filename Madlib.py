#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  7 16:48:42 2019

@author: sharchen
"""
import tkinter as tk
from tkinter import *

class Madlib:
    """ methods for collecting the inputs from the user """
    def __init__(self, filename):
        """ initializes the stories """
        self.story = filename
        self.wordlist = self.readFileIntoWordList(self.story)
        self.dict = {}
        self.create_dictionary()
        self.master = Tk()
        self.master.title('Name')
        self.e = Entry(self.master)
        self.e.pack()
        self.e.focus_set()
        
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
                self.master.title('Enter Noun')
                b = Button(self.master, text='okay', command = lambda:[self.get_val(k), b.destroy()])
                b.pack(side='bottom')
#                self.master.mainloop()
                
            if self.dict[k] == 'number':                  # if the value is noun
                self.master.title('Enter Number')
                b = Button(self.master, text='okay', command = lambda:[self.get_val(k), b.destroy()])
                b.pack(side='bottom')
                self.master.mainloop()
                
            if self.dict[k] == 'verb':                  # if the value is noun
                self.master.title('Enter Verb')
                b = Button(self.master, text='okay', command = lambda:[self.get_val(k), b.destroy()])
                b.pack(side='bottom')
                self.master.mainloop()
                
            if self.dict[k] == 'adjective':                  # if the value is noun
                self.master.title('Enter Adjective')
                b = Button(self.master, text='okay', command = lambda:[self.get_val(k), b.destroy()])
                b.pack(side='bottom')
                self.master.mainloop()
                
            if self.dict[k] == 'place':                  # if the value is noun
                self.master.title('Enter Place')
                b = Button(self.master, text='okay', command = lambda:[self.get_val(k), b.destroy()])
                b.pack(side='bottom')
                self.master.mainloop()
#                
#            elif self.dict[k] == 'number':                  # if the value is number
#                self.dict[k] = input("Enter a number: ")    # the value changes to the inputted number
#                
#            elif self.dict[k] == 'verb':                    # if the value is a verb
#                self.dict[k] = input("Enter a verb: ")      # the value changes to the inputted verb
#            
#            elif self.dict[k] == 'adjective':               # if the value is an adjective
#                self.dict[k] = input("Enter an adjective: ")    # the value changes to the inputted adjective
#            
#            elif self.dict[k] == 'place':
#                self.dict[k] = input("Enter a place: ")
        self.master.destroy()
        self.finshStory()

    def get_val(self, k):
        """ takes self and k """
        self.dict[k] = self.e.get()
        self.e = Entry(self.master)
        
    def get_story(self):
        """ prints the story on the screen """
        
        return self.wordlist
    
    def finshStory(self):
        """finshes story"""
        blank_count = 0
        for i in range(len(self.wordlist)):
            if self.wordlist[i][0] == '[':
                blank_count += 1
                self.wordlist[i] = self.dict[str(blank_count)]
            
                
        
if __name__ == '__main__' :
    w = Madlib('wedding.txt')
    w.replace_words()
    
#    print(w.wordlist)
    print(w.get_story())
    
     

