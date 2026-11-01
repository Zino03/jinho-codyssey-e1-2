# 퀴즈 게임
from quiz import Quiz


def default_quizzes():
    # 첫 실행이나 파일 손상 시 사용할 기본 퀴즈 목록을 만들어 반환
    return [
        Quiz(
            "키(key)와 값(value)의 쌍으로 데이터를 저장하는 자료형은?",
            ["list", "dict", "tuple", "set"],
            2,
        ),
        Quiz(
            "다음 중 문자열(str) 값은?",
            ["3", "3.0", "True", '"3"'],
            4,
        ),
        Quiz(
            "조건식이 참인 동안 계속 반복하는 반복문은?",
            ["while", "for", "if", "def"],
            1,
        ),
        Quiz(
            "함수가 계산한 결과를 호출한 곳으로 돌려줄 때 사용하는 키워드는?",
            ["print", "input", "return", "break"],
            3,
        ),
        Quiz(
            "클래스로 객체를 만들 때 자동으로 실행되어 초기값을 저장하는 메서드는?",
            ["__str__", "__del__", "__call__", "__init__"],
            4,
        ),
        Quiz(
            "오류가 발생해도 프로그램이 비정상 종료되지 않도록 처리할 때 사용하는 구문은?",
            ["if / else", "try / except", "for / while", "import / from"],
            2,
        ),
    ]


# 메뉴창
def show_menu():
    print("========================================")
    print("            진호의 퀴즈 게임")
    print("========================================")
    print("1. 퀴즈 풀기")
    print("2. 퀴즈 추가")
    print("3. 퀴즈 목록")
    print("4. 점수 확인")
    print("5. 종료")
    print("========================================")
    
    
# 선택 값 읽기
# 제대로 된 값이 입력될 때까지 반복하고 정수 반환
def read(prompt, low, high):
    while True:
        select = input(prompt).strip() # 앞뒤 공백 제거
        if select == "": # 빈 입력 처리
            print("값을 입력해주세요")
            continue
        
        try:
            select_num = int(select) # 숫자 변환 (실패 시 ValueError) 
            if select_num <= high and select_num >= low:
                return select_num
            print(f"{low} ~ {high} 사이의 숫자를 입력해주세요.")
        except(ValueError):
            print("숫자를 입력해주세요.")


def play_quiz(quizzes):
    count = 0
    n = 1
    quiz_len = len(quizzes)
    if not quizzes:
        print("저장된 퀴즈가 없습니다.")
    else:
        print("\n========================================")
        print(f"퀴즈를 시작합니다 (총 {quiz_len}문제)\n")
        for q in quizzes:
            print(f"{n}.", end=" ")
            q.show_quiz()
            user_choice = read("정답 입력: ", 1, 4)
            n += 1
            if q.check(user_choice):
                count += 1
                print("정답입니다!\n")
            else:
                print(f"오답입니다ㅠㅠ (정답: {q.answer})\n")
                
        print(f"맞힌 개수: {count} / 전체 문제 수: {quiz_len}")
        
        score = round(count / quiz_len * 100, 2)
        print(f"점수: {score}점\n")
        return score

def add_quiz(quizzes):
    print("추가하실 퀴즈를 입력해주세요")
    question = ""
    while True:
        question = input("문제: ").strip()
        if question == "":
            print("문제를 입력해주세요.")
            continue
        break
        
    choices = []
    n = 1
    while True:
        c = input(f"{n}번 선택지: ").strip()
        if c == "":
            print("선택지를 입력해주세요.")
            continue
        choices.append(c)
        n += 1
        if n > 4:
            break
    
    answer = read("정답을 입력해주세요 (1 ~ 4): ", 1, 4)
    q = Quiz(question, choices, answer)
    quizzes.append(q)
    print("퀴즈 추가가 완료되었습니다!\n")
    

def list_quizzes(quizzes):
    if not quizzes:
        print("저장된 퀴즈가 없습니다.")
    else:
        print(f"\n등록된 퀴즈 목록 (총 {len(quizzes)}개)\n")
        n = 1
        for q in quizzes:
            print(f"[{n}] {q.question}")
            n += 1
        print()
            
        
  

def main():
    quizzes = default_quizzes()
    while True:
        show_menu()
        select = read("선택: ", 1, 5)
        # 항목 구현 전
        if select == 1:
            play_quiz(quizzes)
        elif select == 2:
            add_quiz(quizzes)
        elif select == 3:
            list_quizzes(quizzes)
        elif select == 4:
            break
        elif select == 5:
            print("프로그램을 종료합니다")
            break


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\n입력이 중단되어 프로그램을 종료합니다.")