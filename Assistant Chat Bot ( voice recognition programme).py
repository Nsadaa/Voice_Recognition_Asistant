import pyttsx3
import speech_recognition as sr
from time import ctime ,sleep
import webbrowser
import random
import requests


def voice(play_voice):
    engine = pyttsx3.init()

    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)

    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate - 60)

    engine.say(play_voice)
    engine.runAndWait()


def get_voice():

    global voice_data
    voice_data = ""

    while True:
        r = sr.Recognizer()
        with sr.Microphone() as source:

            try:
                audio = r.listen(source)
                voice_data = r.recognize_google(audio)
                sleep(1)
                break

            except:
                continue


def get_voice_2():

    global voice_data2
    voice_data2 = ""

    while True:
        r_2 = sr.Recognizer()
        with sr.Microphone() as source:
            try:
                audio = r_2.listen(source)
                voice_data2 = r_2.recognize_google(audio)
                sleep(1)
                break
            except:

                break


def greeting():
    g_messages = ["hi there.","hey sadaruwan.","yeah im here.","How can I help you sadaruwan","yes im here."]
    r_message = random.choice(g_messages)
    voice(r_message)

def thanking():
    th_messages = ["you are welcome.","its pleasure to being with you.","Never mind its my job"]
    r_th_message = random.choice(th_messages)
    voice(r_th_message)


def get_ip_info():

    global internet_status
    internet_status = False

    try:
        r = requests.get('https://get.geojs.io/')
        ip_req = requests.get('https://get.geojs.io/v1/ip.json')
        ip_add = ip_req.json()['ip']
        # print(ip_add)

        url = 'https://get.geojs.io/v1/ip/geo/' + ip_add + '.json'
        geo_req = requests.get(url)
        geo_data = geo_req.json()

        global get_city , get_region , get_country

        get_city = str((geo_data['city']))
        get_region = str((geo_data['region']))
        get_country = str((geo_data['country']))

        internet_status = True

    except:
        internet_status = False


def analyse_voice():

    get_ip_info()

    if internet_status == False:
        voice("Check Your Internet Connection !")
        exit()

    else:

        voice("im Alexa How Can I Help You ?")
        joke_count = 0
        answer_count = 0

        while True:

            if answer_count >= 5:
                joke_count = 0
                answer_count = 0

            else:
                pass

            get_voice()
            words = ["time","location","city","country","hi","hey","bye","thanks",
                     "search","town","do","old","joke","ok","okay","thank","great","wow",
                     "name","yoo","yo","tired","sleep","sleepy","cool","region"]
            x = str(voice_data)
            z = x.split()
            avl_words = 0

            for y in z:
                if y.lower() in words:
                    avl_words += 1

            if avl_words == 0:
                print(x)
                voice("Did Not Get you.")
                continue

            elif avl_words >= 2:
                voice("Cant Identify What You Actually Need ! speak again.")
                continue

            else:
                if "Bye" in z:
                    voice("Good Bye Sadaruwan.")
                    break

                else:
                    for i in z:
                        if i.lower() in words :

                            if  joke_count >= 1:
                                answer_count += 1

                            else:
                                pass

                            if i.lower() =="time":
                                now_time = "Now Time Is " + ctime()
                                converted_now_time = str(now_time)
                                voice(converted_now_time)
                                break

                            elif i.lower()=="town":
                                voice("Location is moratuwa.")
                                break

                            elif i=="city":
                                your_city = 'Your city Is,' + get_city + '.'
                                voice(your_city)
                                break

                            elif i.lower()=="hi" or i.lower()=="yoo" or i.lower()=="yo" or i.lower()=="hey":
                                greeting()
                                break

                            elif i.lower()=="thanks" or i.lower()=="thank":
                                thanking()
                                break

                            elif i.lower()=="search":
                                voice("What Do You Want To search.")
                                get_voice_2()

                                if voice_data2 == "":
                                    voice("Did Not Able To Find.")
                                    break
                                else:

                                    google_url = 'https://google.com/search?q=' + voice_data2
                                    webbrowser.get().open(google_url)
                                    voice("here what i got.")
                                    voice_data2 = ""
                                    break
                                    sleep(1.5)


                            elif i.lower()=="location":
                                voice("Where Do You Want To search.")
                                get_voice_2()

                                if voice_data2 == "":
                                    voice("Did Not Able To Find.")
                                    break
                                else:
                                    location_url = 'https://google.nl/maps/place/' + voice_data2 + '/&amp'
                                    webbrowser.get().open(location_url)
                                    voice("here what i got.")

                                    sleep(1.5)
                                    voice_data2 = ""
                                    break


                            elif i.lower()=="country":
                                your_country = 'Your country Is ,' + get_country + '.'
                                voice(your_country)
                                break

                            elif i.lower()=="region":
                                your_region = 'Your region Is ,' + get_region + '.'
                                voice(your_region)
                                break

                            elif i.lower()=="old":

                                voice("I have no idea about that. ask from the inventer.")
                                break

                            elif i.lower()=="do":

                                voice("I can do several thing for you as for now. in near future i will be upgraded with more. for now i can search what ever you want from google , find loactions , time , city , country & make you mood good Thats all.")
                                break

                            elif i.lower()=="joke":

                                if joke_count == 0:
                                    voice("imagine, that how there is no internet connection in the world")
                                    joke_count += 1

                                else:
                                    voice("Im fed up with telling stories to you. so plz.")
                                break


                            elif i.lower()=="ok" or i.lower()=="okay":

                                voice("Sounds Good.")
                                break

                            elif i.lower()=="wow" or i.lower()=="great" or i.lower()=="cool":

                                voice("Its awesome being able to help.")
                                break

                            elif i.lower()=="name":

                                voice("my name is alexa.")
                                break

                            elif i.lower()=="tired":

                                voice("okay sadaruwan take a rest.")
                                break

                            elif i.lower()=="sleep" or i.lower()=="sleepy":

                                voice("okay sadaruwan go to the bed.")
                                break

                        else:
                            continue


analyse_voice()
