from sklearn import datasets, linear_model, metrics 

# load the digit dataset 
# digits = datasets.load_digits() 

# # defining feature matrix(X) and response vector(y) 
# X = digits.data 
# y = digits.target 

import numpy as np

Xtrain = np.array([[91],
                   [90],
                   [89],
                   [88],
                   [87],
                   [86],
                   [85],
                   [84],
                   [83],
                   [82],
                   [81],
                   [80],[79],[78],[77],[76],[75],[74],[73],[72],[71],[70],[69],[68],[67],[66],[65],[64],[63],[62],[61],[60],[59],[58],[57],[56],[55],[54],[53],[52],[51],[50]])

ytrain = np.array([0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1, 3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3])

# splitting X and y into training and testing sets 
# from sklearn.model_selection import train_test_split 
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, 
# 													random_state=1) 

# create logistic regression object 
reg = linear_model.LogisticRegression() 

# train the model using the training sets 
reg.fit(Xtrain, ytrain) 

import pickle

pickle_out = open("LogisticRegression.pkl","wb")
pickle.dump(reg,pickle_out)
pickle_out.close()

# making predictions on the testing set 
y_pred = reg.predict([[101.10]])

print(y_pred) 

# comparing actual response values (y_test) with predicted response values (y_pred) 
# print("Logistic Regression model accuracy(in %):", 
# metrics.accuracy_score(ytrain, y_pred)*100) 
