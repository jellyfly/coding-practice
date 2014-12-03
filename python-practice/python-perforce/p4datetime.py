from P4 import P4
from datetime import datetime#, timedelta

p4 = P4()
p4.user = 'mintan2'
p4.password = 'cisco123$'
p4.connect()
p4.run_login()
# change_info = p4.run_describe(534576)
change_info = p4.run('describe', '-dsw', 534576)
print (change_info)
#description = change_info[0]['desc']
#print(description)
myDate = datetime.utcfromtimestamp(int(change_info[0]['time']))
# myDate = datetime.fromtimestamp(int(change_info[0]['time']))
# myDate = datetime.now()
h = myDate.hour + myDate.minute / 60. + myDate.second / 3600.
h = myDate.hour
d = myDate.weekday()
print (myDate, h, d)
p4.disconnect()
