from datetime import date, timedelta, datetime


def now():
    today = datetime.now()
    return today.strftime('%Y-%m-%dT%H:%M:%SZ')


def yesterday():
    return days_ago(1)


def days_ago(days: int):
    yesterday = date.today() - timedelta(days=days)
    return yesterday.strftime('%Y-%m-%dT%H:%M:%SZ')


def week_ago():
    return weeks_ago(weeks_count=1)


def weeks_ago(weeks_count: int = 1):
    yesterday = date.today() - timedelta(days=7 * weeks_count)
    return yesterday.strftime('%Y-%m-%dT%H:%M:%SZ')
