from collections import ChainMap, Counter

bread = {"булочка с кунжутом": 15, "обычная булочка": 10, "ржаная булочка": 15}
meat = {"куриный бифштекс": 50, "говяжий бифштекс": 70, "рыбный бифштекс": 40}
sauce = {
    "сливочно-чесночный": 15,
    "кетчуп": 10,
    "горчица": 10,
    "барбекю": 15,
    "чили": 15,
}
vegetables = {"лук": 10, "салат": 15, "помидор": 15, "огурцы": 10}
toppings = {"сыр": 25, "яйцо": 15, "бекон": 30}

product_price = ChainMap(bread, meat, sauce, vegetables, toppings)
order = Counter(input().split(","))

# Вычислим итоговую сумму
summ = 0
for k in order:
    summ += order[k] * product_price[k]
res_output = f'ИТОГ: {summ}р'

max_cnt = max(order.values())  # Вычислим кол. единиц в заказе
max_len_word = max(map(len, order.keys())) + 3 + len(str(max_cnt))  # Максимальная длина строки

# Вывод не экран заказа
for k in sorted(order):
    space = (max_len_word - len(k) - 3 - len(str(max_cnt))) * ' ' # Вычислим, сколько нужно добавить ' '
    if space:
        print(f"{k + space} x {order[k]}")
    else:
        print(f"{k + space} x {order[k]}")

# Условие, сколько выводить символов "_"
if max_len_word < len(res_output):
    max_len_word = len(res_output)

print(max_len_word * "-")
print(res_output)
