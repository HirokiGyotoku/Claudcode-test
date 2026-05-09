import random


HANDS = ("グー", "チョキ", "パー")


def judge(player: int, cpu: int) -> str:
    if player == cpu:
        return "あいこ"
    if (player - cpu) % 3 == 2:
        return "あなたの勝ち"
    return "あなたの負け"


def read_hand() -> int | None:
    prompt = "手を選んでください [0:グー / 1:チョキ / 2:パー / q:終了]: "
    while True:
        choice = input(prompt).strip()
        if choice.lower() in ("q", "quit", "exit"):
            return None
        if choice in ("0", "1", "2"):
            return int(choice)
        print("0, 1, 2 のいずれかを入力してください。")


def main() -> None:
    print("=== じゃんけんゲーム ===")
    wins = losses = draws = 0

    while True:
        player = read_hand()
        if player is None:
            break

        cpu = random.randint(0, 2)
        print(f"あなた: {HANDS[player]} / CPU: {HANDS[cpu]}")

        result = judge(player, cpu)
        print(f"=> {result}\n")

        if result == "あなたの勝ち":
            wins += 1
        elif result == "あなたの負け":
            losses += 1
        else:
            draws += 1

    print(f"\n戦績  勝ち:{wins}  負け:{losses}  あいこ:{draws}")
    print("ご利用ありがとうございました。")


if __name__ == "__main__":
    main()
