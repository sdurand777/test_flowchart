

from pycallgraph2 import PyCallGraph
from pycallgraph2.output import GraphvizOutput
from pycallgraph2 import Config
from pycallgraph2 import GlobbingFilter

from module1 import func1
from module2 import func2

import numpy as np

def main():
    func1()
    a = 10
    matrice = np.zeros(3)
    print(matrice)
    print(a)
    import pdb; pdb.set_trace()
    func2()

if __name__ == "__main__":


    config = Config()

    config.trace_filter = GlobbingFilter(exclude=['numpy.*', 'pdb.*','pycallgraph2.*' ,'_*'])

    graphviz = GraphvizOutput()
    graphviz.output_file = 'callgraph.pdf'
    graphviz.output_type = 'pdf'  # Spécifier le format de sortie en PDF

    # Générer le graphe d'appel
    with PyCallGraph(output=graphviz, config=config):
        main()

