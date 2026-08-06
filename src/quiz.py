class Quiz:
    def __init__(self, question, choices, answer):
        self.question = question
        self.choices = choices
        self.answer = answer

    def printQuestion(self):
        print(self.question)
        print(self.choices)

    def checkAnswer(self, num):
        if (self.answer == num):
            return True
        else:
            return False