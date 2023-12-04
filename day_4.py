from pathlib import Path

def part_1():
    lines = Path('day_4.txt').read_text().splitlines()
    total_score = 0
    for line in lines:
        scores_and_draws = line.split(":")[-1].strip()
        scores_str, draws_str = map(str.strip, scores_and_draws.split("|"))
        scores = {int(score) for score in scores_str.split()}
        draws = [int(draw) for draw in draws_str.split()]
        scores_this_round = 0
        for draw in draws:
            if draw in scores:
                scores_this_round += 1
        total_score += 2 ** (scores_this_round - 1) if scores_this_round else 0
    print(total_score)


def part_2():
    lines = Path('day_4.txt').read_text().splitlines()
    total_score = 0
    count = 0
    number_of_games = [1 for _ in lines]
    for game_n, line in enumerate(lines):
        for i in range(number_of_games[game_n]):
            count += 1
            scores_and_draws = line.split(":")[-1].strip()
            scores_str, draws_str = map(str.strip, scores_and_draws.split("|"))
            scores = {int(score) for score in scores_str.split()}
            draws = [int(draw) for draw in draws_str.split()]

            number_of_wins = sum((1 for draw in draws if draw in scores))
            for x in range(number_of_wins):
                number_of_games[game_n + x + 1] += 1

    print(count)


def main() -> None:
    part_2()

if __name__ == '__main__':
    main()