from datetime import date


def valid_data(data):
    try:
        y, m, d = data
        dt = date(y, m, d)
        return True
    except:
        return False


birth_dates = ['2020-09-41', '2020-0918', '202009-18', '2020-9-18', '2020-41-09']

for d in birth_dates:
    res = valid_data(d)
    print(res)