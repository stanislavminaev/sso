from abc import ABC, abstractmethod


class ApplicationService(ABC):
    @abstractmethod
    def result(self):
        pass
