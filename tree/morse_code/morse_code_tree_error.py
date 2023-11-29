class MorseCodeTreeError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self) -> str:
        return (repr(self.value))
