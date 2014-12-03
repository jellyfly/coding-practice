from P4 import P4

p4 = P4()
p4.user = os.environ.get('P4USER')
p4.password = os.environ.get('P4PASSWORD')
p4.port = os.environ.get('P4PORT')
p4.connect()
p4.run_login()
for i in range(0, 10000000):
	print(p4.connected())
p4.disconnect()
