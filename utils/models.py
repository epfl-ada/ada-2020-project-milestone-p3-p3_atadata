# To address imbalance, compute the weights
import numpy as np
import tensorflow as tf
import contextlib

from sklearn.utils import class_weight
from tensorflow.keras.layers import Dense, Dropout
from tensorflow.keras.models import Sequential
from tensorflow.keras.regularizers import L2
from sklearn.preprocessing import StandardScaler


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


def get_embedding_submodel(maxlen, maxwords, embedding_dim, embedding_matrix):
    inputs = tf.keras.layers.Input(shape=(maxlen), name="emb_input")
    embedding = tf.keras.layers.Embedding(maxwords, embedding_dim, weights=[embedding_matrix], trainable=False)(inputs)
    lstm = tf.keras.layers.LSTM(64, activation='relu', kernel_regularizer=L2(1e-5), bias_regularizer=L2(1e-5))(
        embedding)
    model = tf.keras.Model(inputs=inputs, outputs=lstm)
    return model


def get_numerical_submodel(numerical_features_num):
    inputs = tf.keras.layers.Input(shape=(numerical_features_num), name="num_input")
    dense = tf.keras.layers.Dense(64, kernel_regularizer=L2(1e-5), bias_regularizer=L2(1e-5), name="num_dense")(inputs)
    model = tf.keras.Model(inputs=inputs, outputs=dense)
    return model


def get_combined_model(model_embeddings, model_numerical):
    combined = tf.keras.layers.concatenate([model_embeddings.output, model_numerical.output])
    dense = tf.keras.layers.Dense(32, activation='linear', name="combined_dense")(combined)
    dropout = tf.keras.layers.Dropout(0.4)(dense)
    final_output = tf.keras.layers.Dense(1, activation="sigmoid")(dropout)

    model = tf.keras.models.Model(inputs=[model_embeddings.input, model_numerical.input], outputs=final_output)
    model.compile(loss='binary_crossentropy', optimizer=tf.keras.optimizers.Adam(lr=0.0005))
    return model


def get_numerical_model_x_inputs(x_train, x_test):
    # Inputs for the numerical model
    numerical_model_features = ['sentiment_positive', 'sentiment_neutral', 'sentiment_negative', 'n_requests',
                                'n_words', 'politeness', 'n_sentences', 'delta_role_politeness',
                                'delta_time_politeness', 'friendship_length']
    x_train = x_train[numerical_model_features]
    x_test = x_test[numerical_model_features]

    # Standardization of numerical features
    scaler = StandardScaler()
    x_train = scaler.fit_transform(x_train)
    x_test = scaler.transform(x_test)

    return x_train, x_test


def get_embeddings_model_x_inputs(x_train, x_test, maxlen):
    x_train = x_train['all_words']
    x_test = x_test['all_words']

    x_train = tf.keras.preprocessing.sequence.pad_sequences(list(x_train), maxlen=maxlen, padding='post')
    x_test = tf.keras.preprocessing.sequence.pad_sequences(list(x_test), maxlen=maxlen, padding='post')
    return x_train, x_test


def get_embedding_model_only(maxlen, maxwords, embedding_dim, embedding_matrix):
    inputs = tf.keras.layers.Input(shape=(maxlen), name="emb_input")
    embedding = tf.keras.layers.Embedding(maxwords, embedding_dim, weights=[embedding_matrix], trainable=False)(inputs)
    lstm = tf.keras.layers.LSTM(64, activation='relu', kernel_regularizer=L2(1e-6))(embedding)
    dropout = tf.keras.layers.Dropout(0.4)(lstm)
    output = tf.keras.layers.Dense(1, activation="sigmoid")(dropout)

    model = tf.keras.Model(inputs=inputs, outputs=output)
    model.compile(loss='binary_crossentropy', optimizer=tf.keras.optimizers.Adam(lr=0.001))
    return model
