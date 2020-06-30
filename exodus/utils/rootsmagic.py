import calendar

from .. import YEAR_AD_CUTOFF

def read_date_str(rootsmagic_date):
    """
    Read a date as provided in the RootsMagic format.

    - "." for unset
    - "D[R.]+YYYYMMDD.[CA.]00000000.."
        - "R" is for a range, where the second set of digits is the end of the range,
          and set to "00000000" otherwise
        - where the "+" likely means AD ("-" for BC dates?)
        - MM and DD can be set to "00" for incomplete dates, with "A" for years
          and "C" for months (but "A" and "C" is not used for date ranges)
            - "C" and "A" may also be for "estimated", "calculated", "circa", etc...?
    """
    if rootsmagic_date[0] == '.' and len(rootsmagic_date) == 1:
        return None
    elif rootsmagic_date[0] != 'D':
        raise ValueError('RootsMagic dates must start with "D"')

    if rootsmagic_date[1] == 'R':
        is_range = True
    else:
        is_range = False

    if rootsmagic_date[13] in ["A", "C"]:
        flag = rootsmagic_date[13]
    else:
        flag = None

    raw_dates = [rootsmagic_date[2:13], rootsmagic_date[13:24]]
    dates = []

    for raw in raw_dates:
        if raw[0] == "+":
            is_ad = True
        else:
            raise ValueError(f'Unknown sign in {raw}')

        year = int(raw[1:5])
        month = int(raw[5:7])
        day = int(raw[7:9])
        # not sure what the last two digits mean...

        processed = {
            'year': year,
            'month': month or None,
            'day': day or None,
            'ad': is_ad,
            'range': is_range,
            'flag': flag,
        }
        dates.append(processed)
    return dates


def pprint_date(dates):
    print(dates)
    # TODO: deal with date flags...
    if dates is None:
        return '-'
    
    return_str = ''
    date_parts = []
    for date in dates:
        this_date_parts = []
        if date['day']:
            this_date_parts.append(str(date['day']))
        if date['month']:
            # TODO: "Sept" vs "Sep"
            this_date_parts.append(calendar.month_abbr[date['month']])
        if date['year']:
            this_date_parts.append(str(date['year']))
            if 0 < date['year'] <= YEAR_AD_CUTOFF and date['ad']:
                this_date_parts.append("AD")

        if this_date_parts:
            date_parts.append(" ".join(this_date_parts))

    return " - ".join(date_parts)

def read_and_pprint_date(rootsmagic_date):
    return pprint_date(read_date_str(rootsmagic_date))
