
from tkinter import *
from outputs import *
from PIL import ImageTk, Image
import functions
import pyttsx3
import os



class View:
    def __init__(self, root, model):

        #robotic voice initialisation
        self.TTS = pyttsx3.init()
        self.VOICES = self.TTS.getProperty('voices')
        self.TTS.setProperty('voice', self.VOICES[0].id)
        self.range = 0
        self.first_el = 0
        self.last_el = 0
        self.key = 0

        self.root = root

        self.frametop = Frame(root, background="orange")
        self.frametop.pack(side=TOP, fill=BOTH, expand=1)

        self.framebtm = Frame(root, background="orange")
        self.framebtm.pack(side=BOTTOM, fill=BOTH, expand=1)

        self.lbl_output = Label(self.frametop, text=outputs[0], fg="white", font = "Verdana 20 bold", background="orange")
        self.lbl_output.pack(side=LEFT, pady = 20, padx = 20)


        #base_folder = os.path.dirname(__file__)
        #image_path = os.path.join(base_folder, 'pictures\dio.png')
        #photo = PhotoImage(file=image_path)

        img_voice = ImageTk.PhotoImage(Image.open("pictures\dio.png"))
        self.lbl_voice = Label(self.frametop, image = img_voice)
        #http://effbot.org/pyfaq/why-do-my-tkinter-images-not-appear.htm
        self.lbl_voice.image = img_voice
        self.lbl_voice.bind('<Button-1>', self.tell_me)
        self.lbl_voice.pack(side=RIGHT, pady = 20, padx = 20)

        img = ImageTk.PhotoImage(Image.open("pictures\game_over.png"))
        self.lbl_image = Label(self.framebtm, image = img)
        #http://effbot.org/pyfaq/why-do-my-tkinter-images-not-appear.htm
        self.lbl_image.image = img

        imgWin = ImageTk.PhotoImage(Image.open("pictures\you_win.jpg"))
        self.lbl_imageWin = Label(self.framebtm, image = imgWin)
        #http://effbot.org/pyfaq/why-do-my-tkinter-images-not-appear.htm
        self.lbl_imageWin.image = imgWin

        img10 = ImageTk.PhotoImage(Image.open("pictures\i_10.png"))
        self.btn_to10 = Button(self.framebtm, text="10", image=img10, padx=20, pady=20, command=lambda : functions.setRange(self, 10))
        self.btn_to10.image=img10
        self.btn_to10.bind('<Button-1>', self.hide_me)
        #btn_to10.bind("<Button-1>", handle_click)
        self.btn_to10.pack(side= LEFT)

        img20 = ImageTk.PhotoImage(Image.open("pictures\i_20.png"))
        self.btn_to20 = Button(self.framebtm, text="20", image=img20, padx=20, pady=20, command=lambda : functions.setRange(self, 20))
        self.btn_to20.image=img20
        self.btn_to20.bind('<Button-1>', self.hide_me)
        self.btn_to20.pack(side=LEFT)

        img50 = ImageTk.PhotoImage(Image.open("pictures\i_50.png"))
        self.btn_to50 = Button(self.framebtm, text="50", image=img50, padx=20, pady=20, command=lambda : functions.setRange(self, 50))
        self.btn_to50.image=img50
        self.btn_to50.bind('<Button-1>', self.hide_me)
        self.btn_to50.pack(side=LEFT)

        img100 = ImageTk.PhotoImage(Image.open("pictures\i_100.png"))
        self.btn_to100 = Button(self.framebtm, text="100", image=img100, padx=20, pady=20, command=lambda : functions.setRange(self, 100))
        self.btn_to100.image=img100
        self.btn_to100.bind('<Button-1>', self.hide_me)
        self.btn_to100.pack(side=LEFT)

        imgYes = ImageTk.PhotoImage(Image.open("pictures\_yes.png"))
        self.btn_yes = Button(self.framebtm, text="YES", image=imgYes, padx=20, pady=20)
        self.btn_yes.image=imgYes
        self.btn_yes.bind('<Button-1>', self.action1)

        imgNo = ImageTk.PhotoImage(Image.open("pictures\_no.png"))
        self.btn_no = Button(self.framebtm, text="NO", image=imgNo, padx=20, pady=20)
        self.btn_no.image=imgNo
        self.btn_no.bind('<Button-1>', self.action1)

    def tell_me(self, event):
        self.TTS.say(self.lbl_output.cget('text'))
        self.TTS.runAndWait()

    def action1(self, event):
        functions.action1(self, event)

    def action3(self, event, key):
        functions.action3(self, event, key)

    def action2(self, event, key):
        functions.action2(self, event, key)

    def hide_me(self, event):
        functions.hide_me(self, event)

    def run(self):
        self.root.mainloop()
