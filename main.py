import tensorflow as tf

hi = tf.constant("Hello!")

with tf.Session() as sess:
    print(sess.run(hi))
