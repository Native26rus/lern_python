from collections import Counter


def print_bar_chart(data, mark):
    counter = Counter()

    if type(data) == list:
        for w in data:
            counter.update([w])
        max_len = max(map(len, counter))

        for l, n in counter.most_common():
            print(f'{l.ljust(max_len)} |{mark * n}')

    else:
        counter = Counter(data)
        for l, n in counter.most_common():
            print(f'{l} |{mark * n}')
