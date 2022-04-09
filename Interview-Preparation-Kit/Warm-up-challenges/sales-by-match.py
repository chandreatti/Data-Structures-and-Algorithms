
def sockMerchant(n, ar):
    
    socks_used = []
    counter = 0
    
    for pos_num1 in range(n):
        for pos_num2 in range(n):
            if (ar[pos_num1] == ar[pos_num2]) and (pos_num1 != pos_num2):
                if (pos_num1 in socks_used) or (pos_num2 in socks_used):
                    pass
                else:
                    counter += 1
                    socks_used.append(pos_num1)
                    socks_used.append(pos_num2)
    
    return counter

if __name__ == '__main__':

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    print(sockMerchant(n, ar))