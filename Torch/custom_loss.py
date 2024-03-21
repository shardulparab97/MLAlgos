import torch
import torch.nn as nn

class customLoss(nn.Module):
    def __init__(self):
        super(customLoss, self).__init__()

    def forward(self, preds, targets):
        return torch.mean((preds - targets) ** 2)


predictions = torch.randn(1, 2, 5)
targets =  torch.randn(1, 2, 5)

cl = customLoss()
print(cl(predictions, targets))

