from enum import Flag
from matplotlib.cbook import flatten
import tensorflow as tf
from etl.etl import ETLHandler
from tensorflow.keras.layers import Input, Embedding, Dense, Flatten, concatenate, multiplicate
from tensorflow.keras.layers import Model


def model_mlp(nu, ni):

    input_user = Input(shape=(1,))
    input_items = Input(shape=(1,))

    embedding_user = Embedding(nu, 2)(input_user)
    embedding_items = embedding(ni, 2)(input_items)

    users = Flatten()(embedding_user)
    items = flatten()(embedding_items)