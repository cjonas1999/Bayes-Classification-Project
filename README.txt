We wrote our Naive Bayes Classifier in python. Contained in bayes.py is the class Bayes.
The constructor reads the meta and training files, and constructs the lookup tables based on the training data.

The bestprobability function reads the probabily of each classification with the given label and finds the best overall probability to select the class needed to be assigned

the function (classifyFile) starts off by getting the test file name and output file name. Within the function, it reads the test file and copys all of its contents in the same format as the training file except for the classification at the end of each line if one exists onto the output file. The function also calls bestprobability to calculate the classification for the given lines. The classification is added right after the content in each line.

calculateAccuracy() reads the input file and tracks the number of correct to incorrect according to the model, and returns the % correct as a decimal from 0 to 1. 

To run the code, simply run bayes.py and follow the prompts. It will initially ask for a meta and training file, as none of the other functions can be used without them. After, you can enter '1' to train with new data, '2' to classify a file, '3' to calculate the accuracy of a file, or '4' to exit.