all_scores_value: dict[str, int] = {"X": 1, "Y": 2, "Z": 3, "A": 1, "B": 2, "C": 3}
lookup_map: dict[str, str] = {
    "A": "Rock",
    "B": "Paper",
    "C": "Scissors",
    "X": "Rock",
    "Y": "Paper",
    "Z": "Scissors",
}
wanted_outcome: dict[str, int] = {"Y": 0, "X": -1, "Z": 1}  # draw, lose, win


def part_2() -> int:
    total_score: int = 0
    with open("input.txt") as file:
        for line in file:
            scores: list[str] = line.strip().split(" ")

            opponent_choice: str = scores[0]
            my_choice: str = scores[1]

            opponent_score: int = all_scores_value[opponent_choice]

            # draw
            if wanted_outcome[my_choice] == 0:
                total_score += 3
                total_score += opponent_score

            # win
            if wanted_outcome[my_choice] == 1:
                total_score += 6

                if lookup_map[opponent_choice] == "Paper":
                    total_score += 3  # scissors
                if lookup_map[opponent_choice] == "Rock":
                    total_score += 2  # paper
                if lookup_map[opponent_choice] == "Scissors":
                    total_score += 1  # rock

            # lose
            if wanted_outcome[my_choice] == -1:
                if lookup_map[opponent_choice] == "Paper":
                    total_score += 1  # rock
                if lookup_map[opponent_choice] == "Scissors":
                    total_score += 2  # paper
                if lookup_map[opponent_choice] == "Rock":
                    total_score += 3  # scissors

        return total_score


if __name__ == "__main__":
    part_2_ans: int = part_2()
    print(f"part_2_ans:{part_2_ans}")
