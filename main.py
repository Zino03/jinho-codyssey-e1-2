from quiz_game import QuizGame

if __name__ == "__main__":
    game = QuizGame()
    try:
        game.run()
    except (KeyboardInterrupt, EOFError):
        print("\n입력이 중단되어 프로그램을 종료합니다.")
        game.save_state() # 비정상 종료에서도 가능한 범위에서 저장