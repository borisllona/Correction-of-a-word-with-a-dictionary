# corrector.py
import re
import sys
import difflib

dictionary = []
original = []
number = []
corrected = []


def args():
    global original, dictionary, corrected, number
    if len(sys.argv) > 4:
        dictionary = open(str(sys.argv[1]), "r", encoding="utf-8")
        original = open(str(sys.argv[2]), "r", encoding="utf-8")
        corrected = open(str(sys.argv[3]), "w", encoding="utf-8")
        number = open(str(sys.argv[4]), "w", encoding="utf-8")
    else:
        dictionary = sys.stdin
        original = sys.stdin
        corrected = sys.stdout
        number = sys.stdout


def compare(textList, dictList):
    global number, corrected
    new_text = ''
    total_differences = 0

    if len(textList) == 0:
        return 0

    i = textList[0].strip()
    pos = 0
    differences = []

    add_differences(dictList, differences, i, pos)

    min_differences = min(differences)
    total_differences += min_differences

    if new_text != '':
        new_text += ' '

    new_text += dictList[differences.index(min_differences)]

    differences.clear()
    compare(textList[1:], dictList)

    number.write(str(total_differences))
    corrected.write(new_text)


def add_differences(dictList, differences, i, pos):
    if len(dictList) == 0:
        return 0

    j = dictList[0].strip()
    differences.append(0)
    s = difflib.SequenceMatcher()
    s.set_seqs(i, j)

    differences[pos] = diff(s, len(i), len(j))
    pos += 1

    return add_differences(dictList[1:], differences, i, pos)


def diff(s, lena, lenb):
    matches = sum(triple[-1] for triple in s.get_matching_blocks())
    if lena == lenb:
        return lena - matches

    if lena > lenb:
        return lena - matches
    else:
        return lenb - matches


if __name__ == "__main__":
    args()

    diccionari = ''.join(dictionary)
    original = ''.join(original)

    text = re.split("\s", original)
    text = list(filter(None, text))

    dict = re.split("\s", diccionari)

    compare(text, dict)
