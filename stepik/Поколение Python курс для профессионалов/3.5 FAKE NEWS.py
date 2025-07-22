from datetime import datetime

def format_datetime_with_cases(id: int, num: int):
    plural_dict = {0: ("день", "дня", "дней"), 1: ("час", "часа", "часов"), 2: ("минута", "минуты", "минут")}

    if num % 10 == 1 and num != 11:
        return plural_dict[id][0]
    elif num % 10 in (2, 3, 4) and num % 100 not in (12, 212):
        return plural_dict[id][1]
    else:
        return plural_dict[id][2]

start_course = datetime(2022, 11, 8, 12)
current_dt = datetime.strptime(input(), '%d.%m.%Y %H:%M')
delta = start_course - current_dt
day, hour, minute = delta.days, int(delta.seconds / 3600), int((delta.seconds / 60) % 60)

if delta.total_seconds() <= 0:
    print('Курс уже вышел!')
elif day and minute:
    print(f'До выхода курса осталось: {day} {format_datetime_with_cases(0, day)} и'
          f' {hour} {format_datetime_with_cases(1, hour)}')
elif day and not minute:
    print(f'До выхода курса осталось: {day} {format_datetime_with_cases(0, day)}')
elif not day and hour and minute:
    print(f'До выхода курса осталось: {hour} {format_datetime_with_cases(1, hour)} и'
          f' {minute} {format_datetime_with_cases(2, minute)}')
elif not day and not minute and hour:
    print(f'До выхода курса осталось: {hour} {format_datetime_with_cases(1, hour)}')
elif not day and minute and not hour:
    print(f'До выхода курса осталось: {minute} {format_datetime_with_cases(2, minute)}')