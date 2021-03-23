number_lines = int(input())
match_outcomes = [input() for _ in range(number_lines)]
winners = [winner.split(" ")[0] for winner in match_outcomes if winner.endswith("win")]

print(winners)
print(len(winners))
