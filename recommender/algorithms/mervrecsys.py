from recsys.algorithm.factorize import SVD

def generate(filename):
	print 'generating'
	svd = SVD()
	svd.load_data(filename=filename, sep='::',
	       format={'col':0, 'row':1, 'value':2, 'ids': int})

