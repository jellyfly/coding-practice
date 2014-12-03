#/usr/bin/python
# use python-weka-wrapper

import weka.core.jvm as jvm
jvm.start(system_cp=True, packages=True)
jvm.start(max_heap_size="521m")

from weka.core.converters import Loader

loader = Loader(classname = "weka.core.converters.ArffLoader")
data = loader.load_file("train.arff")
print data

jvm.stop()
