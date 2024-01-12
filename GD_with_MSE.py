import numpy as np

# Generate example data
X = np.array([[1, 2, 3, 4],
              [2, 3, 4, 5],
              [3, 4, 5, 6],
              [4, 5, 6, 7],
              [5, 6, 7, 8]])  # Input features, shape (5, 4)
Y = np.array([2, 4, 5, 4, 5])  # Target values

# Initialize parameters
learning_rate = 0.01
epochs = 1000
weights = np.zeros(4)  # Initial guess for the weights
bias = 0.0  # Initial guess for the bias

# Perform gradient descent
for epoch in range(epochs):
    # Calculate predictions
    predictions = np.dot(X, weights) + bias

    # Calculate the gradient of the cost function with respect to weights and bias
    gradient_weights = (-2 / len(X)) * np.dot(X.T, Y - predictions)
    gradient_bias = (-2 / len(X)) * np.sum(Y - predictions)

    # Update parameters using gradient descent update rule
    weights = weights - learning_rate * gradient_weights
    bias = bias - learning_rate * gradient_bias

    # Calculate the Mean Squared Error (MSE)
    mse = np.mean((predictions - Y) ** 2)

    # Print the progress
    if epoch % 100 == 0:
        print(f'Epoch {epoch}: MSE = {mse:.4f}, Weights = {weights}, Bias = {bias:.4f}')

print(f'Final values: Weights = {weights}, Bias = {bias:.4f}')