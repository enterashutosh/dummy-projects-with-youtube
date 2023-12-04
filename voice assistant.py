import speech_recognition as sr
from gtts import gTTS
import playsound
import PyAudio
from googlesearch import search

def listen_for_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        audio = r.listen(source)

    try:
        command = r.recognize_google(audio)
        print("you said: ", command)
        return command.lower
    except sr.UnknownValueError:
        print("could not understand your command.")
    except sr.RequestError:
        print("could not request results; check your network connection.")

def execute_command():

    if "search" in command:
        query = command.replace("search", "").strip()
        search_results = list(search(query, num=5, stop=4, pause=2))
        for result in search_results:
            print(result)

            # converting results into speech
            text_to_speech = gTTS(result)
            text_to_speech.save("search results.mp3")

            # play the speech
            playsound.playsound("search results.mp3")

while True:

    command = listen_for_command()
    if command:
        execute_command(command)
