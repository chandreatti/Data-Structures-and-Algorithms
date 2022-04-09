
def jumpingOnClouds(array, array_last_position, position=0, result=0):
    if position == array_last_position:
        return result
    else:
        if ((position + 2) <= array_last_position) and (array[position + 2] == 0):
            return jumpingOnClouds(array, array_last_position, position + 2, result + 1)
        elif ((position + 1) <= array_last_position) and (array[position + 1] == 0):
            return jumpingOnClouds(array, array_last_position, position + 1, result + 1)

if __name__ == '__main__':

    n = int(input().strip())

    c = list(map(int, input().rstrip().split()))

    print(jumpingOnClouds(c, n - 1))