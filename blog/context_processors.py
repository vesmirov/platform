import datetime as dt


def dates(request):
    """Adds current year, date and weekday"""

    year = dt.datetime.now().year
    today = dt.date.today()
    yesterday = dt.datetime.today() - dt.timedelta(days=1)
    weekday = dt.date.today().strftime('%A')
    return {
        'year': year,
        'today': today,
        'yesterday': yesterday,
        'weekday': weekday,
    }
