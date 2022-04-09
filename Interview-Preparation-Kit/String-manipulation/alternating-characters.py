
def alternatingCharacters(string):

    counter = 0
    previous_letter = string[0]

    for letter_position in range(1, len(string)):
        
        if (string[letter_position] == previous_letter):
            counter += 1
        
        previous_letter = string[letter_position]
    
    return counter

if __name__ == '__main__':

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        print(alternatingCharacters(s))