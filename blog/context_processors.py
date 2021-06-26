import datetime as dt


def today(request):
    """Adds current year, date and weekday"""

    year = dt.datetime.now().year
    date = dt.date.today().strftime('%d %B %Y')
    weekday = dt.date.today().strftime('%A')
    return {'year': year, 'date': date, 'weekday': weekday}
