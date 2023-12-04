lines = open("input.txt").read().splitlines()
#print(lines)


part1_total = 0


card_num = 1
for line in lines:
    current_line_sum = 0
    
    line = line.split("|")
    nums = line[1].strip().split(" ")
    ## remove all empty strings from list
    while '' in nums:
        nums.remove('')
    dummy = line[0].split(":")
    winning_numbers = dummy[1].strip().split(" ")
    while '' in winning_numbers:
        winning_numbers.remove('')
    #print(winning_numbers)

    # check for winning numbers
    for num in nums:
        if num in winning_numbers:
            if current_line_sum == 0:
                current_line_sum += 1
            else:
                current_line_sum *= 2
    #print(f"card: {card_num} | {current_line_sum}")
    card_num += 1
    part1_total += current_line_sum
    
print(part1_total)

