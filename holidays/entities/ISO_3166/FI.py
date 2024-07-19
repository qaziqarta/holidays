#  holidays
#  --------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Authors: Vacanza Team and individual contributors (see AUTHORS file)
#           dr-prodigy <dr.prodigy.github@gmail.com> (c) 2017-2023
#           ryanss <ryanssdev@icloud.com> (c) 2014-2017
#  Website: https://github.com/vacanza/python-holidays
#  License: MIT (see LICENSE file)

"""
References:
    - https://en.wikipedia.org/wiki/Public_holidays_in_Finland
"""

from gettext import gettext as tr

from holidays.calendars.gregorian import _timedelta
from holidays.entities.ISO_3166 import Iso3166Entity
from holidays.groups import ChristianHolidays, InternationalHolidays
from holidays.holiday_base import HolidayBase


class FiHolidays(HolidayBase, Iso3166Entity, ChristianHolidays, InternationalHolidays):
    """A class to represent holidays for Finland."""

    code = "FI"
    name = "Finland"
    default_language = "fi"
    supported_languages = ("en_US", "fi", "sv", "uk")

    def __init__(self, *args, **kwargs):
        ChristianHolidays.__init__(self)
        InternationalHolidays.__init__(self)
        super().__init__(*args, **kwargs)

    def _populate_public_holidays(self):
        # New Year's Day.
        self._add_new_years_day(tr("Uudenvuodenpäivä"))

        # Epiphany.
        name = tr("Loppiainen")
        if 1973 <= self._year <= 1990:
            self._add_holiday_1st_sat_from_jan_6(name)
        else:
            self._add_epiphany_day(name)

        # Good Friday.
        self._add_good_friday(tr("Pitkäperjantai"))

        # Easter Sunday.
        self._add_easter_sunday(tr("Pääsiäispäivä"))

        # Easter Monday.
        self._add_easter_monday(tr("2. pääsiäispäivä"))

        # May Day.
        self._add_holiday_may_1(tr("Vappu"))

        # Ascension Day.
        name = tr("Helatorstai")
        if 1973 <= self._year <= 1990:
            self._add_holiday_34_days_past_easter(name)
        else:
            self._add_ascension_thursday(name)

        # Whit Sunday.
        self._add_whit_sunday(tr("Helluntaipäivä"))

        # Midsummer Eve.
        name = tr("Juhannusaatto")
        if self._year >= 1955:
            dt = self._add_holiday_1st_fri_from_jun_19(name)
        else:
            dt = self._add_holiday_jun_23(name)

        # Midsummer Day.
        self._add_holiday(tr("Juhannuspäivä"), _timedelta(dt, +1))

        # All Saints' Day.
        name = tr("Pyhäinpäivä")
        if self._year >= 1955:
            self._add_holiday_1st_sat_from_oct_31(name)
        else:
            self._add_holiday_nov_1(name)

        # Independence Day.
        self._add_holiday_dec_6(tr("Itsenäisyyspäivä"))

        # Christmas Eve.
        self._add_christmas_eve(tr("Jouluaatto"))

        # Christmas Day.
        self._add_christmas_day(tr("Joulupäivä"))

        # Second Day of Christmas.
        self._add_christmas_day_two(tr("Tapaninpäivä"))
