from re import X
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
import random
from math import sin, cos, pi, sqrt
from sklearn.metrics import accuracy_score

def meteorites():
    angle = random.uniform(0, 2 * pi)  # in radians
    distance = sqrt(random.uniform(200, 300))
    return distance * cos(angle), distance * sin(angle)

x = np.zeros(1000)
y = np.zeros(1000)

for i in range(1000):
    x[i], y[i] = meteorites()

plt.scatter(x,y, color='red')


x = x.reshape(1, -1)
y = y.reshape(1, -1)

r2 = 2 * np.sqrt(np.random.rand(1, 1000))
theta2 = 2 * np.pi * np.random.rand(1, 1000)
x2 = r2 * np.cos(theta2)
y2 = r2 * np.sin(theta2)

plt.scatter(x2,y2, color='blue')
plt.show()

X_1 = np.concatenate((x, y))
X_2 = np.concatenate((x2, y2))

X_train = np.concatenate((X_1, X_2), axis=1)
X_hat = np.concatenate(((np.ones((1, 2000)), X_train)))

y_train = tf.keras.layers.Concatenate(axis=1)([tf.ones((1, 1000)), tf.zeros((1, 1000))])

# print(y_train)
theta1 = tf.Variable([[1.,-1., 1.], [1., -1., 1.], [1., 1., -1.]])
theta2 = tf.Variable([[-1.], [-1.], [-1.]])


def loss():
    layer_1 = tf.keras.activations.sigmoid(tf.linalg.matmul(theta1, X_hat, transpose_a=True))
    # print(layer_1)
    layer_2 = tf.linalg.matmul(theta2, layer_1, transpose_a=True)
    # print(layer_2)
    return tf.reduce_mean(tf.nn.sigmoid_cross_entropy_with_logits(logits=layer_2, labels=y_train))

opt = tf.keras.optimizers.Adam(learning_rate = 0.1)
eps = 0.00001
i = 0
while True:
    with tf.GradientTape() as tape:
        loss_ = loss()
    grads = tape.gradient(loss_, [theta2, theta1])
    opt.apply_gradients(zip(grads, [theta2, theta1]))
    print('Loss:', loss_.numpy())
    # break
    if abs(loss_.numpy()) < eps:
        break

layer_1 = tf.keras.activations.sigmoid(tf.linalg.matmul(theta1, X_hat, transpose_a=True))
    # print(layer_1)
layer_2 = tf.keras.activations.sigmoid(tf.linalg.matmul(theta2, layer_1, transpose_a=True))

layer_2=tf.round(layer_2)
acc = accuracy_score(layer_2, y_train)
print(acc)