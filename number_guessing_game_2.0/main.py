from tkinter import *
from tkinter import messagebox
from random import randint
import pygame

pygame.mixer.init()

def play_sound(n):
    pygame.mixer.music.load(n)
    pygame.mixer.music.play()
def close():
      messagebox.showinfo(title='RULE',message='''Choose a difficulty level
                                      \nEasy: Guess between 1-50 (10 attempts).
                                      \nMedium: Guess between 1-100 (8 attempts).
                                      \nHard: Guess between 1-500 (10 attempts).
                                      \nEnter a number and click GUESS.
                                      \nIf your guess is greater than the secret number → Too High.
                                      \nIf your guess is smaller than the secret number → Too Low.
                                      \nEach wrong guess reduces your remaining attempts.
                                      \nGuess the correct number before attempts run out to win.
                                      \nScore depends on remaining attempts.
                                      \nHighest score is saved as Best Score.
                                      \nIf attempts reach 0, the game is over.''')
def difficulty():
    global computer,x,a
    if diff.get()==1:
        a=10
        x=50
    elif diff.get()==2:
        a=7
        x=100
    elif diff.get()==3:
        a=5
        x=500
    computer=randint(1,x)
    attempts['text']=f'ATTEMPTS LEFT\n{a}'


def youscore(n):
    global sco
    if diff.get()==1:
     sco=a*10
    elif diff.get()==2:
        sco=a*40
    elif diff.get()==3:
        sco=a*90
    score['text']=f'score\n{sco}'

def hiscore(n):
    global hi
    if n==0:
         with open('Best_score.txt','a') as f:
           f.write('')
         with open('Best_score.txt') as f:
                    hi= f.read()
                    if hi=='':
                     hi=0
                    #    with open('Best_score.txt','w') as f:
                    #      f.write(str(sco))
                    #      Bestscore['text']=f'Best score\n{sco}'  
                    if int(hi)<sco :
                       with open('Best_score.txt','w') as f:
                         f.write(str(sco))
                         Bestscore['text']=f'Best score\n{sco}'
    else:
          with open('Best_score.txt','a') as f:
           f.write('')
          with open('Best_score.txt') as f:
                    hi= f.read()
         
          if hi=='':
                     hi=0
                    #  Bestscore['text']=f'Best score\n{hi}'


def game():
    global a
    
    try:
             user=int(guess.get())
    except:
             messagebox.showerror(title='Invaild Input',message='Please Enter vaild digit')
    if not 1<=int(guess.get())<=x:
              messagebox.showerror(title='Invaild Input',message='Please Enter number in given range')
    elif diff.get() == 0:
              messagebox.showwarning("Difficulty","Please select a difficulty")
    if a>1:
         if int(guess.get())==computer:
                hint['fg']='#ffcb50'
                hint['text']=' YOU WIN'
                youscore(a)
                hiscore(0)
                play_sound('win.mp3')
         elif int(guess.get())>computer:
                hint['fg']='#f74c06'
                hint['text']='TO HIGH (Try lower please)'
                play_sound('alert.mp3')
         elif int(guess.get())<computer:
                hint['fg']="#10DF77"
                hint['text']='TO LOW (Try higher please)'
                play_sound('alert.mp3')
         a-=1
    else:
        a=0
        hint['text']=f'YOU LOOSE (Better luck next time)\nNO:{computer}'
        play_sound('loose.mp3')
    guess.delete(0,END)
    attempts['text']=f'ATTEMPTS LEFT\n{a}'
def reset():
    difficulty()
    hint['fg']='yellow'
    hint['text']='HINT'
    guess.delete(0,END)
    # computer=randint(1,x)

win=Tk()
    
win.title('Guess_The_number???')

win['bg']='#000328'
logo=PhotoImage(file=r"logo.png.png")
win.iconphoto(True,logo)

head=Label(win,text='Guess-The-Number???',fg='#fff708'
           ,bg='#000328',
           font=("Courier New",30,'bold','underline'))
head.pack()

level=Label(win,text='chose difficulty ',font=("arial",15,'bold',),fg='#b5c6e0',bg='#000328',)
level.pack(pady=20)

diff=IntVar()

r1=Radiobutton(win,text='Easy\n(1-50)\n10 tries',bg="#042B55",font=("arial",15,'bold',),width=10
               ,fg='#4a9e48',activebackground="#042B55",activeforeground='#4a9e48'
               ,variable=diff,value=1,command=difficulty, relief='ridge')
r1.place(x=70,y=100)
r2=Radiobutton(win,text='Medium\n(1-100)\n7 tries',bg="#042B55",font=("arial",15,'bold',),width=10
               ,fg="yellow",activebackground="#042B55",activeforeground='yellow',variable=diff
               ,value=2,command=difficulty, relief='ridge')
r2.place(x=220,y=100)
r3=Radiobutton(win,text='Hard\n(1-500)\n5 tries',bg="#042B55",font=("arial",15,'bold',),width=10
               ,fg='#cf203e',activebackground="#042B55",activeforeground='#cf203e',
               variable=diff,value=3,command=difficulty, relief='ridge')
r3.place(x=370,y=100)

enter=Label(win,text='Enter your guess ',font=("arial",15,'bold',),fg='#b5c6e0',bg='#000328',)
enter.place(x=220,y=200)

guess=Entry(win,font=("Tahoma",20,),width=20)
guess.place(x=70,y=250)

gbutton=Button(win,text='GUESS',font=("Tahoma",15,'bold'),bg='#f4d444',command=game,activebackground='#f4d444')
gbutton.place(x=430,y=250)

hint=Label(win,text='HINT',font=("Tahoma",20,),bg="#042B55",width=30,relief='groove',fg='yellow')
hint.place(x=70,y=320)

photo1=PhotoImage(file='t.png')
photo2=PhotoImage(file='trophy.png')
photo3=PhotoImage(file='chart.png')
attempts=Label(win,text='ATTEMPTS LEFT\n0',font=("Tahoma",17,'bold'),bg='#000328'
               ,fg='#e93a28',image=photo1,compound='top')
attempts.place(x=60,y=420)

score=Label(win,text='SCORE\n0',font=("Tahoma",17,'bold'),bg='#000328',fg='#ff930f',
            image=photo2,compound='top')
score.place(x=270,y=413)

hiscore(1)

Bestscore=Label(win,text=f'BEST SCORE\n{hi}',font=("Tahoma",17,'bold'),bg='#000328'
                ,fg='#d3eef4',image=photo3,compound='top')
Bestscore.place(x=390,y=395)
newgame=Button(win,text='↻  NEW GAME',font=("Tahoma",15,),bg='#46b83d',width=20,command=reset)
newgame.place(x=40,y=520)

rule=Button(win,text='➜] RULE',font=("Tahoma",15,),bg='#c5302e',width=20,command=close)
rule.place(x=330,y=520)

win.geometry('600x600')
win.mainloop()