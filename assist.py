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


engine =pyttsx3.init()
voices =engine.getProperty('voices')
engine.setProperty('voice',voices[-1].id)

def speak(audio):
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

if __name__ == "__main__":
  # speak("Hello Boss")
    wishme()
    print('type help for queris')
    # query=str(input( "enter query"))#to manualy enter query
    while True:#In below code say somthing what do you want to open or get activity from friday and say stop to end process
#        query=str(input( "enter query: "))#to manualy enter query
        query =listen().lower()#to enter query with speach
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
        #Commands on os modules
        elif 'play video' in query:
                music_dir= 'C:\\Users\\Amol\\Desktop'
                video = os.listdir(music_dir)
                print(video)
                os.startfile(os.path.join(music_dir,video[22]))
        elif 'stop music' in query:
                music_dir= 'C:\\Users\\Amol\\Desktop'
                songs = os.listdir(music_dir)
                print(songs)
                os.close(os.path.join(music_dir,songs[0,])) 
        elif 'moonknight one' in query:
            dir='C:\\Users\\Amol\\Desktop\\moonknight'
            list=os.listdir(dir)
            print(list)
            os.startfile(os.path.join(dir,list[0]))
        elif 'moonknight two' in query:
            dir='C:\\Users\\Amol\\Desktop\\moonknight'
            list=os.listdir(dir)
            print(list)
            os.startfile(os.path.join(dir,list[1]))
        elif 'open' in query:
                v='/home/q/Desktop/'
                list=os.listdir(v)
                os.startfile(os.path.join(v,list[1]))     
        elif 'I want to watch movies' in query:
            dir='C:\\Users\\Amol\\Desktop\\movies'
            list=os.listdir(dir)
            print(list)

            

        # os.startfile(os.path.join(dir,list[]))

        elif 'time' in query:
                strtime= datetime.datetime.now().strftime("%H:%M:%S")
                # print(strtime)
                speak(f"The time is {strtime}")
                # time.sleep(2)
                # print(f"The time is {strtime}")

        # elif 'email' in query:
        #         try:
        #             speak("what shoould I say?")
        #             content= listen()
        #             to= "amolbran0@gmail.com"
        #             sendEmail(to,content)
        #             speak("Email successfully send!")
        #         except Exception as e:
        #             print(e)
        #             speak("sorry boss, i am not able to send email")
        elif 'youtube' in query:
                speak('starting')
                time.sleep(3)
                webbrowser.open('https://youtu.be/iik25wqIuFo')

        elif 'help' in query:
            speak('here are some query you can use')
            print('''
                who are you : for the intoduction of AI
                youtube : to start youtube in web browser
                time : to check current time 
                wikipedia <topic to search from wiki>: to search wikipedia
                quit : to terminate program''')

        # elif 'file' in query:
        #         v='C:\\'
        #         os.startfile(v)      

        elif'who are you' in query:
                speak('I am veronica, i am A.i system of created by self,with love of you, i m a ho,such a disspointment to this dammed world') 
        

        elif 'quit' in query:
            speak('have a great day')
            # time.sleep(2)
            # print('***have a great day***')
            break;

        else:
            speak("please give appropriate query")
                
                          
   
