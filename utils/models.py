# To address imbalance, compute the weights
import numpy as np
import tensorflow as tf
import contextlib

from sklearn.utils import class_weight
from tensorflow.keras.layers import Dense, Dropout
from tensorflow.keras.models import Sequential
from tensorflow.keras.regularizers import L2


def get_class_weights(Y):
    weights = class_weight.compute_class_weight(class_weight="balanced", classes=np.unique(Y), y=Y)
    class_weights = {0: weights[0], 1: weights[1]}
    return class_weights


def get_feed_forward_model(features_num):
    model = Sequential()
    model.add(Dense(units=512, activation='tanh', kernel_regularizer=L2(1e-5), bias_regularizer=L2(1e-5),
                    input_shape=(features_num,)))
    model.add(Dense(units=256))
    model.add(Dropout(0.4))
    model.add(Dense(units=1, activation='sigmoid'))

    opt = tf.keras.optimizers.Adam(learning_rate=0.0001)

    model.compile(optimizer=opt, loss='binary_crossentropy')
    return model


@contextlib.contextmanager
def local_seed(seed):
    state = np.random.get_state()
    np.random.seed(seed)
    tf.random.set_seed(seed)

    try:
        yield
    finally:
        np.random.set_state(state)
        tf.random.set_seed(np.random.randint(1000))
