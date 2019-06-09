# corrector.py
import re
import sys
import difflib

dictionary = []
original = []
number = []
corrected = []


def args():

    global original,dictionary,corrected,number
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


def compare(text_list, dictionary_list):

    global number, corrected
    new_text = ''

    total_differences = 0

    for i in text_list:
        pos = 0
        differences = []
        i = i.strip()
        for j in dictionary_list:
            j = j.strip()
            # afegim per cada paraula del diccionari
            differences.append(0)
            # funcio de la llibreria difflib que dona les lletres que son iguals
            s = difflib.SequenceMatcher()
            s.set_seqs(i, j)
            # guardem les diferencies per en array
            differences[pos] = diff(s, len(i), len(j))
            pos += 1
        # busquem les diferencia mínima
        min_differences = min(differences)
        # Acumules diferencies minimes en tot el text
        total_differences += min_differences

        if new_text != '':
            new_text += ' '
        # trobem la primera paraula amb el minim de diferencies
        new_text += dictionary_list[differences.index(min_differences)]

        differences.clear()
    # guardem a fitxers
    number.write(str(total_differences))
    corrected.write(new_text)


def diff(s, lena, lenb):
    # funcio de la llibreria py que ens dona lletres iguals
    matches = sum(triple[-1] for triple in s.get_matching_blocks())
    # calcules les diferencies.
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
