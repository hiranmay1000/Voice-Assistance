import pyttsx3

def get_all_voices():
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    choices = 0
    gender_spec = ["male", "female", "none", "exit"]
    choices = int(input("\n1. Male\n2.Female\n3.None\n4.Exit\n_"))
    

    voice_list = []
    for index, voice in enumerate(voices, start=0):
        if choices > 3:
            return []

        if voice.gender == gender_spec[choices - 1]:
            voice_info = {
                "ID": index,
                "Name": voice.name,
                "Languages": [lang.decode('utf-8') for lang in voice.languages],
                "Gender": voice.gender,
            }
            voice_list.append(voice_info)
    

    return voice_list

if __name__ == "__main__":
    all_voices = get_all_voices()

    if all_voices:
        print("Available Voices:")
        for voice_info in all_voices:
            print(f"ID: {voice_info['ID']}")
            print(f"Name: {voice_info['Name']}")
            print(f"Languages: {', '.join(voice_info['Languages'])}")
            print(f"Gender: {voice_info['Gender']}")
            print("----------")
    else:
        print("No voices found on your computer.")

    print("\nTotal voices generated: ", len(all_voices))