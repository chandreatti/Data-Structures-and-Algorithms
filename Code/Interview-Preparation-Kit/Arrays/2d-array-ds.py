
def sumFunc(x,y, array):
    sum_first_column = array[y][x] + array[y][x + 1] + array[y][x + 2]
    sum_second_column = array[y + 1][x + 1]
    sum_third_column = array[y + 2][x] + array[y + 2][x + 1] + array[y + 2][x + 2]

    return sum_first_column + sum_second_column + sum_third_column

def hourglassSum(array):
    max_value = -70
    
    for y in range(4):
        for x in range(4):
            result = sumFunc(x, y, array)
            if (result > max_value):
                max_value = result
    
    return max_value

if __name__ == '__main__':

    array = []

    for _ in range(6):
        array.append(list(map(int, input().rstrip().split())))

    print(hourglassSum(array))