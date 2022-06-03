import pandas as pd
import numpy as np
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
import graphviz

iris_data = load_iris()

iris_df = pd.DataFrame(iris_data.data, columns=iris_data.feature_names)
iris_df["target"] = iris_data.target

print(iris_data.feature_names)
X = iris_data.data
y = iris_data.target

X_train , X_test, y_train, y_test = train_test_split(X, y, stratify=iris_df.target, test_size=0.3, random_state=42)


dt_classifier = DecisionTreeClassifier(max_leaf_nodes=5)

dt_classifier.fit(X_train, y_train)
# tree.plot_tree(dt_classifier)

dot_data = tree.export_graphviz(dt_classifier, out_file=None)
graph = graphviz.Source(dot_data)
graph.render("iris")

print(dt_classifier.score(X_test, y_test))