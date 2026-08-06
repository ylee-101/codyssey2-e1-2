from quiz import Quiz

def get_menu_choice():
    inputStr = input("정답을 입력하세요 :")
    try:
        num = int(inputStr.strip())
    except:
        ValueError
        return -1
    return num

while True :
    quiz = Quiz("문제입니다", "1.오답, 2.정답, 3.오답, 4.오답", 2)
    quiz.printQuestion()
    num = get_menu_choice()
    if (num == -1):
        print("잘못된 값을 입력했습니다.")
    elif (quiz.checkAnswer(num)) :
        print("정답입니다!")
        break
    else :
        print("땡!! 틀렸습니다!")
