import re
import sys

pattern = 'Fred'
pattern = '\\ in'
pattern = r'\\ in'
pattern = r'''
^ 
RUN\ 
\d{6} 
\ COMPLETED\.\ OUTPUT\ IN\ FILE\ 
[a-z]+\.dat 
\. 
$ 
'''
# regexp = re.compile(pattern)
regexp = re.compile(pattern, re.IGNORECASE)
for line in sys.stdin:
	match = regexp.search(line)
	if match:
		sys.stdout.write(line)


