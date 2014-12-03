from P4 import P4

p4 = P4()
p4.connect()
print (p4.connected())
#spec = p4.run("client", "o")[0]
#print (spec)
revisions = p4.run_filelog()
for r in revisions:
	print (r)
p4.disconnect()
