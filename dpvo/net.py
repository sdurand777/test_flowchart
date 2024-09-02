import torch
import torch.nn as nn

class VOnet(nn.Module):
    def __init__(self):
        super(VOnet, self).__init__()
        self.dim = 10
        self.patchify = Patchifier()

    def forward(self, x):
        return x + self.dim

class Patchifier(nn.Module):
    def __init__(self):
        super(Patchifier, self).__init__()
        self.linear = nn.Linear(20,4)

    def forward(self, x):
        return self.linear(x)
