import sys
import datetime
input = sys.stdin.readline

given_time = input().strip()
alarm_time = datetime.datetime.strptime(given_time,'%H %M')-datetime.timedelta(minutes = 45)

print(datetime.datetime.strftime(alarm_time, '%-H %-M'))

