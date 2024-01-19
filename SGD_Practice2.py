import  numpy as np

num_samples = 500
num_classes = 3
num_features = 4

def get_one_hot_labels(y):
    # 50 * 3
    y_ = np.zeros((num_samples, num_classes))
    for i in range(num_samples):
        y_[i][y[i]] = 1

    return y_
# 50 * 1
y = np.random.randint(0, num_classes, num_samples)
y = get_one_hot_labels(y)


# 50 * 4
x = np.random.random((num_samples, num_features))
# 4 * 3
w = np.random.random((num_features, num_classes))
b = np.random.random(num_classes)

num_epochs = 10000
lr = 0.01
np.random.seed(0)
# def run_SGD(num_epochs, y, x, w, b):
#     # right npw lets to
#     for epoch in range(num_epochs):
#         avg_loss = 0
#         for _ in range(num_samples):
#             # idx = np.random.choice(num_samples)
#             # x_ = x[idx].reshape(1, -1)
#             # y_ = y[idx].reshape(1, -1)
#             # y_hat = np.dot(x_, w) + b
#             idx = np.random.randint(0, len(x))
#             x_ = x[idx]
#             y_ = y[idx]
#             y_hat = np.dot(x_, w) + b
#             exp_logits = np.exp(y_hat)
#             softmax_probs = exp_logits / sum(exp_logits)
#
#             #  now run softmax on it
#             # exp_vals = np.exp(y_hat)
#             # softmax_probs = exp_vals/np.sum(exp_vals, axis=1, keepdims=True)
#
#             # now get categorical cross entropy on it
#             loss = -1 * np.sum(y_ * np.log(softmax_probs))
#             avg_loss += loss
#             d_w = np.outer(x_, softmax_probs - y_)
#             d_b = np.sum(softmax_probs - y_)
#
#             w = w - lr * d_w
#             b = b - lr * d_b
#
#         if (epoch + 1) % 10 == 0:
#             avg_loss = avg_loss/num_samples
#             print(f"Epoch: {epoch+1}, Average loss is: {avg_loss}")
#
#
#
#
#
# run_SGD(num_epochs, y, x, w, b)
for epoch in range(num_epochs):
    total_loss = 0
    for i in range(len(x)):
        idx = np.random.randint(0, len(x))

        x_i = x[idx]
        y_i = y[idx]
        logits = np.dot(x_i, w) + b
        exp_logits = np.exp(logits)
        softmax_probs = exp_logits / sum(exp_logits)

        loss = -1 * np.sum(y_i * np.log(softmax_probs))
        total_loss += loss

        grad_w = np.outer(x_i, softmax_probs - y_i)
        grad_b = np.sum(softmax_probs - y_i)

        w = w - lr * grad_w
        b = b - lr * grad_b


    average_loss = total_loss/len(x)

    if epoch % 100 == 0:
        print(f'Epoch {epoch}: Loss: {total_loss}, Avg. Loss = {average_loss:.4f}')
