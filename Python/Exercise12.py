#Read the News
import requests
import time
import datetime
import speech_recognition as sr
import time

def speak(str):
    from win32com.client import Dispatch
    speak = Dispatch('SAPI.SpVoice')
    speak.Speak(str)

time = int(datetime.datetime.now().hour)
businessdata = requests.get('https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=ca45b92db24242bcb440a125fd0b86c6')
businessresult = businessdata.json()
print(businessresult['status'])
businessnews = businessresult['articles']

sportdata = requests.get('https://newsapi.org/v2/top-headlines?country=us&category=sports&apiKey=ca45b92db24242bcb440a125fd0b86c6')
sportresult = sportdata.json()
sportnews = sportresult['articles']

techdata = requests.get('https://newsapi.org/v2/top-headlines?country=us&category=technology&apiKey=ca45b92db24242bcb440a125fd0b86c6')
techresult = techdata.json()
technews = techresult['articles']

entertainmentdata = requests.get('https://newsapi.org/v2/top-headlines?country=us&category=entertainment&apiKey=ca45b92db24242bcb440a125fd0b86c6')
entertainmentresult = entertainmentdata.json()
entertainmentnews = entertainmentresult['articles']

politicdata = requests.get('https://newsapi.org/v2/top-headlines?country=us&category=politics&apiKey=ca45b92db24242bcb440a125fd0b86c6')
politicresult = politicdata.json()
politicnews = politicresult['articles']

healthdata = requests.get('https://newsapi.org/v2/top-headlines?country=us&category=health&apiKey=ca45b92db24242bcb440a125fd0b86c6')
healthresult = healthdata.json()
healthnews = healthresult['articles']

sciencedata = requests.get('https://newsapi.org/v2/top-headlines?country=us&category=science&apiKey=ca45b92db24242bcb440a125fd0b86c6')
scienceresult = sciencedata.json()
sciencenews = scienceresult['articles']

def greet():
    if time>0 and time<12:
        speak('Good Morning')
    elif time>12 and time<18:
        speak('Good Afternoon')
    else:
        speak('Good Evening')
greet()

speak('Here\'s a list of news')
print('List of news: \n1.Business \n2.Sports \n3.Technology \n4.Entertainment \n4.Political \n5.Health \n6.Science')
speak('Hit enter to speak')
input()
def takeCommand():
        r = sr.Recognizer()
        
        with sr.Microphone() as source:
            print("Listening...")
            r.adjust_for_ambient_noise(source, duration = 1)
            audio = r.listen(source)
        try:
            print("Recognizing...")    
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")
        except Exception as e:
            print(e)
            speak('Sorry I didn\'t get that')
            return 'None'
        if 'business' in query:
            speak('Some latest business news are:')
            for i in range(1,10):
                print(i)
                print(businessnews[i]['description'])
                speak(businessnews[i]['description'])
                if i>=9:
                    break
                elif i==8:
                    speak('Last news is')
                elif i<8 and i>0:
                    speak('Moving to our next news')

        elif 'sports' in query:
            speak('Some latest sport news are:')
            for i in range(1,10):
                print(i)
                print(sportnews[i]['description'])
                speak(sportnews[i]['description'])
                if i>=9:
                    break
                elif i==8:
                    speak('Last news is')
                elif i<8 and i>0:
                    speak('Moving to our next news')
        
        elif 'technology' in query:
            speak('Some latest tech news are:')
            for i in range(1,10):
                print(i)
                print(technews[i]['description'])
                speak(technews[i]['description'])
                if i>=9:
                    break
                elif i==8:
                    speak('Last news is')
                elif i<8 and i>0:
                    speak('Moving to our next news')
            
        elif 'entertainment' in query:
            speak('Some latest entertainment news are:')
            for i in range(1,10):
                print(i)
                print(entertainmentnews[i]['description'])
                speak(entertainmentnews[i]['description'])
                if i>=9:
                    break
                elif i==8:
                    speak('Last news is')
                elif i<8 and i>0:
                    speak('Moving to our next news')
        
        elif 'political' in query:
            speak('Some latest political news are:')
            for i in range(1,10):
                print(i)
                print(politicnews[i]['description'])
                speak(politicnews[i]['description'])
                if i>=9:
                    break
                elif i==8:
                    speak('Last news is')
                elif i<8 and i>0:
                    speak('Moving to our next news')

        elif 'health' in query:
            speak('Some latest health news are:')
            for i in range(1,10):
                print(i)
                print(healthnews[i]['description'])
                speak(healthnews[i]['description'])
                if i>=9:
                    break
                elif i==8:
                    speak('Last news is')
                elif i<8 and i>0:
                    speak('Moving to our next news')

        elif 'science' in query:
            speak('Some latest science news are:')
            for i in range(1,10):
                print(i)
                print(sciencenews[i]['description'])
                speak(sciencenews[i]['description'])
                if i>=9:
                    break
                elif i==8:
                    speak('Last news is')
                elif i<8 and i>0:
                    speak('Moving to our next news')
        
        return query

takeCommand()
