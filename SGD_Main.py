#Loading
# import torch
# import torchvision
# import torchvision.datasets as datasets
# mnist_trainset = datasets.MNIST(root='./data', train=True, download=True, transform=None)
# mnist_testset = datasets.MNIST(root='./data', train=False, download=True, transform=None)

import numpy as np
from keras.datasets import mnist
import matplotlib.pyplot as plt
(train_X, train_y), (test_X, test_y) = mnist.load_data()
#Plotting
train_X = train_X[:1500]
train_y = train_y[:1500]
test_X = test_X[:200]
test_y = test_y[:200]
fig = plt.figure(figsize=(10,7))
for i in range(15):
    ax = fig.add_subplot(3, 5, i+1)
    ax.imshow(train_X[i], cmap=plt.get_cmap('gray'))
    ax.set_title('Label (y): {y}'.format(y=train_y[i]))
    plt.axis('off')

# X_train = train_X.reshape(60000,28*28)
# X_test = test_X.reshape(10000,28*28)


def one_hot(y, c):
    # y--> label/ground truth.
    # c--> Number of classes.

    # A zero matrix of size (m, c)
    y_hot = np.zeros((len(y), c))

    # Putting 1 for column where the label is,
    # Using multidimensional indexing.
    y_hot[np.arange(len(y)), y] = 1

    return y_hot


def softmax(z):
    # z--> linear part.

    # subtracting the max of z for numerical stability.
    exp = np.exp(z - np.max(z))

    # Calculating softmax for all examples.
    for i in range(len(z)):
        exp[i] /= np.sum(exp[i])

    return exp


def fit(X, y, lr, c, epochs):
    # X --> Input.
    # y --> true/target value.
    # lr --> Learning rate.
    # c --> Number of classes.
    # epochs --> Number of iterations.

    # m-> number of training examples
    # n-> number of features
    m, n = X.shape

    # Initializing weights and bias randomly.
    w = np.random.random((n, c))
    b = np.random.random(c)
    # Empty list to store losses.
    losses = []

    # Training loop.
    for epoch in range(epochs):

        # Calculating hypothesis/prediction.
        z = X @ w + b
        y_hat = softmax(z)

        # One-hot encoding y.
        y_hot = one_hot(y, c)

        # Calculating the gradient of loss w.r.t w and b.
        w_grad = (1 / m) * np.dot(X.T, (y_hat - y_hot))
        b_grad = (1 / m) * np.sum(y_hat - y_hot)

        # Updating the parameters.
        w = w - lr * w_grad
        b = b - lr * b_grad

        # Calculating loss and appending it in the list.
        loss = -np.mean(np.log(y_hat[np.arange(len(y)), y]))
        losses.append(loss)
        # Printing out the loss at every 100th iteration.
        if epoch % 100 == 0:
            print('Epoch {epoch}==> Loss = {loss}'
                  .format(epoch=epoch, loss=loss))
    return w, b, losses

def softmax_sgd(x):
    exp_x = np.exp(x - np.max(x, axis=1, keepdims=True))
    return exp_x / np.sum(exp_x, axis=1, keepdims=True)
def fit_sgd(X, y, lr, c, epochs):
    n = len(X[0])
    w = np.random.random((n, c))
    b = np.random.random(c)
    y_hot = one_hot(y, c)
    for epoch in range(epochs):
        total_loss = 0.0
        for _ in range(len(X)):
            idx = np.random.choice(len(X))
            x_ = X[idx]
            y_ = y_hot[idx]

            y_hat = np.dot(x_, w) + b
            exp = np.exp(y_hat - np.argmax(y_hat))
            exp /= np.sum(exp)
            y_hat = exp
            # y_hat = softmax(y_hat)
            # y_hat = softmax(y_hat)


            loss = -1 * np.sum(y_ * np.log(y_hat))
            # loss = -np.mean(np.log(y_hat[y[idx]]))
            # print(loss)
            total_loss += loss
            dw = np.outer(x_, (y_hat - y_))
            db = np.sum(y_hat - y_hot, axis=0)

            w = w - lr * dw
            b = b - lr * db

        if (epoch+1)%10 == 0:
            total_loss = loss/len(X)
            print(f"{epoch+1 }total loss: {total_loss}")





def predict(X, w, b):
    # X --> Input.
    # w --> weights.
    # b --> bias.

    # Predicting
    z = X @ w + b
    y_hat = softmax(z)

    # Returning the class with highest probability.
    return np.argmax(y_hat, axis=1)

def accuracy(y, y_hat):
    return np.sum(y==y_hat)/len(y)


X_train = train_X.reshape(1500,28*28)
# Normalizing.
X_train = X_train/255
# Training
# w, b, l = fit(X_train, train_y, lr=0.9, c=10, epochs=1000)
w, b, l = fit_sgd(X_train, train_y, lr=0.01, c=10, epochs=1000)


# Flattening the image.
X_train = train_X.reshape(1500,28*28)
# Normalizing.
X_train = X_train/255
# Training
# w, b, l = fit(X_train, train_y, lr=0.9, c=10, epochs=1000)


