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
    
if __name__ == "__main__":
    q = Quiz("Python의 창시자는?", ["Guido", "Linus", "Bjarne", "James"], 1)
    q.show_quiz()
    print(q.check(1)) # True
    print(q.check(3)) # False