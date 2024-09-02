import torch
import torch.nn

from classtorch import SimpleModel

# Définition de la classe SimpleNet qui contient SimpleModel en tant qu'attribut
class SimpleNet:
    def __init__(self):
        # Instanciation du modèle SimpleModel
        self.model = SimpleModel()

    def predict(self, x):
        # Prédiction avec le modèle
        with torch.no_grad():
            return self.model(x)
