import pickle,glob
for filename in glob.glob('*.pkl'):
	recfile=open(filename,'rb')
	record=pickle.load(recfile)
	print(filename,'=>',record)
	recfile.close()
	
	