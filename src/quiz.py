class Quiz:
    def __init__(self, id, question, choices, answer):
        self.id = id
        self.question = question
        self.choices = choices
        self.answer = answer

    def printQuestion(self):
        print(f"{self.id}// {self.question}")
        print("\t" + self.choices)

    def checkAnswer(self, num):
        if (self.answer == num):
            return True
        else:
            return False