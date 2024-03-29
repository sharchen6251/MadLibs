#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 15 00:20:14 2019

@author: josh
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 23:55:45 2019

@author: sharchen
"""

import tkinter as tk
from tkinter import *
from Madlib import Madlib

class Book():
    """ uses inputs from words class and adds it to the story
    making a new story """
    
    def __init__(self):
        """ initializes the values """
        self.input = open('input.txt')
        self.pages = [Madlib(file) for file in self.input]
        self.page = 0
        
        
    def get_pages(self):
        return self.pages
    
   
    def next_page():
        """ flips page forward """
        self.page += 1
        if self.page == len(self.pages):
            self.page = 0
   
    def last_page():
        """ flips page backward """
        self.page -= 1
        if self.page == -1:
            self.page = len(self.pages - 1)
        
    def get_page(self):
        """ finds out what page it is on """
        
        return self.pages[self.page]
        



if __name__ == '__main__' :
    ml_book = Book()
    pages = ml_book.get_pages()

    window = tk.Tk()                                                                    # creates the start window
    window.title('Madlib Book')
    start_button = tk.Button(window, text = 'Start', width = 25, command = window.destroy)
    start_button.pack()
    window.mainloop()
    
    master = Tk()
    master.title('Madlib Book')
    screen = Canvas(master, width = 1000, height = 1000)
    screen.pack()
    canvas_height = 200
    canvas_width = 2000
    y = int(canvas_height / 2)
    screen.create_line(0, y, canvas_width, y)
#    print(pages[self.page].get_story())
    
    message_var = Message(screen, text = ml_book.get_page().get_story(), width = 400)
    message_var.pack()
    
    frame = Frame(master)
    frame.pack()
    top_frame = Frame(master)
    top_frame.pack(side = TOP)
    play_button = Button(frame, text = 'Play', width = 25, command = ml_book.get_page().replace_words) # call replace words pages[ml_book.get_page()]
    play_button.pack(side = TOP)
    bottom_frame = Frame(master)
    bottom_frame.pack(side = BOTTOM)
    next_button = Button(frame, text = 'Next', fg = 'black', command = ml_book.next_page) # next page
    next_button.pack(side = RIGHT)
    back_button = Button(frame, text = 'Back', fg = 'black', command = ml_book.last_page) # last page
    back_button.pack(side = LEFT)
    master.mainloop()

    

    