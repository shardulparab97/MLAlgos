import numpy as np

# say we have the data in the ofll
def sigmoid(z):
    return 1/(1+np.exp(-z))


class LogisticRegression:
    def __init__(self, x, y):
        self.x = x
        self.y = y.reshape(-1, 1)
        self.num_samples, self.num_features = x.shape
        self.w = np.random.random((num_features, 1))
        self.b = 0
        # self.num_samples = self.y.shape[0]

    def get_rmse(self, y, pred):
        return (1/(2*self.num_samples))*np.sqrt(np.sum((y - pred)**2))


    def fit(self, epochs, lr):
        for epoch in range(epochs):
            z = np.dot(self.x, self.w) + self.b
            predictions = sigmoid(z)

            loss = self.get_rmse(self.y, z)
            dw = (1/self.num_samples) * np.dot(self.x.T, (predictions-self.y))
            db = (1/self.num_samples) * np.sum(predictions - self.y)

            self.w = self.w - lr * dw
            self.b = self.b - lr * db

            if (epoch+1)%10 == 0:
                print(f"RMSE loss is: {loss}")


num_samples = 100
num_features = 4
learning_rate = 0.01
num_epochs = 250
y = np.random.random(num_samples)
x = np.random.random((num_samples, num_features))
lr = LogisticRegression(x, y)
lr.fit(num_epochs, learning_rate)



