

from pycallgraph2 import PyCallGraph
from pycallgraph2.output import GraphvizOutput
from pycallgraph2 import Config
from pycallgraph2 import GlobbingFilter

from module1 import func1
from module2 import func2
from classtorch import SimpleModel

from classnet import SimpleNet

import numpy as np

import torch
import torch.nn as nn

from dpvo import DPVO


def main():
    func1()
    a = 10
    matrice = np.zeros(3)
    print(matrice)
    print(a)
    #import pdb; pdb.set_trace()
    func2()
    # Initialisation du modèle
    net = SimpleNet() 
    # Création d'un tensor d'entrée aléatoire de taille (1, 10)
    input_tensor = torch.randn(1, 10)
    # Appel de la méthode forward avec le tensor d'entrée
    output = net.predict(input_tensor)
    # Affichage du résultat
    print("Input Tensor:", input_tensor)
    print("Output Tensor:", output)

    slam = DPVO()

    slam()





if __name__ == "__main__":


    config = Config()

    config.trace_filter = GlobbingFilter(exclude=['numpy.*', 
                                                  'pdb.*',
                                                  'pycallgraph2.*' ,
                                                  '_*', 
                                                  'torch.*'
                                                  ])

    graphviz = GraphvizOutput()
    graphviz.output_file = 'callgraph.pdf'
    graphviz.output_type = 'pdf'  # Spécifier le format de sortie en PDF

    # Générer le graphe d'appel
    with PyCallGraph(output=graphviz, config=config):
        main()

