import kivy
from kivy.core.audio import SoundLoader
import tkinter
import pygame
import sys
from tkinter import *
pygame.init()

class hitam:
    def __init__(self,master):
        self.master=master
        topframe = Frame(root)
        topframe.pack(side=TOP)
        root.title("")
        self.button=Button(topframe, padx=8, height=6, pady=8, bd=8, text="01", bg="black", fg="white", command=self.value_Cs).pack(side=LEFT)
        self.button22 = Button(topframe, state=DISABLED, height=7, width=1, padx=0, pady=0, relief=RIDGE).pack(side=LEFT)
        self.button2 = Button(topframe, padx=8, pady=8, height=6, bd=8, text="02", bg="black", fg="white", command=self.value_Ds).pack(side=LEFT)
        self.button22 = Button(topframe, state=DISABLED, height=7, width=4, padx=0, pady=0, relief=RIDGE).pack(side=LEFT)
        self.button3 = Button(topframe, padx=8, pady=8, height=6, bd=8, text="03", bg="black", fg="white", command=self.value_Fs).pack(side=LEFT)
        self.button22 = Button(topframe, state=DISABLED, height=7, width=1, padx=0, pady=0, relief=RIDGE).pack(side=LEFT)
        self.button4 = Button(topframe, padx=8, pady=8, height=6, bd=8, text="04", bg="black", fg="white", command=self.value_Gs).pack(side=LEFT)
        self.button22 = Button(topframe, state=DISABLED, height=7, width=1, padx=0, pady=0, relief=RIDGE).pack(side=LEFT)

        self.button2 = Button(topframe, padx=8, pady=8, height=6, bd=8, text="05", bg="black", fg="white", command=self.value_Bb).pack(side=LEFT)
        self.button22 = Button(topframe, state=DISABLED, height=7, width=4, padx=0, pady=0, relief=RIDGE).pack(side=LEFT)
        self.button3 = Button(topframe, padx=8, pady=8, height=6, bd=8, text="06", bg="black", fg="white",command=self.value_Cs1).pack(side=LEFT)
        self.button22 = Button(topframe, state=DISABLED, height=7, width=1, padx=0, pady=0, relief=RIDGE).pack(side=LEFT)
        self.button4 = Button(topframe, padx=8, pady=8, height=6, bd=8, text="07", bg="black", fg="white",command=self.value_Ds1).pack(side=LEFT)

    def value_Cs(self):
        pygame.mixer_music.load("Music_Notes/D_s.wav")
        pygame.mixer_music.play()

    def value_Ds(self):
        sound = pygame.mixer.Sound("Music_Notes/D_s.wav")
        sound.play()

    def value_Fs(self):
        sound = pygame.mixer.Sound("Music_Notes/F_s.wav")
        sound.play()

    def value_Gs(self):
        sound = pygame.mixer.Sound("Music_Notes/G_s.wav")
        sound.play()

    def value_Bb(self):
        sound = pygame.mixer.Sound("Music_Notes/Bb.wav")
        sound.play()

    def value_Cs1(self):
        sound = pygame.mixer.Sound("Music_Notes/C_s1.wav")
        sound.play()

    def value_Ds1(self):
        sound = pygame.mixer.Sound("Music_Notes/D_s1.wav")
        sound.play()
class putih:
    def __init__(self,master):
        self.master=master
        frame1 = Frame(root)
        frame1.pack(side=TOP)

        self.button1 = Button(frame1, padx=16, pady=16, bd=8, height=8, text="1", fg="black", command=self.value_C).pack(
            side=LEFT)
        self.button2 = Button(frame1, padx=16, pady=16, bd=8, height=8, text="2", fg="black", command=self.value_D).pack(
            side=LEFT)
        self.button3 = Button(frame1, padx=16, pady=16, bd=8, height=8, text="3", fg="black", command=self.value_E).pack(
            side=LEFT)
        self.button4 = Button(frame1, padx=16, pady=16, bd=8, height=8, text="4", fg="black", command=self.value_F).pack(
            side=LEFT)

        self.button5 = Button(frame1, padx=16, pady=16, bd=8, height=8, text="5", fg="black", command=self.value_G).pack(
            side=LEFT)
        self.button6 = Button(frame1, padx=16, pady=16, bd=8, height=8, text="6", fg="black", command=self.value_A).pack(
            side=LEFT)
        self.button7 = Button(frame1, padx=16, pady=16, bd=8, height=8, text="7", fg="black", command=self.value_B).pack(
            side=LEFT)
        self.button8 = Button(frame1, padx=16, pady=16, bd=8, height=8, text="8", fg="black", command=self.value_C1).pack(
            side=LEFT)

        self.button9 = Button(frame1, padx=16, pady=16, bd=8, height=8, text="9", fg="black", command=self.value_D1).pack(
            side=LEFT)
        self.button10 = Button(frame1, padx=16, pady=16, bd=8, height=8, text="10", fg="black", command=self.value_E1).pack(
            side=LEFT)
        self.button11 = Button(frame1, padx=16, pady=16, bd=8, height=8, text="11", fg="black", command=self.value_F1).pack(
            side=LEFT)

    def value_C(self):
        sound = pygame.mixer.Sound("Music_Notes/C.wav")
        sound.play()

    def value_D(self):
        sound = pygame.mixer.Sound("Music_Notes/D.wav")
        sound.play()

    def value_E(self):
        sound = pygame.mixer.Sound("Music_Notes/E.wav")
        sound.play()

    def value_F(self):
        sound = pygame.mixer.Sound("Music_Notes/F.wav")
        sound.play()

    def value_G(self):
        sound = pygame.mixer.Sound("Music_Notes/G.wav")
        sound.play()

    def value_A(self):
        sound = pygame.mixer.Sound("Music_Notes/A.wav")
        sound.play()

    def value_B(self):
        sound = pygame.mixer.Sound("Music_Notes/B.wav")
        sound.play()

    def value_C1(self):
        sound = pygame.mixer.Sound("Music_Notes/C1.wav")
        sound.play()

    def value_D1(self):
        sound = pygame.mixer.Sound("Music_Notes/D1.wav")
        sound.play()

    def value_E1(self):
        sound = pygame.mixer.Sound("Music_Notes/E1.wav")
        sound.play()

    def value_F1(self):
        sound = pygame.mixer.Sound("Music_Notes/F1.wav")
        sound.play()


root=Tk()
obj=hitam(root)
obj1=putih(root)
root.mainloop()