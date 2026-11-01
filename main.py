# 퀴즈 게임

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
            print("메뉴를 입력해주세요")
            continue
        
        try:
            select_num = int(select) # 숫자 변환 (실패 시 ValueError) 
            if select_num <= high and select_num >= low:
                return select_num
            print(f"{low} ~ {high} 사이의 숫자를 입력해주세요.")
        except(ValueError):
            print("숫자를 입력해주세요.")


def main():
    while True:
        show_menu()
        select = read("선택: ", 1, 5)
        # 항목 구현 전
        if select == 1:
            break
        elif select == 2:
            break
        elif select == 3:
            break
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