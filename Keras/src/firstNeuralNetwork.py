from keras.models import Sequential
from keras.layers import Dense
import numpy
# - Author(s) Jason Brownlee
# - Date 24 May 2016
# - Title of program/source code Develop Your First Neural Network in Python with Keras - Step-By-Step
# - Code version 2
# - Type (e.g. computer program, source code) Source code
# - Web address or publisher (e.g. program publisher, URL) https://machinelearningmastery.com/tutorial-first-neural-network-python-keras/
numpy.random.seed(7)
#load pima indians dataset
dataset = numpy.loadtxt("pima-indians-diabetes", delimiter=",")
# split into input x and output y variables
X = dataset[:,0:8]
Y = dataset[:,8]
#create model
model = Sequential()
model.add(Dense(12, input_dim=8, activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(1, activation='sigmoid'))
#Compile model
model.compile(loss="binary_crossentropy",optimizer ="adam", metrics=['accuracy'])
#fit the model
model.fit(X,Y, epochs=150, batch_size=10)
#evaluate the model
scores = model.evaluate(X,Y)
print("\n%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))