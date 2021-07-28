from dialog.blenderbot.blenderbot import Blenderbot
from dialog.blenderbot.chatbot import Dialog, Utterance

bot = Blenderbot()
dialog = Dialog()

print("start a conversation:\n")
while True:
    userInput = input()
    dialog.append(Utterance(userInput))
    response = bot.respond(dialog)
    dialog.append(response)
    print(response)


