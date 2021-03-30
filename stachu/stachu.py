import pyttsx3 #pip install
import datetime
import speech_recognition as sr #pip install sr
import wikipedia #pip install wiki

engine = pyttsx3.init()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time_():
    time=datetime.datetime.now().strftime('%I:%M:%S') #for 12 hour clock
    speak('The current time is')
    speak(time)

def date_(): #day month year by numbers
    year=datetime.datetime.now().year
    month=datetime.datetime.now().month
    day=datetime.datetime.now().day
    speak('The current date is')
    speak(day)
    speak(month)
    speak(year)

def wishme():
    speak("Welcome back Gruby!")
    time_()
    date_()

    #Greetings

    hour = datetime.datetime.now().hour

    if hour >=6 and hour<12:
        speak("Good Morning m8!")
    elif hour >=12 and hour<18:
        speak("Good Afternoon m8!")
    elif hour >=18 and hour<24:
        speak("Good Evening m8")
    else:
        speak("Go to sleep motherfucker!")

    speak("Stachu at your service. Tell me how I can help you?")

def take_command():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening....')
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print('Recognizing...')
        query =r.recognize_google(audio,language='pl-PL')
        print(query)

    except Exception as e:
        print(e)
        print('Say that again motherfucker...')
        return 'None'
    return query

if __name__ == '__main__':
    
    wishme()

    while True:
        query = take_command().lower()

        #all comands will be stored in lowercase letters in query
        #for easy recong

        if 'time' in query: #tells us time
            time_()

            
        elif 'date' in query: #tells us date
            date_()

        elif 'wikipedia' in query:
            speak('Searching...')
            query=query.replace('wikipedia','')
            result=wikipedia.summary(query, sentences=3)
            speak('According to Wikipedia')
            print(result)
            speak(result)


            
    
    
