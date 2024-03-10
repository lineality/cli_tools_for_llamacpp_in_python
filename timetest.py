import datetime, calendar, time
from datetime import date, datetime, UTC


year = 2021
month = 12
day = 14


Sample_Time = datetime(year,month,day)


print("Staring with Normal Time")
print(Sample_Time)
print(type(Sample_Time))


# Current Time UTC
# from datetime import datetime, UTC
date_time = datetime.now(UTC)
