from quiz import Quiz

def get_menu_choice():
    print("1. 퀴즈 풀기 / 5. 종료")
    inputStr = input("진행할 메뉴 번호를 입력하세요 :")
    try:
        num = int(inputStr.strip())
        if (num < 1 or num > 5): return -1
    except:
        ValueError
        return -1
    return num

def startQuiz():
    quiz1 = Quiz(1, "Python에서 값을 이름에 저장할 때 사용하는 것은 무엇인가?", "1. 변수 / 2. 반복문 / 3. 주석 / 4. 파일", 1)
    quiz2 = Quiz(2, "점수처럼 정수를 저장하기에 알맞은 자료형은 무엇인가?", "1. `str` / 2. `int` / 3. `list` / 4. `bool`", 2)
    quiz3 = Quiz(3, "문제 문장이나 사용자 입력처럼 글자를 저장하기에 알맞은 자료형은 무엇인가?", "1. str / 2. int / 3. dict / 4. float", 1)
    default_quizzes = [quiz1, quiz2, quiz3]
    cnt = 0
    for quiz in default_quizzes:
        quiz.printQuestion()
        choice = input("정답을 입력하세요: ")
        choiceNum = -1
        try: 
            choiceNum = int(choice.strip()) 
        except: 
            ValueError
        if (quiz.checkAnswer(choiceNum)):
            print("정답입니다!")
            cnt+=1
        else:
            print("틀렸습니다!")
    return cnt


while True :
    num = get_menu_choice()
    if (num == 1) :
        print("퀴즈를 시작합니다.")
        cnt = startQuiz()
        print(f"3문제 중 {cnt}문제 정답`")
    elif (num == 5) :
        print("프로그램을 종료합니다.")
        break
    else :
        print("잘못된 값을 입력했습니다.")
