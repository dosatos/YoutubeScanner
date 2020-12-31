from datetime import date, timedelta, datetime


class RFS3339Time:
    @classmethod
    def now(cls):
        today = datetime.now()
        return today.strftime('%Y-%m-%dT%H:%M:%SZ')

    @classmethod
    def yesterday(cls):
        return cls.days_ago(1)

    @classmethod
    def days_ago(cls, days: int):
        yesterday = date.today() - timedelta(days=days)
        return yesterday.strftime('%Y-%m-%dT%H:%M:%SZ')

    @classmethod
    def week_ago(cls):
        return cls.weeks_ago(weeks_count=1)

    @classmethod
    def weeks_ago(cls, weeks_count: int = 1):
        yesterday = date.today() - timedelta(days=7 * weeks_count)
        return yesterday.strftime('%Y-%m-%dT%H:%M:%SZ')
