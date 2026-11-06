# It is a built-in helper function that loads the Iris dataset, which is included with Scikit-learn. You don't need to download a CSV file separately.Scikit-learn loads the dataset and returns an object containing the data and some information about it.
from sklearn.datasets import load_iris
# This function splits the dataset into training data and testing data.
from sklearn.model_selection import train_test_split
# This imports the Random Forest classification algorithm.
from sklearn.ensemble import RandomForestClassifier
# This function measures how many predictions were correct.
from sklearn.metrics import accuracy_score
# Joblib allows us to save the trained model to a file and load it later.

import joblib

iris = load_iris()   # load_iris() gives us a ready-made Iris dataset from Scikit-learn.

print(iris.data)
print(iris.target)
print(iris.feature_names)
print(iris.target_names)

# Separate features and target
# X contains the input measurements.
# y contains the correct species labels.
# The target values are encoded as numbers:
# 0 → Setosa
# 1 → Versicolor
# 2 → Virginica
X = iris.data
y = iris.target

'''
test_size=0.2

20% of the dataset is reserved for testing.

random_state=42

Ensures that the split is reproducible. If you run the code again, you get the same split.

stratify=y

Maintains the approximate proportion of each species in both the training and testing sets.
'''

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

'''
A Random Forest is a machine learning algorithm that combines multiple decision trees.
A decision tree makes decisions based on the input measurements.

For example, it might learn rules such as:
- If petal length is small, the flower may be Setosa.
- If petal length is larger, it may be Versicolor or Virginica.
A Random Forest combines the predictions of many decision trees and chooses the final class.

n_estimators=100 means the Random Forest contains 100 decision trees.
'''
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

'''
actual training step.

The model receives:
- X_train: The flower measurements.
- y_train: The correct species labels.
It learns patterns connecting the measurements to the species.
'''

model.fit(X_train, y_train)

# The model predicts the species for the 30 testing samples.
y_pred = model.predict(X_test)

'''
y_test contains the correct labels.

y_pred contains the predicted labels.

Accuracy measures the proportion of predictions that were correct.

'''

accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

#This saves the trained model to a file named iris_model.pkl"
'''
Why save it?

We do not want to train the model every time a user visits our Flask application.

Instead, Flask will load the already-trained model:
'''

joblib.dump(model, "iris_model.pkl")


# Using test data 
model = joblib.load("iris_model.pkl")
prediction = model.predict([[5.1, 3.5, 1.4, 0.2]])
flower_name = iris.target_names[prediction[0]]

print("Predicted flower:", flower_name)