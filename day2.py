import re

with open('day2_input.txt') as inputfile:
    input_content = inputfile.readlines()

red_cubes = 12
green_cubes = 13
blue_cubes = 14
all_cubes = red_cubes + green_cubes + blue_cubes

ans = 0

for input in input_content:
    game_regex = re.compile(r'Game (\d+)')
    game_raw = game_regex.search(input)
    game_no = game_raw.group(1)
    print(game_no)
    cont = True
    red_regex = re.compile(r'(\d+) red')
    red_raw = red_regex.findall(input)
    red_int = [int(item) for item in red_raw]
    #red_sum = sum(red_int)
    for i in red_int:
        if i > red_cubes:
            cont = False

    green_regex = re.compile(r'(\d+) green')
    green_raw = green_regex.findall(input)
    green_int = [int(item) for item in green_raw]
    #green_sum = sum(green_int)
    for i in green_int:
        if i > green_cubes:
            cont = False
    
    blue_regex = re.compile(r'(\d+) blue')
    blue_raw = blue_regex.findall(input)
    blue_int = [int(item) for item in blue_raw]
    #blue_sum = sum(blue_int)
    for i in blue_int:
        if i > blue_cubes:
            cont = False
    if cont:
        print("Match")
        ans += int(game_no)
"""     #all_sum = red_sum + green_sum + blue_sum

    if all_sum < all_cubes:
        if red_sum < red_cubes and green_sum < green_cubes and blue_sum < blue_cubes: """

print(ans)