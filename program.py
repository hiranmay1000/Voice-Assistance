print("Code entry...")
import speech_recognition as sr
import pyttsx3 as tt

listener = sr.Recognizer()

try:
    with sr.Microphone() as source:
        print("\n\nListening...")
        ret, voice = listener.listen(source);
        if ret:
            print("Please wait while proccessing your request...");
        command = listener.recognize_google(voice)
        print(command)
        

except:
    pass

print("\n\n\nCode end...")


# !DEPENDENCIES
# sudo apt-get install portaudio19-dev
# pip install pyaudio

