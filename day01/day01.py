with open("input.txt", "r") as input_file:
    lines = [tuple(map(int, line.strip().split())) for line in input_file]

first_numbers = sorted(line[0] for line in lines)
second_numbers = sorted(line[1] for line in lines)
lines = [(min(line), max(line)) for line in zip(first_numbers, second_numbers)]

sum_distances = sum(abs(line[0] - line[1]) for line in lines)
print(sum_distances)

similarity_scores = [n * second_numbers.count(n) for n in first_numbers]
print(sum(similarity_scores))
