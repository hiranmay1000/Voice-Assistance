import pyttsx3

def get_all_voices():
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')

    voice_list = []
    for voice in voices:
        voice_list.append(voice.name)

    return voice_list

if __name__ == "__main__":
    all_voices = get_all_voices()

    if all_voices:
        print("Available Voices:")
        for index, voice in enumerate(all_voices, start=1):
            print(f"{index}. {voice}")
    else:
        print("No voices found on your computer.")
