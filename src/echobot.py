bot_template = "BOT : {0}"
user_template = "USER : {0}"


# Define a function that responds to a user's message: respond
def respond(message):
    # Concatenate the user's message to the end of a standard bot respone
    bot_message = "I can hear you! You said: " + message
    # Return the result
    return bot_message

if __name__ == "__main__":
    print(respond("Hi how are you!"))