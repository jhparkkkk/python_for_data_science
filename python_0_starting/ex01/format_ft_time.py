import time
from datetime import datetime

timestamp = time.time()
formattedTime = "{:,.4f}".format(timestamp)
scientificTime = "{:,.2e}".format(timestamp)
currentTime = time.localtime(timestamp)
date = datetime(
    year=currentTime.tm_year, month=currentTime.tm_mon, day=currentTime.tm_mday
)
formatted_month = date.strftime("%b")

print(
    "Seconds since January 1, 1970: "
    + formattedTime
    + " or "
    + scientificTime
    + " in scientific notation\n"
    + formatted_month
    + " "
    + format(currentTime.tm_mday)
    + " "
    + format(currentTime.tm_year)
)
