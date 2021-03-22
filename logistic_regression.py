import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
import sqlite3

# We need two functions: One for training model and another for predicting results.
classifier = LogisticRegression()
sc = StandardScaler()

def train_model():
  # con stands for connection
  con = sqlite3.connect("dataset.db")
  dataset = pd.read_sql_query("SELECT * FROM dataset", con)

  # print(dataset.head())
  # iloc[whatRowsToSelect, whatColumnsToSelect]
  # lowerBounds selects the row/column while upperBounds excludes the row/column
  # : - takes all rows/columns. -1 - selects the last element (in our case last column), however
  # the last column is going to be excluded since the upperBound excludes the entered value.
  X = dataset.iloc[:, :-1] # Our features/independent variables. X - because it is displayed on x-axis
  y = dataset.iloc[:, -1] # Our dependent variable. y - because it is displayed on y-axis

  # Splitting dataset into train and test sets.
  X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25)

  X_train = sc.fit_transform(X_train)
  X_test = sc.fit_transform(X_test)

  classifier.fit(X_train, y_train)

  print("Training OK!")
  con.close()


def predict(age, income):
  prediction = classifier.predict(sc.transform([[age, income]]))
  prediction = True if prediction == 1 else False
  print(prediction)

  click_probability = classifier.predict_proba(sc.transform([[age, income]]))
  click_probability = int(click_probability[0, 1] * 100)
  print(click_probability)

  result = {"will-click": prediction, "probability": click_probability}
  return result
