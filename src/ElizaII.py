import random
import re

bot_template = "BOT : {0}"
user_template = "USER : {0}"

# This bot is called Eliza II : It extracts key phrases
rules = {'I want (.*)': ['What would it mean if you got {0}', 'Why do you want {0}', "What's stopping you from getting {0}"],
         'do you remember (.*)': ['Did you think I would forget {0}', "Why haven't you been able to forget {0}",
                                  'What about {0}', 'Yes .. and?'],
         'if (.*)': ["Do you really think it's likely that {0}", 'Do you wish that {0}', 'What do you think about {0}', 'Really--if {0}'],
         'do you think (.*)': ['if {0}? Absolutely.', 'No chance']}


# Define match_rule()
def match_rule(rules, message):
    response, phrase = "default", None

    # Iterate over the rules dictionary
    for pattern, responses in rules.items():
        # Create a match object
        match = re.search(pattern, message)
        if match is not None:
            # Choose a random response
            response = random.choice(responses)
            if '{0}' in response:
                phrase = response.format(match.group(1))
    # Return the response and phrase
    return response, phrase


# Define a function that sends a message to the bot: send_message
def send_message(message):
    # Print user_template including the user_message
    print(user_template.format(message))
    # Get the bot's response to the message
    response = respond(message)
    # Print the bot template including the bot's response.
    print(bot_template.format(response))

def respond(message):
    response, phrase = match_rule(rules, message)
    if(phrase!=None):
        return phrase
    else:
        return response


# Test match_rule
send_message("do you remember your last birthday?")
send_message("I want you to recall the day")
send_message("do you think it was special?")