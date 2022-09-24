from ast import While
import time
import pyttsx3
import speech_recognition as sr
import datetime
import pyaudio
import wikipedia
import webbrowser
import os
import smtplib
import googletrans
import tkinter as t

engine =pyttsx3.init()
voices =engine.getProperty('voices')
engine.setProperty('voice',voices[-1].id)

def dis_text(text):
    tex=t.Text(root,height=14,width=49)
    tex.insert(1.0,text)
    tex.tag_add('center',1.0,'end')
    tex.grid(columnspan=3,row=3)

def speak(audio):
    dis_text(audio)
    print(audio)
    engine.say(audio)
    engine.runAndWait()

def wishme(): #will greet you according to time of the day
    hour = int(datetime.datetime.now().hour)
    speak("hello sir ")    
    if hour>=0 and hour<12:         # if time is between 0 to 12 in the morning
        speak("Good Morning!")

    elif hour>=12 and hour<18:      #if time is between 12 to 6
        speak("Good Afternoon!")

    else:
         speak("Good Evining!")         
    speak("i am friday, how may i help you?")         

def listen():#it takes user input as audio of microphone and returns output as string variable 'query'
    
    k = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        k.pause_threshold == 1
        audio=k.listen(source)

    try:
        print("Recognizing......")
        speak("Recognizing......")
        query=k.recognize_google(audio, language='mar-in')    
        print("user said: ",{query},"\n")

    except Exception as e:
        print("Say that again please....")
        speak("Say that again please....")
        return "None"
    return query

def sendEmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('amolbrand00@gmail.com','amol@1234#')
    server.sendmail('amolbrand00@gmail.com',to,content)
    server.close()    

def exe(query):
    if 'wikipedia' in query:
                try:
                    speak('searching Wikipedia....')
                    query= query.replace("wikipedia","")
                    results = wikipedia.summary(query,sentences=1)
                    speak("Acording To Wikipedia")
                    speak(results)
                except Exception as e:
                    print(e)
                    speak("sorry boss ,i am not able get any appropriate result from wikipedia")
        
    elif 'time' in query:
                strtime= datetime.datetime.now().strftime("%H:%M:%S")
                # print(strtime)
                speak(f"The time is {strtime}")
                # time.sleep(2)
                # print(f"The time is {strtime}")

    elif 'youtube' in query:
                speak('starting')
                time.sleep(3)
                webbrowser.open('https://youtu.be/iik25wqIuFo')

    elif 'help' in query:
            speak('here are some query you can use')
            dis_text('''who are you : for the intoduction of AI \nyoutube : to start youtube in web browser \ntime : to check current time \nwikipedia : to search wikipedia \nquit : to terminate program''')  

    elif'who are you' in query:
                speak('I am veronica, i am A.i system of created by self,with love of you, i m a ho,such a disspointment to this dammed world') 


    elif 'quit' in query:
        speak('have a great day')
        

    else:
            speak("please give appropriate query")
                          
root=t.Tk()

t.Canvas(root,width=400,height=200).grid(columnspan=3)
name_var=t.StringVar()
query_box = t.Entry(root,textvariable = name_var, font=('calibre',10,'normal'),width=35)
query_box.grid(columnspan=3,row=1)

qury_button=t.Button(root,text='q',command=lambda:exe(query_box.get()),width=6,height=2)
qury_button.grid(column=1,row=2)
quit_button=t.Button(root,text='Quit',command=lambda:quit(),width=6,height=2)
quit_button.grid(column=2,row=0)
help_button=t.Button(root,text='help',command=lambda:exe('help'),width=6,height=2)
help_button.grid(column=0,row=0)
t.Canvas(root,width=400,height=200).grid(columnspan=3)
root.mainloop()
