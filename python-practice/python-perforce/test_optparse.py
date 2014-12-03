import argparse

def main():
	parser = argparse.ArgumentParser()

	parser.add_argument('-s', action='store', dest='simple_value',
		                help='Store a simple value')

	parser.add_argument('-c', action='store_const', dest='constant_value',
		                const='value-to-store',
		                help='Store a constant value')

	parser.add_argument('-t', action='store_true', default=False,
		                dest='boolean_switch',
		                help='Set a switch to true')
	parser.add_argument('-f', action='store_false', default=False,
		                dest='boolean_switch',
		                help='Set a switch to false')

	parser.add_argument('-a', action='append', dest='collection',
		                default=[],
		                help='Add repeated values to a list',
		                )

	parser.add_argument('-A', action='append_const', dest='const_collection',
		                const='value-1-to-append',
		                default=[],
		                help='Add different values to list')
	parser.add_argument('-B', action='append_const', dest='const_collection',
		                const='value-2-to-append',
		                help='Add different values to list')

	parser.add_argument('--version', action='version', version='%(prog)s 1.0')

	results = parser.parse_args()
	print ('simple_value     =', results.simple_value)
	print ('constant_value   =', results.constant_value)
	print ('boolean_switch   =', results.boolean_switch)
	print ('collection       =', results.collection)
	print ('const_collection =', results.const_collection)


if __name__ == "__main__":
    main()


    import configparser
from optparse import OptionParser

CONFIG_FILENAME = 'defaults.cfg'

def main():
    config = configparser.ConfigParser()
    config.read(CONFIG_FILENAME)

    parser = OptionParser()
    parser.add_option("-s",
                      "--startime",
                      dest="start_time",
                      help="The UI language",
                      default=config.get("Localization", "language"))
    parser.add_option("-e",
                      "--endtime",
                      dest="end_time",
                      help="The country flag",
                      default=config.get("Localization", "flag"))

    print (parser.parse_args())

    args = parser.parse_args()
    for arg in args:
    	if arg:
    		for arsg in arg:
		    	print(arsg)



if __name__ == "__main__":
    main()


    import argparse

class CustomAction(argparse.Action):
    def __init__(self,
                 option_strings,
                 dest,
                 nargs=None,
                 const=None,
                 default=None,
                 type=None,
                 choices=None,
                 required=False,
                 help=None,
                 metavar=None):
        argparse.Action.__init__(self,
                                 option_strings=option_strings,
                                 dest=dest,
                                 nargs=nargs,
                                 const=const,
                                 default=default,
                                 type=type,
                                 choices=choices,
                                 required=required,
                                 help=help,
                                 metavar=metavar,
                                 )
        print
        print ('Initializing CustomAction')
        for name,value in sorted(locals().items()):
            if name == 'self' or value is None:
                continue
            print ('  %s = %r' % (name, value))
        return

    def __call__(self, parser, namespace, values, option_string=None):
        print
        print ('Processing CustomAction for "%s"' % self.dest)
        print ('  parser = %s' % id(parser))
        print ('  values = %r' % values)
        print ('  option_string = %r' % option_string)
        
        # Do some arbitrary processing of the input values
        if isinstance(values, list):
            values = [ v.upper() for v in values ]
        else:
            values = values.upper()
        # Save the results in the namespace using the destination
        # variable given to our constructor.
        setattr(namespace, self.dest, values)

parser = argparse.ArgumentParser()

parser.add_argument('-a', action=CustomAction)
parser.add_argument('-m', nargs='*', action=CustomAction)
parser.add_argument('positional', action=CustomAction)

results = parser.parse_args(['-a', 'value', '-m' 'multi-value', 'positional-value'])
print
print (results)
