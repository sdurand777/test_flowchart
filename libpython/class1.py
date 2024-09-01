class Classe1:
    def __init__(self, greeting):
        self.greeting = greeting

    def __call__(self, name):
        return f"{self.greeting}, {name}!"
