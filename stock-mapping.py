# encoding: utf-8

import os
import tensorflow as tf

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
index = [23, 21, 30, 27, 29]
one_hot = tf.one_hot(index, 40)

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    print(sess.run(one_hot))

