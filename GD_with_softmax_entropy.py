import numpy as np

# Define your dataset (example data)
X = np.random.rand(50, 3)  # Input features, shape (50, 3)
Y = np.random.randint(0, 3, size=50)  # Target labels (0, 1, or 2), shape (50,)

# Define the number of classes
num_classes = 3

# Initialize the parameters (weights and biases)
learning_rate = 0.01
epochs = 1000
weights = np.random.rand(3, num_classes)  # Weights, shape (3, num_classes)
biases = np.random.rand(num_classes)  # Biases, shape (num_classes,)


# One-hot encode the target labels
def one_hot_encode(labels, num_classes):
    one_hot_labels = np.zeros((len(labels), num_classes))
    for i, label in enumerate(labels):
        one_hot_labels[i, label] = 1
    return one_hot_labels


Y_one_hot = one_hot_encode(Y, num_classes)

# Perform batch gradient descent
for epoch in range(epochs):
    # Calculate the softmax probabilities for the entire dataset
    logits = np.dot(X, weights) + biases
    exp_logits = np.exp(logits)
    softmax_probs = exp_logits / np.sum(exp_logits, axis=1, keepdims=True)

    # Calculate the categorical cross-entropy loss
    loss = -np.sum(Y_one_hot * np.log(softmax_probs)) / len(X)

    # Calculate the gradients
    gradient_weights = np.dot(X.T, softmax_probs - Y_one_hot) / len(X)
    gradient_biases = np.sum(softmax_probs - Y_one_hot, axis=0) / len(X)

    # Update parameters using batch gradient descent
    weights = weights - learning_rate * gradient_weights
    biases = biases - learning_rate * gradient_biases

    # Print the progress
    if epoch % 100 == 0:
        print(f'Epoch {epoch}: Loss = {loss:.4f}')

print('Training complete!')
