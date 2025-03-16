from stats import get_num_words, get_char_stats
import sys

def getTextFromBook(path):
    with open(path) as f:
        return f.read()


def sort_on(dict):
    return dict["num"]

def print_report(path):
    bookText = getTextFromBook(path)
    amount = get_num_words(bookText)
    stats = get_char_stats(bookText)

    sortedStats = reversed(
        sorted(stats.items(), key=lambda kv: (kv[1], kv[0])))

    print(stats)
    print('============ BOOKBOT ============')
    print('Analyzing book found at', path, '...')
    print('----------- Word Count ----------')
    print('Found', amount, 'total words')
    print('--------- Character Count -------')

    for key, value in sortedStats:
        if isinstance(key, str) and not key.isalpha():
            continue
        text = key + ': ' + str(value)
        print(text)

    print('============= END ===============')

def main():
    if (len(sys.argv) < 2):
        print('Usage: python3 main.py <path_to_book>')
        sys.exit(1)

    print_report(sys.argv[1])
    sys.exit(0)


main()
