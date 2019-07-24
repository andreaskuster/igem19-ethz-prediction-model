from abc import ABC, abstractmethod


class AbstractDataSource(ABC):

    def __init__(self):
        super().__init__()

    """
    Define all abstract methods like this:
    
    @abstractmethod
    def dummy_method(self):
        pass
    """