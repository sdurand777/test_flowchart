
import torch
import torch.nn as nn

def method_wrapper_decorator(method):
    def wrapper(*args, **kwargs):
        print(f"Calling method: {method.__name__}")
        result = method(*args, **kwargs)
        print(f"Finished method: {method.__name__}")
        return result
    return wrapper

class Patchifier(nn.Module):
    def __init__(self):
        super(Patchifier, self).__init__()
        self.linear = nn.Linear(20, 4)

    @method_wrapper_decorator
    def forward(self, x):
        return self.linear(x)

class VOnet(nn.Module):
    def __init__(self):
        super(VOnet, self).__init__()
        self.patchify = Patchifier()

class DPVO:
    def __init__(self):
        self.load_weight()
        self.data = torch.randn(1, 20)

    def load_weight(self):
        self.network = VOnet()

    def __call__(self):
        print("self.data : ", self.data)
        output = self.network.patchify(self.data)  # Appelle directement Patchifier.forward
        print("output : ", output)

if __name__ == '__main__':
    dpvo = DPVO()
    dpvo()
