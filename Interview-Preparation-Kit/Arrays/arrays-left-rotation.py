
def rotLeft(array, left_rotations):
    return array[left_rotations:] + array[:left_rotations] 

if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    d = int(first_multiple_input[1])

    a = list(map(int, input().rstrip().split()))

    print(rotLeft(a, d))