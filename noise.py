"""Module to add edit noise to a text"""

import sys
import random
import string

def modify(word):
    """Modify the word by changing, removing or adding a character"""
    action = random.randint(1, 3)
    position = random.randint(0, len(word))

    if action == 1:
        return word[:position]+random.choice(string.ascii_letters)+word[position+1:]
    if action == 2:
        return word[:position]+word[position+1:]
    if action == 3:
        return word[:position]+random.choice(string.ascii_letters)+word[position:]

def main(max_editions):
    """Main function for edit noise generator"""
    output = open(sys.argv[3], 'w')
    actual_editions = open(sys.argv[4], 'w')
    editions = 0
    for line in open(sys.argv[2]):
        for word in line.split():
            new_word = word
            for _ in range(random.randint(0, max_editions)):
                new_word = modify(new_word)
                editions +=1
            print(new_word, end=' ', file=output)
        print(file=output)
    print(editions, file=actual_editions)

if __name__ == "__main__":
    MaxEditions = int(sys.argv[1])
    main(MaxEditions)
