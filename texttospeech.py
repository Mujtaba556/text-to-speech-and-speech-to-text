from tkinter import *
from tkinter.messagebox import showinfo
from gtts import gTTS
import speech_recognition as sr
import os

mainwindow= Tk() # Create the main window tk is a class in tkinter and Tk is a constructor of that class 
mainwindow.title('Text-To-Speech and Speech-To-Text Converter')
mainwindow.geometry('500x500') # Set the size of the window
mainwindow.resizable(0, 0) 
mainwindow.configure(bg='yellow')

def say(text1): # Function to convert text to speech and playback the audio
     language = 'en'
     speech = gTTS(text = text1, lang = language, slow = False)
     speech.save("text.mp3") # Save the audio file as text.mp3
     os.system("start text.mp3") # Play the audio file using the default media player


def recordvoice(): # Function to record voice and convert it to text
    r = sr.Recognizer() # Create a recognizer object to recognize speech (class)
    with sr.Microphone() as source: # Use the microphone as the source of audio input
        audio = r.listen(source) # Listen for the audio input from the microphone
        try:    
            text = r.recognize_google(audio, language="en-IN") # Recognize the speech using Google Web Speech API
        except sr.UnknownValueError: # Handle the case where the speech is not recognized
            text = "Sorry, I couldn't understand your speech." 
        except sr.RequestError: # Handle the case where the request to the Google Web Speech API fails
            text = "Could not request results; check your internet."
    
    return text  # Return the recognized text

def TextToSpeech(): # Function to create the Text-to-Speech  new window
    texttospeechwindow = Toplevel(mainwindow) # Create a new window for Text-to-Speech conversion
    texttospeechwindow.title('Text-to-Speech Converter')
    texttospeechwindow.geometry("500x500")
    texttospeechwindow.configure(bg='Blue')

    Label(texttospeechwindow, text='Text-to-Speech Converter', font=("Times New Roman", 15), bg='Blue').place(x=50)

    text = Text(texttospeechwindow, height=5, width=30, font=12)
    text.place(x=7, y=60)
    
    speakbutton = Button(texttospeechwindow, text='listen', bg='coral', command=lambda: say(str(text.get(1.0, END))))
    speakbutton.place(x=140, y=200)

def SpeechToText(): # Function to create the Speech-to-Text new window
    speechtotextwindow = Toplevel(mainwindow) 
    speechtotextwindow.title('Speech-to-Text Converter')
    speechtotextwindow.geometry("500x500")
    speechtotextwindow.configure(bg='pink')

    Label(speechtotextwindow, text='Speech-to-Text Converter', font=("Comic Sans MS", 15), bg='IndianRed').place(x=50)

    text = Text(speechtotextwindow, font=12, height=3, width=30)
    text.place(x=7, y=100)
    
    recordbutton = Button(speechtotextwindow, text='Record', bg='Sienna', command=lambda: text.insert(END, recordvoice()))
    recordbutton.place(x=140, y=50)

Label(mainwindow, text='Text-To-Speech and Speech-To-Text Converter',
     font=('Times New Roman', 16), bg='red', wrap=True, wraplength=450).place(x=25, y=0)

texttospeechbutton = Button(mainwindow, text='Text-To-Speech Conversion', font=('Times New Roman', 16), bg='Purple', command=TextToSpeech)
texttospeechbutton.place(x=100, y=150)

speechtotextbutton = Button(mainwindow, text='Speech-To-Text Conversion', font=('Times New Roman', 16), bg='Purple', command=SpeechToText)
speechtotextbutton.place(x=100, y=250)

mainwindow.update() # Update the main window to reflect any changes made to it
mainwindow.mainloop() # Start the main event loop to keep the window open and responsive to user interactions
