import pyttsx3 as tt

engine = tt.init()
voices = engine.getProperty('voices')
selected_voice = voices[11].id

if selected_voice:
    engine.setProperty('voice', selected_voice)
else:
    print("No voices found!")

def talk(text):
    engine.say(text)
    engine.runAndWait()