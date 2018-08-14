# Perceptron
Small Ai-project with Python

Custom made perceptron tries to compete with commonly known "Nearest neighbor"-algorithm. 

Training Data example: <br>
1 4 1 1 5 0 <br>
2 5 2 3 5 0 <br>
3 4 5 1 2 0 <br>

Perceptron tries then to predict the first value of the row based on the last five values.

Data without first Col: <br>
x 4 1 1 5 0 <br>
x 5 2 3 5 0 <br>
x 4 5 1 2 0 <br>


"vertigo_train.txt" is used as a training data. Each row has all values.<br>
"vertigo_predict.txt" only haves last five values<br>
"vertigo_answers.txt" has the first column, which is missing from vertigo_predict.txt<br>

Output:<br>
Perceptron: 61.34% correct<br>
Nearest neighbor: 58.76% correct<br>

Process finished with exit code 0

How to:<br>
build and run test.py
