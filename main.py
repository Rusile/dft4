import datetime

import speech_recognition as sr
import pyttsx3
import requests
from googletrans import Translator

# Создаем объекты для распознавания речи и синтеза речи
r = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
translator = Translator()

engine.setProperty('voice', 'ru')
for voice in voices:
    if voice.name == 'Aleksandr':
        engine.setProperty('voice', voice.id)


# Функция для синтеза речи
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Функция для распознавания речи и выполнения команды
def recognize_speech():
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("Скажите что-нибудь...")
        audio = r.listen(source)

    try:
        # Распознаем речь с помощью Google Speech Recognition
        command = r.recognize_google(audio, language="ru-RU")
        print("Вы сказали: " + command)

        # Выполняем команду
        if "факт о числе" in command:
            response = requests.get("http://numbersapi.com/random/math")
            text = translator.translate(response.text.strip(), src='en', dest='ru').text
            speak(text)
        elif "интересный год" in command:
            response = requests.get("http://numbersapi.com/random/year")
            text = translator.translate(response.text.strip(), src='en', dest='ru').text
            speak(text)
        elif "забавный факт" in command:
            response = requests.get("http://numbersapi.com/random/trivia")
            text = translator.translate(response.text.strip(), src='en', dest='ru').text
            speak(text)
        elif "интересный месяц" in command:
            response = requests.get("http://numbersapi.com/random/date")
            text = translator.translate(response.text.strip(), src='en', dest='ru').text
            speak(text)
        elif "пока" in command:
            speak("До свидания!")
            exit()
        else:
            speak("Я не понимаю, что вы сказали.")
    except sr.UnknownValueError:
        print("Не удалось распознать речь")
    except sr.RequestError as e:
        print("Ошибка сервиса распознавания речи; {0}".format(e))

# Бесконечный цикл для распознавания речи и выполнения команд
while True:
    recognize_speech()