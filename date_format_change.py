
#This function accepts date and converts it like-- 2022-06-03T01:45:44.000+00:00

def oagis_date_format(in_date_time):
    """ pass date type in this function """
    if '.' in str(in_date_time):
        date_time = str(in_date_time).split(".")[0].replace(" ", "T")
        tz_part = str(in_date_time).split(".")[1]
        if '+' in tz_part:
            date_time_str = tz_part.split("+")[0][:3]
            date_format = date_time + "." + date_time_str + "+" + tz_part.split("+")[1]
        elif '-' in tz_part:
            date_time_str = tz_part.split("-")[0][:3]
            date_format = date_time + "." + date_time_str + "-" + tz_part.split("-")[1]
        else:
            date_format = str(in_date_time)
    else:
        date_format = str(in_date_time)[:19].replace(" ", "T") + ".000" + str(in_date_time)[-6:]
    return date_format
