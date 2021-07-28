class Utterance:
    def __init__(self, text: str, bot: bool = False):
        self.text = text
        self.bot = bot

    def __str__(self):
        return self.text


class Dialog:
    def __init__(self, utterances=None):
        if utterances is None:
            utterances = []
        self.__utterances = utterances

    def last_utterance(self) -> Utterance:
        return self.__utterances[-1]

    def is_empty(self) -> bool:
        return not self.__utterances

    def append(self, utterance: Utterance):
        self.__utterances.append(utterance)

    def list(self) -> [Utterance]:
        return self.__utterances.copy()


class Chatbot:
    def respond(self, dialog: Dialog) -> Utterance:
        pass
