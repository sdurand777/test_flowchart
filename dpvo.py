
import torch
import torch.nn

import functools

from net import VOnet

import contextlib

# class ModelWrapper:
#     def __init__(self, model):
#         self.model = model
#
#     def forward(self, *args, **kwargs):
#         # Appel explicite au forward du modèle
#         print("Calling model forward")
#         return self.model(*args, **kwargs)
#
#     def __call__(self, *args, **kwargs):
#         return self.forward(*args, **kwargs)

class MethodWrapper:
    def __init__(self, method):
        self.method = method

    def __call__(self, *args, **kwargs):
        print(f"Calling {self.method.__name__} with args: {args}, kwargs: {kwargs}")
        result = self.method(*args, **kwargs)
        print(f"Result of {self.method.__name__}: {result}")
        return result



class DPVO:
    def __init__(self):
        self.load_weight()
        self.data = torch.randn(1, 20)

    def load_weight(self):
        self.network = VOnet()

        # Wrapping the 'forward' method of Patchifier instance
        self.network.patchify.forward = MethodWrapper(self.network.patchify.forward)

    def __call__(self):
        print("self.data : ", self.data)
        output = self.network.patchify(self.data)
        print("output : ", output)

# def method_wrapper(method):
#     @functools.wraps(method)
#     def wrapper(*args, **kwargs):
#         print(f"Calling {method.__name__} with args: {args}, kwargs: {kwargs}")
#         result = method(*args, **kwargs)
#         print(f"Result of {method.__name__}: {result}")
#         return result
#     return wrapper

# class MethodWrapper(contextlib.ContextDecorator):
#     def __init__(self, method):
#         self.method = method
#     
#     def __enter__(self):
#         print(f"Entering: {self.method.__name__}")
#     
#     def __exit__(self, exc_type, exc_value, traceback):
#         print(f"Exiting: {self.method.__name__}")
#     
#     def __call__(self, *args, **kwargs):
#         self.__enter__()
#         result = self.method(*args, **kwargs)
#         self.__exit__(None, None, None)
#         return result


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



# class DPVO:
#     def __init__(self):
#         self.load_weight()
#
#         self.data = torch.randn(1, 20)
#
#     def load_weight(self):
#         #self.network = ModelWrapper(VOnet())
#         self.network = VOnet()
#
#         # Wrapping the 'forward' method of Patchifier instance
#         #self.network.patchify.forward = MethodWrapper(self.network.patchify.forward)
#         self.network.patchify.forward = method_wrapper(self.network.patchify.forward)
#
#     #@method_wrapper
#     def __call__(self):
#         print("self.data : ", self.data)
#         output = self.network.patchify(self.data)
#         print("output DPVO call :", output)
#         print("output DPVO call shape :", output.shape)


# class DPVO:
#     def __init__(self):
#         self.load_weight()
#         self.data = torch.randn(1, 20)
#
#     def load_weight(self):
#         self.network = VOnet()
#
#     # def __call__(self):
#     #     print("self.data : ", self.data)
#     #     with MethodWrapper(self.network.patchify):
#     #         output = self.network.patchify(self.data)
#     #     print("output : ", output)
#     def __call__(self):
#         print("self.data : ", self.data)
#         # Directly call the wrapped patchify method
#         output = self.network.patchify(self.data)
#         print("output : ", output)

    # def __call__(self):
    #     print("self.data:", self.data)
    #     output = self.network(self.data)
    #     # output = self.network.intermediate_process(self.data)
    #     print("output DPVO call :", output)
    #     print("output DPVO call shape :", output.shape)


# class DPVO:
#     def __init__(self):
#         self.load_weight()
#
#         self.data = torch.randn(1,20)
#
#     def load_weight(self):
#         self.network = VOnet()
#
#     def __call__(self):
#         print("self.data : ", self.data)
#         output = self.network.patchify(self.data)
#         #output = self.network.intermediate_process(self.data)
#         print("output DPVO call :", output)
#         print("output DPVO call shape :", output.shape)

