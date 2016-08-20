import sys
import datetime

now = datetime.datetime.now()
busses = {"92": None, "93": None, "96": None}

stop_times_string = {
"92": ["7:30", "8:28", "8:55", "9:31", "10:16", "10:44", "11:14", "11:44", "12:14", "12:44", "13:14", "13:44", "14:14", "14:47", "15:16", "15:46", "16:16", "16:46", "17:16", "17:46", "18:16", "18:46", "19:16", "19:46", "20:16", "20:46", "21:16", "21:46", "22:16", "22:46", "23:28", "23:59"],
"93": ["6:23", "6:55", "7:25", "7:56", "8:27", "8:57", "9:27", "9:42", "9:52", "10:07", "10:22", "10:37", "10:52", "11:07", "11:22", "11:37", "11:52", "12:07", "12:22", "12:37", "12:52", "13:07", "13:22", "13:37", "13:52", "14:07", "14:22", "14:37", "14:52", "15:10", "15:23", "15:38", "15:58", "16:13", "16:28", "16:42", "16:55", "17:08", "17:19", "17:31", "17:43", "17:55", "18:06", "18:18", "18:29", "18:54", "19:24", "19:54", "20:23", "20:50", "21:20", "21:50", "22:20", "22:50", "23:20", "23:48", "0:18", "0:48"],
"96": ["3:59", "4:29", "4:59", "5:26", "5:53", "6:05", "6:13", "6:20", "6:25", "6:31", "6:38", "6:42", "6:48", "6:57", "6:58", "7:05", "7:12", "7:16", "7:18", "7:21", "7:23", "7:34", "7:37", "7:40", "7:44", "7:48", "7:52", "7:53", "7:55", "7:58", "8:04", "8:05", "8:08", "8:12", "8:16", "8:21", "8:22", "8:26", "8:35", "8:38", "8:47", "8:53", "9:00", "9:08", "9:19", "9:23", "9:35", "9:50", "10:05", "10:30", "10:58", "11:27", "11:57", "12:27", "12:57", "13:27", "13:57", "14:25", "14:36", "15:00", "15:30", "16:00", "16:30", "17:00", "17:30", "17:59", "18:29", "18:59", "19:29", "19:59", "20:29", "20:59", "21:29", "21:59", "22:29", "22:58", "23:15", "23:45", "0:15", "0:47", "1:17", "1:47", "2:17"]
}

"""usage: <arrival time> <departure time>"""
def toDayTime(num):
	return "%02d:%02d" % (int(num), round((num - int(num))*60))

def toPastTime(num):
	if int(num):
		return "%d hours, %d minutes" % (int(num), round((num - int(num))*60))
	else:
		return "%d minutes" % (round((num - int(num))*60))

def currentDate():
	return "%s/%s/%s" % (now.month, now.day, now.year)

for bus in busses.keys():
	busses[bus] = {'times': []}
	for time in stop_times_string[bus]:
		hour, minute = tuple(time.split(':'))
		busses[bus]['times'].append(int(hour) + int(minute)/60.0)

h, m = tuple(sys.argv[1].split(':'))
arrival_time = int(h) + int(m)/60.0
h, m = tuple(sys.argv[2].split(':'))
departure_time = int(h) + int(m)/60.0
assert departure_time > arrival_time


late_busses = {}
earliest_bus = ('96', 19)
for bus in busses:
	late_busses[bus] = []
	for time in busses[bus]['times']:
		if time > arrival_time and time < departure_time:
			late_busses[bus].append(time)
			if time < earliest_bus[1]:
				earliest_bus = (bus, time)

assert earliest_bus[1] > arrival_time
assert earliest_bus[1] < departure_time

excess_wait_time = departure_time - earliest_bus[1]
late_bus_count = 0
scheduled_busses = ""

for bus in busses:
	if late_busses[bus]:
		string = ""
		for time in late_busses[bus]:
			late_bus_count += 1
			string += "%s, " % toDayTime(time)
		scheduled_busses += "%s at %s\n" % (bus, string)



output = """Hello OC Transpo,

On %(date)s I waited at stop 6480 for %(extra)s longer than scheduled.

I arrived at %(start)s.
The schedule lists the following busses and times:
%(schedule)s
The bus came at %(end)s.

Therefore, %(late_count)d busses were late.

Dominik Schmidtlein
OC Transpo User
""" % {
'date': currentDate(),
'extra': toPastTime(excess_wait_time),
'start': toDayTime(arrival_time),
'end': toDayTime(departure_time),
'schedule': scheduled_busses,
'late_count': late_bus_count
}

print output

# print "%s/%s/%s" % (now.month, now.day, now.year)
# print "waited for %s" % toPastTime(excess_wait_time)
# print "%d busses were late" % late_bus_count