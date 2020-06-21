import time
import datetime
import pytz

#
# print('The epoch on this system starts at ' + time.strftime('%c', time.gmtime(0)))
#
# print('The current timeZone is {0} with an offset of {1}'.format(time.tzname[0], time.timezone))
#
# if time.daylight != 0:
#     print('\tDatylight Saving Time is in effect for this location')
#     print('\tThe DST timezone is ' + time.tzname[1])
#
# print('Local time is ' + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
# print('UTC time is ' + time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime()))

# print(datetime.datetime.today())
# print(datetime.datetime.now())  # it is much better then .today
# print(datetime.datetime.utcnow())  # if you are in uk all times are equal

country = 'Europe/Moscow'
tz_to_display = pytz.timezone(country)
local_time = datetime.datetime.now(tz=tz_to_display)
print('The time in {} is {}'.format(country, local_time))
print('UTC is {}'.format(datetime.datetime.utcnow()))


for x in pytz.all_timezones:
    print(x)

for x in sorted(pytz.country_names):
    print(x + ' : ' + pytz.country_names[x])

for x in sorted(pytz.country_names):
    print(f'{x} : {pytz.country_names[x]} : {pytz.common_timezones}')
