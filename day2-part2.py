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

    red_regex = re.compile(r'(\d+) red')
    red_raw = red_regex.findall(input)
    red_int = [int(item) for item in red_raw]
    red_int.sort(reverse=True)
    smallest_red = red_int[0]
    


    green_regex = re.compile(r'(\d+) green')
    green_raw = green_regex.findall(input)
    green_int = [int(item) for item in green_raw]
    green_int.sort(reverse=True)
    smallest_green = green_int[0]

    
    blue_regex = re.compile(r'(\d+) blue')
    blue_raw = blue_regex.findall(input)
    blue_int = [int(item) for item in blue_raw]
    blue_int.sort(reverse=True)
    smallest_blue = blue_int[0]

    power = smallest_red * smallest_blue * smallest_green
    print(smallest_red, smallest_blue, smallest_green, " power is ", power)
    
    ans += power


print(ans)