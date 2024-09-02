
import torch
import torch.nn as nn

from libpython.module3 import func3

# Définition d'une classe simple avec une méthode forward
class SimpleModel(nn.Module):
    def __init__(self):
        super(SimpleModel, self).__init__()
        # Une simple couche linéaire avec une entrée de dimension 10 et une sortie de dimension 1
        self.linear = nn.Linear(10, 1)

    def forward(self, x):
        # La méthode forward définit le passage des données dans le réseau
        func3()

        return self.linear(x)
