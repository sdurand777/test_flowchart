import torch
import torch.nn as nn
import contextlib


# class MethodWrapper(contextlib.ContextDecorator):
#     def __init__(self, method):
#         self.method = method
#     
#     def __enter__(self):
#         method_name = getattr(self.method, '__name__', type(self.method).__name__)
#         print(f"Entering: {method_name}")
#     
#     def __exit__(self, exc_type, exc_value, traceback):
#         method_name = getattr(self.method, '__name__', type(self.method).__name__)
#         print(f"Exiting: {method_name}")
#     
#     def __call__(self, *args, **kwargs):
#         self.__enter__()
#         # Appel explicite de la méthode réelle
#         result = self.method(*args, **kwargs)
#         self.__exit__(None, None, None)
#         return result


class VOnet(nn.Module):
    def __init__(self):
        super(VOnet, self).__init__()
        self.dim = 10
        self.patchify = Patchifier()
        #self.patchify = MethodWrapper(Patchifier())

    def forward(self, x):
        return x + self.dim

    # def intermediate_process(self, x):
    #     """
    #     Méthode intermédiaire qui appelle la méthode forward de Patchifier.
    #     """
    #     print("Running intermediate process with input:", x)
    #     # Vous pouvez effectuer des opérations supplémentaires ici
    #     output = self.patchify(x)
    #     return output

class Patchifier(nn.Module):
    def __init__(self):
        super(Patchifier, self).__init__()
        self.linear = nn.Linear(20,4)
        self.__name__ = "Patchifier Class"

    def __call__(self, x):
        return self.linear(x)

    # def forward(self, x):
    #     return self.linear(x)
