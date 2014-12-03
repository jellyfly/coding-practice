#!/usr/bin/python

# this used package weka0.1.3: https://pypi.python.org/pypi/weka/0.1.3

from weka.classifiers import IBk

c=IBk(K=1)
c.train("train.arff")
predictions = c.predict("test.arff")
print predictions
