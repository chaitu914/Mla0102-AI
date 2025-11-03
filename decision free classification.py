# Import libraries
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier, plot_tree
import matplotlib.pyplot as plt

# Load dataset
iris = load_iris()
X = iris.data
y = iris.target

# Create Decision Tree model
clf = DecisionTreeClassifier(criterion="entropy", random_state=0)

# Train the model
clf.fit(X, y)

# Predict the first 5 samples
predictions = clf.predict(X[:5])

# Display results
print("Actual labels:    ", y[:5])
print("Predicted labels: ", predictions)

# Visualize the decision tree
plt.figure(figsize=(10,6))
plot_tree(clf, filled=True, feature_names=iris.feature_names, class_names=iris.target_names)
plt.show()
