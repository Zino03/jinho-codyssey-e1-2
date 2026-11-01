# 퀴즈 게임
from quiz import Quiz


def default_quizzes():
    # 첫 실행이나 파일 손상 시 사용할 기본 퀴즈 목록을 만들어 반환
    # 퀴즈 주제 : python 기초
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
            print("값을 입력해주세요\n")
            continue
        
        try:
            select_num = int(select) # 숫자 변환 (실패 시 ValueError) 
            if select_num <= high and select_num >= low: # 입력값 범위 설정
                return select_num
            print(f"{low} ~ {high} 사이의 숫자를 입력해주세요.")
        except(ValueError):
            print("숫자를 입력해주세요.\n")


def play_quiz(quizzes): # 퀴즈 풀기
    count = 0 # 퀴즈 맞춘 수 카운팅
    n = 1 # 퀴즈 번호 넘버링
    quiz_len = len(quizzes) # 퀴즈 총 개수
    if not quizzes: # 저장된 퀴즈가 없는 경우 처리
        print("저장된 퀴즈가 없습니다.")
    else:
        print("\n========================================")
        print(f"퀴즈를 시작합니다 (총 {quiz_len}문제)\n")
        for q in quizzes: # 반복문을 통해 quizzes 안에 Quiz 객체를 하나씩 가져옴
            print(f"{n}.", end=" ") # 퀴즈 번호 (줄바꿈 안되게)
            q.show_quiz() # 문제 및 선택지 출력
            user_choice = read("정답 입력: ", 1, 4) # 사용자가 입력한 정답 저장
            n += 1 # 퀴즈 번호 + 1
            if q.check(user_choice): # 정답과 일치하는지 확인
                count += 1
                print("정답입니다!\n")
            else:
                print(f"오답입니다ㅠㅠ (정답: {q.answer})\n")
                
        print(f"맞힌 개수: {count} / 전체 문제 수: {quiz_len}")
        
        score = round(count / quiz_len * 100) # 점수 계산 (소수점 없이 반올림)
        print(f"점수: {score}점\n")
        return score


def add_quiz(quizzes): # 퀴즈 추가
    print("추가하실 퀴즈를 입력해주세요")
    while True:
        question = input("문제: ").strip() # 공백만 있는 문자열 처리
        if question == "": # 빈 문자열 입력 받은 경우 처리
            print("문제를 입력해주세요.")
            continue
        break
        
    choices = [] # 선택지 담을 리스트
    n = 1 # 선택지 번호 넘버링
    while True:
        c = input(f"{n}번 선택지: ").strip() # 공백만 있는 문자열 처리
        if c == "": # 빈 문자열 입력 받은 경우 처리
            print("선택지를 입력해주세요.")
            continue
        choices.append(c) # append 함수를 통해 입력 받은 순서대로 선택지 삽입
        n += 1 # 
        if n > 4: # 4개 입력 받으면 종료
            break
    
    answer = read("정답을 입력해주세요 (1 ~ 4): ", 1, 4) # 문제에 대한 정답 입력 받기
    q = Quiz(question, choices, answer) # Quiz 객체 생성
    quizzes.append(q) # 퀴즈 목록에 추가
    print("퀴즈 추가가 완료되었습니다!\n")
    

def list_quizzes(quizzes): # 퀴즈 목록
    if not quizzes: # 저장된 퀴즈가 없는 경우
        print("저장된 퀴즈가 없습니다.\n")
    else:
        print(f"\n등록된 퀴즈 목록 (총 {len(quizzes)}개)\n")
        n = 1 # 퀴즈 목록 넘버링
        for q in quizzes:
            print(f"[{n}] {q.question}")
            n += 1
        print()
            

def show_score(best_score): # 점수 확인 (최고 점수)
    if best_score < 0:
        print("아직 퀴즈를 풀지 않았습니다.\n")
    else:
        print(f"최고 점수: {best_score}점!\n")
    

def update_score(best_score, score): # 최고 점수 갱신
    if score == None: # quiz가 없는 경우 score가 None 저장
        print("등록된 퀴즈가 없습니다.\n")
        return best_score # 비교 불가로 best_score 유지
        
    if best_score < score: # 점수 비교 후 score 갱신
        print("새로운 최고 점수입니다!\n")
        return score
    return best_score # score가 더 작으면 기존의 best_score 그대로 반환

  
def main(): 
    quizzes = default_quizzes() # 기본 퀴즈
    best_score = -1 # best_score 초기값
    while True: # 5번 선택으로 종료하기 전까지 계속 반복
        show_menu() # 메뉴 출력
        select = read("선택: ", 1, 5) # 메뉴 선택

        if select == 1: # 퀴즈 풀기
            score = play_quiz(quizzes) # 퀴즈 풀이 후 점수 반환
            best_score = update_score(best_score, score) # 위에서 받은 점수와 best_score 비교
        elif select == 2: # 퀴즈 추가
            add_quiz(quizzes)
        elif select == 3: # 퀴즈 목록
            list_quizzes(quizzes)
        elif select == 4: # 점수 확인
            show_score(best_score)
        elif select == 5: # 종료
            print("프로그램을 종료합니다")
            break


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\n입력이 중단되어 프로그램을 종료합니다.")