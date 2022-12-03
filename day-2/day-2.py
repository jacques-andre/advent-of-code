opponent_scores = {"A": 1, "B": 2, "C": 3}
my_scores = {"X": 1, "Y": 2, "Z": 3}

lookup_map = {
    "A": "Rock",
    "B": "Paper",
    "C": "Scissors",
    "X": "Rock",
    "Y": "Paper",
    "Z": "Scissors",
}
lookup_score = {"Y": 0, "X": -1, "Z": 1}


total_score = 0
with open("input.txt") as file:
    for line in file:
        scores = line.strip().split(" ")
        print(scores)

        opponent_choice = scores[0]
        my_choice = scores[1]

        opponent_score = opponent_scores[opponent_choice]
        my_score = my_scores[my_choice]

        # draw
        if lookup_score[my_choice] == 0:
            total_score += 3
            total_score += opponent_score

        # win
        if lookup_score[my_choice] == 1:
            total_score += 6

            if lookup_map[opponent_choice] == "Paper":
                total_score += 3  # scissors
            if lookup_map[opponent_choice] == "Rock":
                total_score += 2  # paper
            if lookup_map[opponent_choice] == "Scissors":
                total_score += 1  # rock

        # lose
        if lookup_score[my_choice] == -1:
            if lookup_map[opponent_choice] == "Paper":
                total_score += 1  # rock
            if lookup_map[opponent_choice] == "Scissors":
                total_score += 2  # paper
            if lookup_map[opponent_choice] == "Rock":
                total_score += 3  # scissors

print(total_score)
