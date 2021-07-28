from transformers import BlenderbotTokenizer, BlenderbotForConditionalGeneration

from dialog.blenderbot.chatbot import Chatbot, Utterance, Dialog


class Blenderbot(Chatbot):
    def __init__(self):
        mname = 'facebook/blenderbot-3B'
        self.__model = BlenderbotForConditionalGeneration.from_pretrained(mname)
        self.__tokenizer = BlenderbotTokenizer.from_pretrained(mname)

    # def respond(self, dialog: Dialog) -> Utterance:
    #     chat = ''
    #     for i, val in enumerate(dialog.list()):
    #         prefix = '' if i == 0 else '<s>'
    #         suffix = '' if i == len(dialog.list()) - 1 else '</s> '
    #         chat += prefix + val.text + suffix + "\n"
    #     print(chat)
    #     inputs = self.__tokenizer([chat], return_tensors='pt')
    #     reply_ids = self.__model.generate(**inputs)
    #     reply = self.__tokenizer.batch_decode(reply_ids, skip_special_tokens=True)[0]
    #     return Utterance(reply, True)

    def respond(self, dialog: Dialog) -> Utterance:
        chat = ''
        for i, val in enumerate(dialog.list()):
            chat += val.text + "    "
        print(chat)
        inputs = self.__tokenizer([chat], return_tensors='pt')
        reply_ids = self.__model.generate(**inputs)
        reply = self.__tokenizer.batch_decode(reply_ids, skip_special_tokens=True)[0]
        return Utterance(reply, True)
