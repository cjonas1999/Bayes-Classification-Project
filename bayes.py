class Bayes:
	def __init__(self, meta_filename, training_filename):
		self.attributes = [] #the classifications are the last item in self.attributes
		self.counts = [] #counts is accessed in this format: self.counts[column][classification][attribute]
		
		#Read meta file
		meta_f = open(meta_filename, "r")
		i = 0
		for line in meta_f:
			n = line.strip().split(':')

			self.attributes.append({})
			self.attributes[i][n[0]] = set()

			for val in n[1].split(','):
				self.attributes[i][n[0]].add(val)
			
			i += 1
		
		meta_f.close()


		#initialize counts
		i = 0
		for attr in self.attributes[:-1]:
			self.counts.append({})
			for classif in self.attributes[-1].values():
				for v in classif:
					self.counts[i][v] = {}

					for c in self.attributes[i].values():
						for attr in c:
							self.counts[i][v][attr] = 0

			i += 1


		#read training file into counts
		train_f = open(training_filename, "r")
		for line in train_f:
			i = 0
			formatted_line = line.strip().split(',')
			for val in formatted_line[:-1]:
				classification = formatted_line[-1]
				self.counts[i][classification][val] = self.counts[i][classification][val] + 1
				i += 1
		
		train_f.close()
	
	
	def classifyFile(self, infile_name, outfile_name):
		pass


	def calculateAccuracy(self, filename):
		pass




def main():
	metafile = input("Enter meta file name:")
	trainingfile = input("Enter training file name:")
	b = Bayes(metafile, trainingfile)

main()