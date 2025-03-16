def get_num_words(string):
    return len(string.split())


def get_char_stats(string):
    stats = {}
    for word in string.split():
        for letter in list(word):
            let = letter.lower()
            if (let in stats):
                value = stats[let] + 1
            else:
                value = 1
            stats[let] = value

    return stats

