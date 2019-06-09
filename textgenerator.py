
import sys
import random

def main():
    dictionary = open(sys.argv[1]).readline().split()
    length = int(sys.argv[2])
    text_file = open(sys.argv[3], 'w')

    print(' '.join(random.choices(dictionary, k=length)), file=text_file)

if __name__ == "__main__":
    main()
