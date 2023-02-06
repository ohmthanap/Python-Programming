# Thanapoom Phatthanaphan
# This is the program to count word frequency in a specific file.
# The program will rearrange the word in a file and count the number of each word,
# then the program will sort by alphabetical and word frequency.

def by_freq(pair):
    return pair[1]


def main():
    print("This program analyzes word frequency in a file")
    print("and prints a report on the n most frequent words.\n")

    # get the sequence of words from the file
    file_name = input("File to analyze: ")
    text = open(file_name, 'r').read()
    text = text.lower()
    for ch in '!"#$%&()*+,-./:;<=>?@[\\]^_`{|}~':
        text = text.replace(ch, ' ')
    words = text.split()    # replace every special characters with space

    # construct a dictionary of word counts
    counts = {}
    for w in words:
        # to count the number of words and add it in the dictionary
        counts[w] = counts.get(w, 0) + 1

    # output analysis of n most frequent words.
    items = list(counts.items())
    items.sort()    # sort by words
    items.sort(key=by_freq, reverse=True)    # sort by frequency
    for i in range(len(items)):
        word, count = items[i]
        print("{0:<15}{1:>5}".format(word, count))


if __name__ == '__main__':
    main()
