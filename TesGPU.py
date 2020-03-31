# -*- coding: utf-8 -*-
"""
Created on Sun Jan 19 23:43:58 2020

@author: revaldi
"""

# testing GPU cara ke-1
import tensorflow as tf
if tf.test.gpu_device_name():
    print('Default GPU Device: {}'.format(tf.test.gpu_device_name()))
else:
    print("Please install GPU version of TF")
print(tf.test.is_gpu_available())

# testing GPU cara ke-2
import tensorflow as tf
sess = tf.compat.v1.Session(config=tf.compat.v1.ConfigProto(
    allow_soft_placement=True,
    log_device_placement=True))

#testing tensorflow
import tensorflow as tf
with tf.compat.v1.Session() as sess:  
    hello = tf.constant('Hello, TensorFlow!')
    print(sess.run(hello))