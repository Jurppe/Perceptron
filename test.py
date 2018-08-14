import numpy as np
from sklearn.linear_model import perceptron
from sklearn.metrics import confusion_matrix
from sklearn.neighbors import KNeighborsClassifier

# Load text data form the file
train_data = np.loadtxt("vertigo_train.txt", dtype=int)
test_data = np.loadtxt("vertigo_predict.txt", dtype=int)
true_class = np.loadtxt("vertigo_answers.txt", dtype=int)

train_class = train_data[:,0]
train_data = np.delete(train_data, 1, 1)

p = perceptron.Perceptron()
perceptron_trained = p.fit(train_data, train_class)

test_result_perceptron = perceptron_trained.predict(test_data)

# confusion matrix
cm =confusion_matrix(true_class,test_result_perceptron)
accuracy_perceptron = sum(np.diag(cm))/len(true_class)*100

neigh = KNeighborsClassifier(metric="manhattan")
nn_fitted = neigh.fit(train_data, train_class)

nn_predict = nn_fitted.predict(test_data)
confu_mat_nn = confusion_matrix(true_class, nn_predict)

## calculating accuracy
accuracy_nn = sum(np.diag(confu_mat_nn))/len(true_class)*100
print("Perceptron: {0:.2f}% correct".format(accuracy_perceptron))
print("Nearest neighbor: {0:.2f}% correct".format(accuracy_nn))