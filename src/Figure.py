from abc import ABC, abstractmethod


class Figure(ABC):
    area = 0
    perimeter = 0

    @abstractmethod
    def get_area(self):
        pass

    @abstractmethod
    def get_perimeter(self):
        pass

    def add_area(self, figure):
        return self.get_area() + figure.get_area()


