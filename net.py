import torch
import torch.nn as nn

class VOnet(nn.Module):
    def __init__(self):
        super(VOnet, self).__init__()
        self.dim = 10
        self.patchify = Patchifier()

    def forward(self, x):
        return x + self.dim


    def intermediate_process(self, x):
        """
        Méthode intermédiaire qui appelle la méthode forward de Patchifier.
        """
        print("Running intermediate process with input:", x)
        # Vous pouvez effectuer des opérations supplémentaires ici
        output = self.patchify(x)
        return output

class Patchifier(nn.Module):
    def __init__(self):
        super(Patchifier, self).__init__()
        self.linear = nn.Linear(20,4)

    def forward(self, x):
        return self.linear(x)
