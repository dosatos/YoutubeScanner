from datetime import date, timedelta, datetime


def now():
    right_now = datetime.now()
    return right_now.strftime('%Y-%m-%dT%H:%M:%SZ')


def days_ago(days: int):
    given_days_ago = datetime.now() - timedelta(days=days)
    return given_days_ago.strftime('%Y-%m-%dT%H:%M:%SZ')


def week_ago():
    return weeks_ago(weeks_count=1)


def weeks_ago(weeks_count: int = 1):
    given_days_ago = datetime.now() - timedelta(days=7 * weeks_count)
    return given_days_ago.strftime('%Y-%m-%dT%H:%M:%SZ')
