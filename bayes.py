class Bayes:
	def __init__(self, meta_filename, training_filename):
		self.classNames = []
		self.classes = []
		
		#Read meta file
		meta_f = open(meta_filename, "r")
		i = 0
		for line in meta_f:
			n = line.strip().split(':')

			self.classNames.append(n[0])
			self.classes.append({})

			for val in n[1].split(','):
				self.classes[i][val] = 1
			
			i += 1
		
		meta_f.close()
		

		#read training file
		train_f = open(training_filename, "r")
		for line in train_f:
			i = 0
			for val in line.strip().split(','):
				self.classes[i][val] = self.classes[i][val] + 1
				i += 1
		
		train_f.close()

def main():
	metafile = input("Enter meta file name:")
	trainingfile = input("Enter training file name:")
	b = Bayes(metafile, trainingfile)

main()