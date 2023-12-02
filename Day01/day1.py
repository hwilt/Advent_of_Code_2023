lines = open("example_part2.txt").read().splitlines()
#print(lines)

DIGITS_part1 = {'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
DIGITS_part2 = {'one':1,'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7, 'eight':8,'nine':9}

print(str(lines[0][0:3]) in DIGITS_part2)
print(str(lines[0][0:3]))

total_sum = 0

first_number = -1
last_number = -1
for line in lines:
    
    line_sum = 0
    for char in line:
        if char in DIGITS_part1 and first_number == -1:
            #print("here")
            #print(DIGITS[char])
            first_number = DIGITS_part1[char]
            last_number = DIGITS_part1[char]
        elif char in DIGITS_part1 and first_number != -1:
            last_number = DIGITS_part1[char]
    #print(first_number*10, last_number)
    if first_number != -1:
        line_sum = first_number*10 + last_number
    total_sum += line_sum
    first_number = -1
    last_number = -1

print(total_sum)

