import json # json 파일 읽고 쓰는 표준 library
from pathlib import Path # 파일 경로 다루는 도구

from quiz import Quiz

# state.json의 위치: 해당 파일이 있는 폴더
STATE_FILE = Path(__file__).parent / "state.json"

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


class QuizGame:
    def __init__(self):
        self.quizzes = self.default_quizzes() # 기본 퀴즈
        self.best_score = -1 # 최고 점수 초기값
        self.load_state() # 시작할 때 저장된 데이터를 불러옴

    def default_quizzes(self):
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
    def show_menu(self):
        print("========================================")
        print("            진호의 퀴즈 게임")
        print("========================================")
        print("1. 퀴즈 풀기")
        print("2. 퀴즈 추가")
        print("3. 퀴즈 목록")
        print("4. 점수 확인")
        print("5. 종료")
        print("========================================")

    def play_quiz(self): # 퀴즈 풀기
        count = 0 # 퀴즈 맞춘 수 카운팅
        n = 1 # 퀴즈 번호 넘버링
        quiz_len = len(self.quizzes) # 퀴즈 총 개수
        if not self.quizzes: # 저장된 퀴즈가 없는 경우 처리
            print("저장된 퀴즈가 없습니다.")
        else:
            print("\n========================================")
            print(f"퀴즈를 시작합니다 (총 {quiz_len}문제)\n")
            for q in self.quizzes: # 반복문을 통해 quizzes 안에 Quiz 객체를 하나씩 가져옴
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
       
    def add_quiz(self): # 퀴즈 추가
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
            n += 1 
            if n > 4: # 4개 입력 받으면 종료
                break
        
        answer = read("정답을 입력해주세요 (1 ~ 4): ", 1, 4) # 문제에 대한 정답 입력 받기
        q = Quiz(question, choices, answer) # Quiz 객체 생성
        self.quizzes.append(q) # 퀴즈 목록에 추가
        print("퀴즈 추가가 완료되었습니다!\n")
        self.save_state() # 추가한 퀴즈 파일에 바로 저장

    def list_quizzes(self): # 퀴즈 목록
        if not self.quizzes: # 저장된 퀴즈가 없는 경우
            print("저장된 퀴즈가 없습니다.\n")
        else:
            print(f"\n등록된 퀴즈 목록 (총 {len(self.quizzes)}개)\n")
            n = 1 # 퀴즈 목록 넘버링
            for q in self.quizzes:
                print(f"[{n}] {q.question}")
                n += 1
            print()

    def show_score(self):# 점수 확인 (최고 점수)
        if self.best_score < 0:
            print("아직 퀴즈를 풀지 않았습니다.\n")
        else:
            print(f"최고 점수: {self.best_score}점!\n")

    def update_score(self, score): # 최고 점수 갱신
        if score is None: # quiz가 없는 경우 score가 None 저장
            return self.best_score # 비교 불가로 best_score 유지
            
        if self.best_score < score: # 점수 비교 후 score 갱신
            print("새로운 최고 점수입니다!\n")
            return score
        return self.best_score # score가 더 작으면 기존의 best_score 그대로 반환

    def run(self):
        while True: # 5번 선택으로 종료하기 전까지 계속 반복
            self.show_menu() # 메뉴 출력
            select = read("선택: ", 1, 5) # 메뉴 선택
            
            if select == 1: # 퀴즈 풀기
                score = self.play_quiz() # 퀴즈 풀이 후 점수 반환
                self.best_score = self.update_score(score) # 위에서 받은 점수와 best_score 비교
                self.save_state() # 갱신됐을 수도 있으니 파일에 저장 (갱신 안 돼도 저장해서 단순하게)  
            elif select == 2: # 퀴즈 추가
                self.add_quiz()
            elif select == 3: # 퀴즈 목록
                self.list_quizzes()
            elif select == 4: # 점수 확인
                self.show_score()
            elif select == 5: # 종료
                print("프로그램을 종료합니다")
                self.save_state() # 종료 직전에 한 번 더 저장 (안전장치)
                break
            
    def save_state(self): # 퀴즈 목록과 최고 점수를 state.json에 저장
        data = {
            "quizzes": [q.to_dict() for q in self.quizzes], # Quiz 객체를 dict로 바꾼 리스트
            "best_score": self.best_score,
        }
        try: # 파일 쓰기 실패할 수도 있으니 try-except 사용
            with open(STATE_FILE, "w", encoding="utf-8") as f: # 쓰기 모드로 open
                json.dump(data, f, ensure_ascii=False, indent=4)
                # 데이터를 json 형식으로 f에 쓰고, 한글을 그대로 저장, 들여쓰기 사용
        except OSError:
            print("파일 저장에 실패했습니다. 이번 변경 내용은 저장되지 않을 수 있습니다.\n") # 프로그램은 멈추지 않고 안내만 출력

    def load_state(self): # state.json에서 데이터를 불러옴 (파일이 없거나 손상되면 기본 데이터를 사용)
        try:
            with open(STATE_FILE, "r", encoding="utf-8") as f: # 읽기 모드로 open
                data = json.load(f) # 파일 내용을 읽음 (json 문법이 깨져 있으면 JSONDecodeError)
            quizzes = [Quiz.from_dict(item) for item in data["quizzes"]] # 딕셔너리들을 Quiz 객체로 복원
            # 키가 없으면 KeyError, 내용이 잘못되면 ValueError
            best_score = data["best_score"] # 최고 점수 읽기 (키가 없으면 KeyError)
            if (not isinstance(best_score, int) or isinstance(best_score, bool)
                    or not -1 <= best_score <= 100): # 정수가 아니거나, bool이거나, 범위 밖이면 ValueError
                raise ValueError("최고 점수가 올바르지 않습니다.")
        except FileNotFoundError: # open 시 파일이 없는 경우
            # 첫 실행: 기본 퀴즈를 그대로 쓰고 파일을 새로 만든다
            self.save_state() # 기본 데이터로 state.json을 새로 만듦
            return
        except (json.JSONDecodeError, KeyError, TypeError, ValueError):
            # 파일이 있지만 내용이 손상됨: 기본 데이터로 초기화
            print("저장 파일이 손상되어 기본 퀴즈로 초기화합니다.\n")
            self.save_state() # 기본 데이터로 복구
            return
        except OSError:
            # 읽기 권한 등 파일 접근 문제
            print("저장 파일을 읽을 수 없어 기본 데이터로 시작합니다.\n")
            return

        # 모든 검증을 통과했을 때만 덮어씀
        self.quizzes = quizzes
        self.best_score = best_score
        score_text = "없음" if best_score < 0 else f"{best_score}점"
        print(f"저장된 데이터를 불러왔습니다. (퀴즈 {len(quizzes)}개, 최고 점수 {score_text})\n")
