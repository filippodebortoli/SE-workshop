class Question(object):
    def __init__(self,title: str, answer: str):
        """
        Constructor with title and answer
        :param title: The question's title (the question)
        :param answer: The question's answer
        """
        self.title = title
        self.answer = answer

    def __eq__(self, other):
        return isinstance(other, self.__class__) and getattr(other, 'title') == self.title and getattr(other, 'answer') == self.answer

    def __hash__(self):
        return hash(self.title + self.answer)