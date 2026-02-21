import speech_recognition as sr
import pyttsx3

class SpeechHandler:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.engine = pyttsx3.init()

    def recognize_speech(self):
        with sr.Microphone() as source:
            print("Adjusting for ambient noise...")
            self.recognizer.adjust_for_ambient_noise(source)
            print("Listening...")
            audio = self.recognizer.listen(source)
            try:
                print("Recognizing...")
                return self.recognizer.recognize_google(audio)
            except sr.UnknownValueError:
                print("Could not understand audio.")
                return None
            except sr.RequestError:
                print("Could not request results from Google Speech Recognition service.")
                return None

    def text_to_speech(self, text):
        self.engine.say(text)
        self.engine.runAndWait()

# Example usage
# handler = SpeechHandler()
# recognized_text = handler.recognize_speech()
# if recognized_text:
#     handler.text_to_speech(recognized_text)