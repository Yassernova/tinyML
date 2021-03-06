#!/usr/bin/env python
from keras.models import Sequential, Graph
from keras.models import model_from_json
from keras.layers.core import Dense, Dropout, Activation
from keras.optimizers import SGD
import numpy as np
import theano, sys

import numpy as np                                                                                                                
import pandas as pd

def fn(xt) :
  return np.sin(xt) + 2*np.cos(np.multiply(2.1, xt)) - 1.4*np.cos(3.4*np.sin(np.multiply(xt, xt)))

# xt = np.random.rand(20000, 1)
# xt = np.multiply(xt, 10)
# yt = fn(xt)
# 
# dx = pd.DataFrame(xt)
# dy = pd.DataFrame(yt)
# 
# dx.to_csv("/home/jhallard/linux/tinyML/trig_v1_input.csv")
# dy.to_csv("/home/jhallard/linux/tinyML/trig_v1_labels.csv")
# 
# sys.exit(0)

dx = pd.read_csv("/home/jhallard/linux/tinyML/trig_v1_input.csv")
dy = pd.read_csv("/home/jhallard/linux/tinyML/trig_v1_labels.csv")
X = dx.values.copy()
X = X[:, -1:]
print str(X)

Y = dy.values.copy()
Y = Y[:, -1:]
print str(Y)

model = Sequential()
model.add(Dense(output_dim=18, input_dim=1))
model.add(Activation('relu'))
model.add(Dense(output_dim=64, init='uniform', input_dim=15))
# model.add(Dropout(0.1))
model.add(Activation('relu'))
# model.add(Dropout(0.1))
model.add(Dense(1, init='uniform'))
model.compile(loss='mean_squared_error', optimizer='rmsprop')
model.fit(X, Y, nb_epoch=460, batch_size=360, validation_split=0.2)


