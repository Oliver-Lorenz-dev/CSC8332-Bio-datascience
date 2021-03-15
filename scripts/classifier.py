#!/usr/bin/env python3

import pandas
import tensorflow
from tensorflow import keras
from tensorflow.keras.layers import Dense
from sklearn import model_selection
from sklearn import preprocessing
from sklearn.preprocessing import LabelEncoder
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.layers import Embedding, Conv1D, MaxPooling1D
from tensorflow.keras.layers import Dropout, Flatten, Dense
from tensorflow.keras.wrappers.scikit_learn import KerasClassifier
import numpy
from sklearn import model_selection

# set seed
tensorflow.random.set_seed(3)

# read data
data = pandas.read_csv('/home/c0059478/Documents/8332/data/proteins.csv.gz')

# preprocessing
y = preprocessing.LabelBinarizer().fit_transform(data.pfam_id)

#convert sequences to lists of tokens
tokenizer = keras.preprocessing.text.Tokenizer(char_level=True)
tokenizer.fit_on_texts(data.sequence)
x = tokenizer.texts_to_sequences(data.sequence)

# pad short / trim long sequences
MAX_LENGTH = 150
x = keras.preprocessing.sequence.pad_sequences(x, MAX_LENGTH, truncating="post")

CLASSES = len(y[0])
TOKENS = len(tokenizer.word_index) + 1
DIMENSIONS = 8
UNITS = 32
SIZE = 4
DROPOUT_RATE = 0.2

# build model function
def build_cnn():
  model = keras.Sequential([
    Embedding(TOKENS, DIMENSIONS, input_length=MAX_LENGTH, mask_zero=True),

    Conv1D(UNITS, SIZE, activation="relu"),
    MaxPooling1D(SIZE),
    Dropout(DROPOUT_RATE),

    Conv1D(UNITS, SIZE, activation="relu"),
    MaxPooling1D(UNITS),
    Dropout(DROPOUT_RATE),

    Flatten(),
    Dense(UNITS, activation="relu"),
    Dense(CLASSES, activation="softmax")
  ])

  model.compile(loss="categorical_crossentropy", optimizer="Adam", metrics=["accuracy"])
  return model

# write wrapper over classifier
class MyClassifier(keras.wrappers.scikit_learn.KerasClassifier):
  def predict(self, x, **kwargs):
    predictions = self.model.predict(x, **kwargs)
    classes = numpy.argmax(predictions, axis=-1)
    return preprocessing.LabelBinarizer().fit(self.classes_).transform(classes)

# predict scores
nn = MyClassifier(build_cnn, epochs=5)
scores = model_selection.cross_val_score(nn, x, y, scoring="f1_macro", cv=5)

# print output to terminal
print(scores)
