
def cmd_handling():
    messages = [
        "Sorry I couldn't hear you properly!",
        "Can you say that again?",
        "I am really sorry I don't get it.",
        "I am not sure what you are saying."
    ]

    selected_message = random.choice(messages)
    print_response(selected_message)
    talk(selected_message)
