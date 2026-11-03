class Quiz:
    def __init__(self, question, choices, answer):
        self.question = question # 문제
        self.choices = choices # 선택지
        self.answer = answer # 문제의 정답
        
    def show_quiz(self): # 문제와 선택지를 보여줌
        print(self.question)
        n = 1
        for c in self.choices: # 선택지에 번호 붙여서 출력
            print(f"{n}. {c}")
            n += 1
    
    def check(self, user_choice): # 정답 확인 (True or False 반환)
        return user_choice == self.answer
    
    def to_dict(self): # json 저장을 위해 dictionary 객체로 바꿈
        return {
            "question": self.question,
            "choices": self.choices,
            "answer": self.answer,
        }
    
    @classmethod
    def from_dict(cls, data): # dict를 Quiz 객체로 복원 (데이터가 올바르지 않으면 예외 처리)
        question = data["question"] # 키가 없으면 KeyError
        choices = data["choices"]
        answer = data["answer"]

        # 문제: 비어 있지 않은 문자열
        if not isinstance(question, str) or question.strip() == "":
            raise ValueError("문제가 올바르지 않습니다.")

        # 선택지: 문자열 4개로 이루어진 리스트
        if not isinstance(choices, list) or len(choices) != 4:
            raise ValueError("선택지는 4개의 리스트여야 합니다.")
        for c in choices:
            if not isinstance(c, str) or c.strip() == "":
                raise ValueError("선택지가 올바르지 않습니다.")

        # 정답: 1~4 사이의 정수 (bool은 int의 하위 타입이라 따로 제외)
        if not isinstance(answer, int) or isinstance(answer, bool) or not 1 <= answer <= 4:
            raise ValueError("정답은 1~4 사이의 정수여야 합니다.")

        return cls(question, choices, answer)
        