import re
with open('day1_input.txt') as inputfile:
    input_content = inputfile.readlines()

ans = 0

numbers = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
    }


for input in input_content:
    val1 = None
    val2 = None
    val_regex_n = re.compile(r'\D*(\d)?\S*(\d)\D*$')
    val_regex = re.compile(r'\D*?(one|two|three|four|five|six|seven|eight|nine|\d)\w*(\d|one|two|three|four|five|six|seven|eight|nine)\D*$')
    val_raw = val_regex.search(input)
    if not val_raw:
        val_raw = val_regex_n.search(input)
    #print(val_raw.groups())
    val1 = val_raw.group(1)
    val2 = val_raw.group(2)
    if val1 and val2:
        if val1.isnumeric() and val2.isnumeric():
            val = val1 + val2
            ans += int(val)
            print('Numbers: ', val)  
        else:
            if val1.isalpha():
                val1 = numbers[val1]
                print('Alpha val1: ',val1)
            if val2.isalpha():
                val2 = numbers[val2]
                print('Alpha val2: ', val2)
            val = str(val1) + str(val2)
            ans += int(val)
            print('Sum: ', val)
    else:
        val = val2 + val2
        ans += int(val)
        print('Numbers: ', val)

print(ans)