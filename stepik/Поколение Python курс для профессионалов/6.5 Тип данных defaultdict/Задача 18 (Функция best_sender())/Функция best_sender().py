from collections import defaultdict


def best_sender(messages: list, senders: list):
    d = defaultdict(int)
    # Получим словарь имя: количество слов в сообщениях
    for text, name in zip(messages, senders):
        d[name] += len(text.split())
    # Получим цифру с мак. кол. слов в сообщениях
    max_len = d[max(d, key=lambda x: d[x])]
    # Сделаем фильтр по значениям с мас. кол. слов
    res = list(filter(lambda x: d[x] == max_len, d))
    return sorted(res)[-1]

