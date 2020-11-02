class Bayes:
	def __init__(self, meta_filename, training_filename):
		self.attributes = [] #the classifications are the last item in self.attributes
		self.counts = [] #counts is accessed in this format: self.counts[column][classification][attribute]
		self.classification_count = {}
		
		#Read meta file
		meta_f = open(meta_filename, "r")
		i = 0
		for line in meta_f:
			n = line.strip().split(':')#attribute name is n[0]

			self.attributes.append(set())

			for val in n[1].split(','):
				self.attributes[i].add(val)
			
			i += 1
		
		meta_f.close()


		#initialize counts
		i = 0
		for attr in self.attributes[:-1]:
			self.counts.append({})
			for classif in self.attributes[-1]:
				self.counts[i][classif] = {}

				for attr in self.attributes[i]:
					self.counts[i][classif][attr] = 1

			i += 1
		
		for c in self.attributes[-1]:
			self.classification_count[c] = 1


		#read training file into counts
		train_f = open(training_filename, "r")
		for line in train_f:
			i = 0
			formatted_line = line.strip().split(',')
			for val in formatted_line[:-1]:
				classification = formatted_line[-1]
				self.counts[i][classification][val] = self.counts[i][classification][val] + 1
				i += 1
			
			self.classification_count[formatted_line[-1]] = self.classification_count[formatted_line[-1]] + 1
		
		train_f.close()

		#change counts from raw number to fraction
		for col in self.counts:
			for classif in col:
				total = 0
				for attr in col[classif]:
					total += col[classif][attr]

				for attr in col[classif]:
					col[classif][attr] = col[classif][attr]/total
		
		total = 0
		for v in self.classification_count.values():
			total += v
		
		for c in self.classification_count:
			self.classification_count[c] = self.classification_count[c]/total
		
		print(self.classification_count)

	
	def classifyFile(self, infile_name, outfile_name):
		pass


	def calculateAccuracy(self, filename):
		pass




def main():
	running = True

	metafile = input("Enter meta file name:")
	trainingfile = input("Enter training file name:")
	b = Bayes(metafile, trainingfile)

	while running:
		choice = input("\n\n1 to train.\n2 to classify a file.\n3 to calculate accuracy.\n4 to exit\nEnter choice: ")

		if choice == "1":
			metafile = input("Enter meta file name:")
			trainingfile = input("Enter training file name:")
			b = Bayes(metafile, trainingfile)
		
		elif choice == "2":
			infile = input("Enter test file name:")
			outfile = input("Enter output file name:")
			b.classifyFile(infile, outfile)
		
		elif choice == "3":
			infile = input("Enter test file name:")
			b.calculateAccuracy(infile)
		
		elif choice == "4":
			running = False

main()