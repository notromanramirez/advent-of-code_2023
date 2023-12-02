# Roman Ramirez
# ADVENT OF CODE 2023
# DAY 01

def get_input(filename):
    my_input = []
    with open(filename,'r') as f:
        for line in f:
            my_input.append(line.strip())
    return my_input

def calc_line(line):
    line_no_str = "".join([c for c in line if not c.isalpha()])
    return int(line_no_str[0] + line_no_str[-1])

def calc_line_v2(line):
    word2num = {
        "one":1,
        "two":2,
        "three":3,
        "four":4,
        "five":5,
        "six":6,
        "seven":7,
        "eight":8,
        "nine":9,
        "zero":0
    }
    
    first_num = None
    last_num = None
    
    # looking for first_num with a forward search
    i = 0
    while first_num is None:
        if line[i].isalpha():
            for (k,v) in word2num.items():
                if line[i:i+len(k)] == k:
                    first_num = str(v)
        elif not line[i].isalpha():
            first_num = line[i]
        i += 1

    # looking for last_num with a backwards search
    i = len(line)-1
    while last_num is None:
        if line[i].isalpha():
            for (k,v) in word2num.items():
                if line[i-len(k)+1:i+1] == k:
                    last_num = str(v)
        elif not line[i].isalpha():
            last_num = line[i]
        i -= 1
    return int(first_num + last_num)

def part1():
    text = get_input('input.txt')
    total = 0
    for line in text:
        total += calc_line(line)
    print(total)

def part2():
    text = get_input('input.txt')
    total = 0
    line = text[0]
    for line in text:
        total += calc_line_v2(line)
    print(total)

if __name__ == '__main__':
    part2()