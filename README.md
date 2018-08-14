# Perceptron
Small Ai-project with Python

Custom made perceptron tries to compete with commonly known "Nearest neighbor"-algorithm. 

Training Data example:
1 4 1 1 5 0
2 5 2 3 5 0
3 4 5 1 2 0

Perceptron tries then to predict the first value of the row based on the last five values.

Data without first Col:
x 4 1 1 5 0
x 5 2 3 5 0
x 4 5 1 2 0


"vertigo_train.txt" is used as a training data. Each row has all values.
"vertigo_predict.txt" only haves last five values
"vertigo_answers.txt" has the first column, which is missing from vertigo_predict.txt

Output:
Perceptron: 61.34% correct
Nearest neighbor: 58.76% correct

Process finished with exit code 0

How to:
build and run test.py
