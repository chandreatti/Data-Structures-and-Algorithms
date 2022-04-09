
def repeatedString(string, array_size):
    
    x = array_size // len(string)
    y = array_size % len(string)

    return (string.count('a') * x) + (string[:y].count('a'))

if __name__ == '__main__':
    
    s = input()

    n = int(input().strip())

    print(repeatedString(s, n))