from P4 import P4
p4 = P4()
p4.connect()
print (p4.connected())
p4.disconnect()
print (p4.connected())
