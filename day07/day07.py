with open("input.txt", "r") as input_file:
    lines = [line.strip() for line in input_file]

lines = [line.split(" ") for line in lines]
lines = [[int(line[0].removesuffix(":")), [int(s) for s in line[1:]]] for line in lines]

def get_operator_results(ints):
    if len(ints) == 1:
        return [ints[0]]
    results = []
    for r in get_operator_results(ints[:-1]):
        results.append(ints[-1] + r)
        results.append(ints[-1] * r)
        results.append(int(str(r) + str(ints[-1]))) # part 2
    return results

total_calibration_result = 0
for line in lines:
    results = get_operator_results(line[1])
    if line[0] in results:
        total_calibration_result += line[0]

print(total_calibration_result)
