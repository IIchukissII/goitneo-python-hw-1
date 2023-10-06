import datetime


def get_birthdays_per_week(data):
    current_date = datetime.date.today()
    people_with_birthday_next_week = []
    people_with_birthday_next_week_dict = {}
    message = ''

    for person in data:
        person_birthday = person["birthday"]
        birthday_this_year = person_birthday.replace(year=current_date.year)

        if birthday_this_year < current_date:
            birthday_this_year = person_birthday.replace(
                year=current_date.year + 1)

        delta_weeks = (birthday_this_year - current_date).days // 7

        if delta_weeks == 0 and (birthday_this_year.strftime('%A') == 'Saturday' or birthday_this_year.strftime('%A') == 'Sunday'):
            people_with_birthday_next_week.append(["Monday", person['name']])
        elif delta_weeks == 1 and not (birthday_this_year.strftime('%A') == 'Saturday' or birthday_this_year.strftime('%A') == 'Sunday'):
            people_with_birthday_next_week.append(
                [birthday_this_year.strftime('%A'), person['name']])

    for people in people_with_birthday_next_week:
        day = people[0]
        if day not in people_with_birthday_next_week_dict:
            people_with_birthday_next_week_dict[day] = []
        people_with_birthday_next_week_dict[day].append(people[1])

#    message += "{:>15}: {:<}\n".format('Day of week', 'Name')
    for key, value in people_with_birthday_next_week_dict.items():
        message += "{:>15}: {:<}\n".format(key, ', '.join(value))

    return message
