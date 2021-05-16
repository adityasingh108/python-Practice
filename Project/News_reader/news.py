import json 
import requests


def Speak(str):
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.SpVoice")
    speak.Speak(str)
    
if __name__=="__main__":
    Speak('lets begin with Latest And  Intresting News....')
    url = "https://newsapi.org/v2/top-headlines?country=in&category=science&apiKey=2937c344ea0840f2a5f010932f078cad"
    json_file = requests.get(url).text
    news_dict = json.loads(json_file)
    arts = news_dict['articles']
    for news in arts:
        print(news["title"])
        Speak(news["title"])
        Speak("Reading more news")

