from PyDictionary import PyDictionary

from modules.speech_module import talk

dictionary = PyDictionary()

def process_dictionary(cmd):
    words_to_remove = ['what', 'is', 'the', 'meaning', 'of', 'means']

    for word in words_to_remove:
        cmd = cmd.replace(word, "")

    meaning_of_word = []
    for word in cmd:
        meaning_of_word.append(word)

    try:

        output = dictionary.meaning(meaning_of_word[0])
        talk("The meaning of " + meaning_of_word[0] + " is")
        talk(output)
    except Exception as e:
        talk(e)