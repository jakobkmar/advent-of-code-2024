with open("input.txt", "r") as input_file:
    lines = [line.strip() for line in input_file]

rules = []
middle_numbers = []
corrected_middle_numbers = []

parsing_updates = False
for line in lines:
    if line == "":
        parsing_updates = True
    elif not parsing_updates:
        (first, second) = map(int, line.split("|"))
        rules.append((first, second))
    else:
        nums = [int(num) for num in line.split(",")]
        valid = True
        for rule in rules:
            try:
                index_first = nums.index(rule[0])
                index_second = nums.index(rule[1])
                if not index_first < index_second:
                    valid = False
                    break
            except ValueError:
                pass
        if valid:
            middle_numbers.append(nums[len(nums) // 2])
        else:
            while True:
                swapped = False
                for rule in rules:
                    try:
                        index_first = nums.index(rule[0])
                        index_second = nums.index(rule[1])
                        if not index_first < index_second:
                            swapped = True
                            nums[index_second] = rule[0]
                            nums[index_first] = rule[1]
                            break
                    except ValueError:
                        pass
                if not swapped:
                    break
            corrected_middle_numbers.append(nums[len(nums) // 2])

print(middle_numbers)
print(sum(middle_numbers))

print(corrected_middle_numbers)
print(sum(corrected_middle_numbers))
