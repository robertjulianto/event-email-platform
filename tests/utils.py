from datetime import datetime


def convert_str_to_datetime(dt_string):
    return datetime.strptime(dt_string, "%B %d, %Y %H:%M%p %z")
