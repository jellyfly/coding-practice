import os
import tempfile
import weka.core.jvm as jvm
import weka.core.converters as converters
#import weka.examples.helper as helper
from weka.classifiers import Classifier
from weka.experiments import SimpleCrossValidationExperiment, SimpleRandomSplitExperiment, Tester, ResultMatrix


def main():
	"""
	    Just runs some example code.
	"""

#	print(helper.get_data_dir())


	# cross-validation + classification
#	helper.print_title("Experiment: Cross-validation + classification")
	#datasets = [helper.get_data_dir() + os.sep + "iris.arff", helper.get_data_dir() + os.sep + "anneal.arff"]
	datasets = ["train.arff", "test.arff"]
	classifiers = [ Classifier("weka.classifiers.trees.J48")]
	outfile = tempfile.gettempdir() + os.sep + "results-cv.arff"
	exp = SimpleCrossValidationExperiment(
		classification=True,
		runs=10,
		folds=10,
		datasets=datasets,
		classifiers=classifiers,
		result=outfile
	)
	exp.setup()
	exp.run()
	# evaluate
	loader = converters.loader_for_file(outfile)
	data = loader.load_file(outfile)
	matrix = ResultMatrix("weka.experiment.ResultMatrixPlainText")
	tester = Tester("weka.experiment.PairedCorrectedTTester")
	tester.set_resultmatrix(matrix)
	comparison_col = data.get_attribute_by_name("Percent_correct").get_index()
	tester.set_instances(data)
	print(tester.header(comparison_col))
	print(tester.multi_resultset_full(0, comparison_col))

	# random split + regression
#	helper.print_title("Experiment: Random split + regression")

	# evaluate
	loader = converters.loader_for_file(outfile)
	data = loader.load_file(outfile)
	matrix = ResultMatrix("weka.experiment.ResultMatrixPlainText")
	tester = Tester("weka.experiment.PairedCorrectedTTester")
	tester.set_resultmatrix(matrix)
	comparison_col = data.get_attribute_by_name("Correlation_coefficient").get_index()
	tester.set_instances(data)
	print(tester.header(comparison_col))
	print(tester.multi_resultset_full(0, comparison_col))

if __name__ == "__main__":
	try:
		jvm.start(system_cp=True, packages = True)
		main()
	except Exception, e:
		print(e)
	finally:
		jvm.stop()
