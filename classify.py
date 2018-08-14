from sklearn import linear_model as sl
import math
import operator
import warnings

# perceptron throws some warnings if used without proper params
# lets just ignore them
warnings.filterwarnings('ignore')

# just reading files,
# param training_data: used for divining training data in two different lists
# param answers: used for reading only aswers from file
def read_vertigo(filename, training_data=False, answers=False):
    table = []
    with open(filename, 'r') as infile:
        if answers:
            for line in infile:
                for number in line.split():
                    table.append(int(number))
            return table
        else:
            if not training_data:
                for line in infile:
                    subset = []
                    for number in line.split():
                        subset.append(int(number))
                    table.append(subset)
                return table
            else:
                answers = []
                for line in infile:
                    subset = []
                    first = True
                    for number in line.split():
                        if first:
                            answers.append(int(number))
                            first = False
                        else:
                            subset.append(int(number))
                    table.append(subset)
            return table, answers


# sums up correct answers and prints success percentage
# ***** DESIGNED ONLY FOR PERCEPTRON *****
def correctness(table1, table2):
    correct = 0
    for i in range(0, len(table1)):
        if table1[i] == table2[i]:
            correct += 1
    print('Success percentage: {0:.2f}%'.format(correct / len(table1) * 100))


# tests perceptron
def test_perceptron(param=0):
    training_data, training_answers = read_vertigo('vertigo_train.txt', True)

    # Creating the PERCEP-O-TRON
    if param:
        p = sl.Perceptron(n_iter=param)
    else:
        p = sl.Perceptron()
    # Train
    p.fit(training_data, training_answers)

    # Compete
    training_data = read_vertigo('vertigo_predict.txt')
    answers = read_vertigo('vertigo_answers.txt', answers=True)
    predicted_classes = p.predict(training_data)

    correctness(answers, predicted_classes)


# finds nearest neighbour for data item from list
def nearest_neighbour(training_data, test_data, k):
    distance = []
    length = len(test_data) - 1
    for i in range(0, len(training_data)):
        dist = measure_distance(training_data[i], test_data, length)
        distance.append((training_data[i], dist))

    distance.sort(key=operator.itemgetter(1))
    neighbours = []
    for i in range(k):
        neighbours.append(distance[i][0])
    return neighbours


# calculates distance between two items
def measure_distance(set1, set2, length):
    distance = 0
    for i in range(0, length):
        distance += pow((set1[i] - set2[i]), 2)
    return math.sqrt(distance)


# tests nearest neighbour
def test_nearest_neighbour():
    test_data = read_vertigo('vertigo_predict.txt')
    training_data, training_answers = read_vertigo('vertigo_train.txt', True)
    answers = read_vertigo('vertigo_answers.txt', answers=True)
    correct = 0

    for i in range(0, len(test_data)):
        nearest = nearest_neighbour(training_data, test_data[i], 1)
        result = get_response(nearest, training_data, training_answers)

        if result == answers[i]:
            correct += 1

    print('Success percentage: {0:.2f}%'.format(correct/len(test_data)*100))


# finds predicted answer with nearest neighbour
def get_response(nearest, training_data, training_answers):
    for i in range(0, len(training_data)):
        if nearest[0] == training_data[i]:
            return training_answers[i]



print('Testing prediction with finding nearest neighbour: ')
test_nearest_neighbour()

print('\nTesting prediction with PERCEP-O-TRON: ')
test_perceptron()

print('\nTesting prediction with PERCEP-O-TRON buffed with parameters i have no idea of: ')
test_perceptron(100)


