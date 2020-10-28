# generate random integer values
from random import randint
from outputs import *
from tkinter import *


def guess_value(i, j):
    value = randint(i, j)
    return(value)



def tell_user(self, string):
    self.lbl_output['text']=string

def game_over(self, event):
    self.lbl_image.pack(fill = "both", expand = "yes")
    self.btn_no.pack_forget()
    self.btn_yes.pack_forget()
    self.frametop.pack_forget()

def setRange(self, r):
    self.range=int(r)
    self.last_el=self.range

def bind_action3(self, event, key):
    self.btn_yes.bind('<Button-1>', lambda event, key=self.key: self.action3(event, key))
    self.btn_no.bind('<Button-1>', lambda event, key=self.key: self.action3(event, key))

def hide_YN(self):
    self.btn_no.pack_forget()
    self.btn_yes.pack_forget()

def hide_me(self, event):
    setRange(self, event.widget.cget('text'))
    self.lbl_output['text']=outputs[1] + event.widget.cget('text') + outputs[2]
    hide_rangeButtons(self)
    self.btn_yes.pack(side=LEFT)
    self.btn_no.pack(side=LEFT)

def hide_rangeButtons(self):
    self.btn_to10.pack_forget()
    self.btn_to20.pack_forget()
    self.btn_to50.pack_forget()
    self.btn_to100.pack_forget()

def play_game(self):

    if self.first_el > self.last_el:
    #no more unchecked elements in the range
        tell_user(self, outputs[4])
        self.btn_no.pack_forget()
        self.btn_yes.pack_forget()
        self.lbl_image.pack(fill = "both", expand = "yes")
    else:
        self.key=guess_value(self.first_el, self.last_el);
        self.btn_yes.bind('<Button-1>', lambda event, key=self.key: self.action2(event, key))
        self.btn_no.bind('<Button-1>', lambda event, key=self.key: self.action2(event, key))
        tell_user(self, str(self.key) + outputs[6])
def action1(self, event):
    #user don't want to guess a number, don't want to cntinue the game
    if event.widget == self.btn_no:
        game_over(self, event)
    #user want to play
    elif event.widget == self.btn_yes:
        play_game(self)

def action2(self, event, key):
    if event.widget == self.btn_no:
        tell_user(self, outputs[7] + str(key) + outputs[6])
        bind_action3(self, event, key)

    elif event.widget == self.btn_yes:
        hide_YN(self)
        self.lbl_imageWin.pack(side = BOTTOM, fill = "both", expand = "yes")
        tell_user(self, outputs[8] + str(key))

def action3(self, event, key):
    if event.widget == self.btn_no:
        self.last_el = key-1
    elif event.widget == self.btn_yes:
        self.first_el = key+1
    play_game(self)
