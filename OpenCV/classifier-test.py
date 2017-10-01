from sklearn.neural_network import MLPClassifier
from sklearn.datasets import load_svmlight_file

# trainingData = [[1,0,0], [0,1,0], [0,0,1]]
# trainingLabels = [1, 2, 3]

trainingData, trainingLabels = load_svmlight_file("dataset.txt")

clf = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(15,), random_state=1)

clf.fit(trainingData, trainingLabels)

print( int(clf.predict([[0,0,1]])[0]) )
