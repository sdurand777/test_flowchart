
import torch
import torch.nn

from .net import VOnet

class DPVO:
    def __init__(self):
        self.load_weight()

        self.data = torch.randn(1,20)

    def load_weight(self):
        self.network = VOnet()

    def __call__(self):
        print("self.data : ", self.data)
        output = self.network.patchify(self.data)
        print("output : ", output)
