import SpeechRecognition as sr
import pyttsx3 as tt

listener = sr.Recognizer();
try:
    with sr.Microphone() as source:
        print("Listening...")
        voice = listener.listen(source);
        command = listener.recognizer_google(voice)
        print(command);

except:
    pass
