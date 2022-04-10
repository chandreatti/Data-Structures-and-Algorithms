
def countingValleys(path):

    level = 0
    valleys_counter = 0
    convert_levels = {'D' : -1, 'U' : 1}

    for step in path:
        level += convert_levels[step]
        if (level == 0) and (step == 'U'):
            valleys_counter += 1
    
    return valleys_counter

if __name__ == '__main__':
    
    steps = int(input().strip())

    path = input()

    print(countingValleys(path))