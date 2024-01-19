import  numpy as np

num_samples = 50
num_classes = 3
num_features = 4

def get_one_hot_encoded(y, num_classes):
    y_matrix = np.zeros((num_samples, num_classes))
    for i in range(num_samples):
        y_matrix[i, y[i]] = 1
    return y_matrix



y = np.random.randint(0, num_classes, num_samples)
x = np.random.random((num_samples, num_features))

w = np.random.random((num_features, num_classes))
b = np.random.random(num_classes)

y = get_one_hot_encoded(y, num_classes)

lr = 0.01
epochs = 1000
#
# def softmax(x, i):
#


for epoch in range(epochs):
    # loss = 0
    for i in range(len(x)):
        idx = np.random.randint(0, len(x))

        x_i = x[idx]
        y_i = y[idx]
        logits = np.dot(x_i, w) + b
        exp_logits = np.exp(logits)
        softmax_probs = exp_logits / sum(exp_logits)

        loss = -1 * np.sum(y_i * np.log(softmax_probs))

        grad_w = np.outer(x_i, softmax_probs - y_i)
        grad_b = np.sum(softmax_probs - y_i)

        w = w - lr * grad_w
        b = b - lr * grad_b


    average_loss = loss/len(x)

    if epoch % 100 == 0:
        print(f'Epoch {epoch}: Loss: {loss}, Avg. Loss = {average_loss:.4f}')

# # run a prediction
# y = np.array([0, 1, 1])
# x = np.random.random((1, num_features))
#
# logits = np.dot(x, w) + b








