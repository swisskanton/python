"""
https://www.olympiad.org.uk/papers/2004/bio/q1.html

The Mayan civilisation used three different calendars. In their long count calendar there were
20 days (called kins) in a uinal, 18 uinals in a tun, 20 tuns in a katun and 20 katuns in a baktun.
In our calendar, we specify a date by giving the day, then month, and finally the year.
The Maya specified dates in reverse, giving the
    baktun (1-20), then
    katun (1-20), then
    tun (1-20), then
    uinal (1-18) and finally the
    kin (1-20).

The Mayan date 13 20 7 16 3 corresponds to the date 1 January 2000 (which was a Saturday).

Write a program which, given a Mayan date (between 13 20 7 16 3 and 14 1 15 12 3 inclusive),
outputs the corresponding date in our calendar. You should output the month as a number.

Example:
13 20 9 2 9  # Mayan date 22 March 2001
22 3 2001    # Gregorian date 22 March 2001
"""
from datetime import datetime, timedelta


def convert_mayan(date):
    baktun, katun, tun, uinal, kin = [int(x) for x in date.split()]
    base_days = get_days(13, 20, 7, 16, 3)
    current_days = get_days(baktun, katun, tun, uinal, kin)
    ini_time = datetime(2000, 1, 1)
    d = ini_time + timedelta(days=current_days - base_days)
    return f'{d.day} {d.month} {d.year}'


def get_days(baktun, katun, tun, uinal, kin):
    return kin + 20 * uinal + 18*20 * tun + 20*18*20 * katun + 20*20*18*20 * baktun


if __name__ == '__main__':
    print(convert_mayan("13 20 9 2 9"), ">> 22 3 2001")
    print(convert_mayan("13 20 7 16 3"), ">> 1 1 2000")
