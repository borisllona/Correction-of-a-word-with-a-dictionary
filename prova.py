import sys


def args():
    if len(sys.argv) > 2:
        inputfile = open("dictionary.txt", "r")  # sys.stdout
        inputfile2 = open("text_amb_errors.txt", "r")  # sys.stdin
        outputfile = open("text_corretgit.txt", "w")  # sys.stdout
        outputfile2 = open("nombre_edicions.txt", "w")  # sys.stdout


if __name__ == "__main__":
    args()
