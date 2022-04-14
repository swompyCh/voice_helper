from gtts import gTTS
import time
import playsound
# import speech_recognition as sr
import os
import webbrowser
import re
from pyowm import OWM
import pymorphy2
from googletrans import Translator
import random
from termcolor import colored
import string
from time import monotonic


def listen_command():
    # obtain audio from the microphone
    # r = sr.Recognizer()
    # with sr.Microphone() as source:
    # audio = r.listen(source)
    return input("Скажите вашу команду: ")
    # recognize speech using Google Speech Recognition
    # try:
    #     our_speech = r.recognize_google(audio, language="ru")
    #     print("Вы сказали: " + our_speech)
    #     return our_speech
    # except sr.UnknownValueError:
    #     return "ошибка"
    # except sr.RequestError:
    #     return "ошибка"


tbr = ('сколько', 'который', 'скажи', 'какая', 'случайное', 'рандомное')


# def execute_command(message):
#     for x in tbr:
#         message = message.replace(x, "").strip()
#     print(message)


def do_this_command(message):
    for x in tbr:
        message = message.replace(x, "").strip()

    message = message.lower()
    if message == 'привет':
        # say_message("Привет, друг!")
        print(colored("Привет, друг!", "blue"))

    elif message == 'пока':
        # say_message("Пока!")
        exit()

    elif "видео" in message:
        search = re.split(r'(видео)', message)
        print("Открываю!")
        url = "https://www.youtube.com/results?search_query=" + search[2]
        webbrowser.get().open(url)

    elif "погода в" in message or "погода" in message:
        owm = OWM('11ff33fc3dd037219c848889ae1657aa')

        print(colored("Ищу данные, подождите!", 'blue'))
        try:
            pogoda = re.split(r'(погода в )|(погода )', message)
            pogoda1 = pogoda[3]

            morph = pymorphy2.MorphAnalyzer()
            pogoda2 = morph.parse(pogoda1)[0]
            place = pogoda2.inflect({'nomn'}).word

            mgr = owm.weather_manager()
            observation = mgr.weather_at_place(place)
            w = observation.weather

            status = w.detailed_status
            temperature = w.temperature('celsius')["temp"]
            wind_speed = w.wind()["speed"]
            pressure = int(w.pressure["press"] / 1.333)

            print(colored("Погода в городе " + string.capwords(place) +
                          ":\n * Статус: " + status +
                          "\n * Скорость ветра (м/сек): " + str(wind_speed) +
                          "\n * Температура (цельсии): " + str(temperature) +
                          "\n * Атмосферное давление (мм рт.ст.): " + str(pressure), "blue"))
            # say_message("Сейчас {0} в городе {1}".format(status, place))
            # say_message("Температура {} по шкале цельсия".format(str(temperature)))
            # say_message("Скорость ветра {} метров в секунду".format(str(wind_speed)))
            # say_message("Атмосферное давление {} миллиметров ртутного столба".format(str(pressure)))
        except:
            print("Город не найден в базе данных")

    elif "переведи" in message or "перевести" in message:
        translator = Translator()
        result = re.split(r'(переведи)|(перевести)', message)
        result = result[3]
        if "на русский" in result:
            word = re.split(r'( на русский слово )|( на русский фразу )|( на русский предложение )|( на русский )', result)
            i = word[5]
            perevod = translator.translate(i, dest='ru')
            print(colored(perevod.text, 'blue'))
        elif "на английский" in result:
            word = re.split(r'( на английский слово )|( на английский фразу )|( на английский предложение )|( на английский)', result)
            i = word[5]
            perevod = translator.translate(i, dest='en')
            print(colored(perevod.text, 'blue'))
        elif "на немецкий" in result:
            word = re.split(r'( на немецкий слово )|( на немецкий фразу )|( на немецкий предложение )|( на немецкий )', result)
            i = word[5]
            perevod = translator.translate(i, dest='de')
            print(colored(perevod.text, 'blue'))

    elif "число" in message:
        try:
            rand = re.split(r'(от)|(до)\s', message)
            a = int(rand[3])
            b = int(rand[6])
            i = random.randint(a, b)
            print(i)
            # say_message("Выпало число {0}".format(i))
        except:
            print(colored("Неправильно указан диапазон генерации чисел!", 'blue'))

    elif "браузер" in message:
        os.system('start chrome')

    elif "найди" in message or "открой" in message:
        search = re.split(r'(найди )|(открой )', message)
        url = "https://www.google.com/search?q=" + search[3]
        webbrowser.get().open(url)

    elif "подбрось монетку" in message or "монетка" in message:
        print('\033[1m' + 'Монетка брошена' + '\033[0m')
        time.sleep(1.5)
        flip_coin = random.randint(0, 1)
        if flip_coin == 0:
            print(colored("Выпала решка", 'blue'))
        elif flip_coin == 1:
            print(colored("Выпал орёл", 'blue'))

    # elif "поставь таймер" in message or "таймер" in message:
    #     timer

    elif "помощь" in message or "команды" in message:
        print(colored("Я умею следующее:" +
                      "\n * Находить информацию в google - команда: \"найди\"" +
                      "\n * Открывать видео на youtube - команда: \"видео\"" +
                      "\n * Находить информацию по погоде в городе - команда: \"погода\"" +
                      "\n * Переводить слова, фразы, предложения - команда: \"переведи\"" +
                      "\n * Назвать случайное число в определённом промежутке - команда: \"случайное число\"" +
                      "\n * Подбросить монетку - команда: \"подбрось монетку\"", 'blue'))
    else:
        print("Команда не распознана!")
        # say_message("Команда не распознана!")


# def say_message(message):
#     voice = gTTS(message, lang="ru")
#     file_voice_name = "audio" + str(random.randint(1, 100000000)) + ".mp3"
#     voice.save(file_voice_name)
#     playsound.playsound(file_voice_name)
#     os.remove(file_voice_name)


if __name__ == '__main__':
    while True:
        command = listen_command()
        do_this_command(command)
