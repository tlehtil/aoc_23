import re

with open('day3_input.txt') as inputfile:
    input_content = inputfile.readlines()
prev = 0
next = 2
counter = 0
ans = 0

regex_aft = re.compile(r'[^.\d](\d+)')
regex_bef = re.compile(r'(\d+)[^.\d]')
regex_no = re.compile(r'(\d+)')

for input in input_content:
    sameline_aft = regex_aft.findall(input)
    if sameline_aft:
        for i in sameline_aft:
            x = [int(item) for item in i]
            ans += x
    sameline_bef = regex_bef.findall(input)
    if sameline_bef:
        for i in sameline_bef:
            x = [int(item) for item in i]
            ans += x
    if prev == 0:
        pos = regex_no.search(input)
