from game import Game
from score import Score


def main():
    game = Game(Score.ZERO, Score.ZERO)
    while not game.is_over():
        print(f"Current score is {game.format_score()}")
        player = input("Enter which player scored:").lower()
        if player[0] == "s":
            game.increment_server_score()
        elif player[0] == "r":
            game.increment_receiver_score()
        else:
            print("Invalid input")
    print(f"Winner is: {game.winner()}")


if __name__ == "__main__":
    main()
