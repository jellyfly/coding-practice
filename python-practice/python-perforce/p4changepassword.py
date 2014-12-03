from P4 import P4
p4 = P4()
p4.user = "mintan2"
p4.password = "cisco123$"
p4.connect()

p4.run_password("cisco123$", "cisco123")
p4.disconnect()
