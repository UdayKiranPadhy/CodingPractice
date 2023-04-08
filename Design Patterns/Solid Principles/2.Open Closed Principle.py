# OPEN FOR EXTENSION, CLOSED FOR MODIFICATION
#
#
# # Open for extension, closed for modification
#
#
# Imagine we have a class that filters products by color
# and another class that filters products by size
# and we want to combine them


from enum import Enum

class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

class Size(Enum):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3

class Product:
    def __init__(self, name, color, size):
        self.name = name
        self.color = color
        self.size = size

class ProductFilter:
    def filter_by_color(self, products, color):
        for p in products:
            if p.color == color:
                yield p

    def filter_by_size(self, products, size):
        for p in products:
            if p.size == size:
                yield p
    
    # We just violated the OCP, OCP says that we should be able to extend the functionality of a class without modifying it.

    def filter_by_size_and_color(self, products, size, color):
        for p in products:
            if p.size == size and p.color == color:
                yield p
    
    # What if we want to filter by size or color?
    # What if we want to filter by size and color or just by size or just by color?
    # What if we want to add more filters?
    # What if we want to AND more than two filters together?
    # What if we want to OR filters together?

    # The solution is to use specification pattern
    # We create a specification class that can be combined together using and/or
    # We create a filter class that takes a specification

# ^^ BEFORE

# Specification is a class that can check if an item satisfies a criteria
#  This is just a base class, we are gonna extend it 
class Specification:
    def is_satisfied(self, item):
        pass

    def __and__(self, other):
        return AndSpecification(self, other)

# This is a base class, we are gonna extend it
class Filter:
    def filter(self, items, spec):
        pass

# This is a concrete class that implements the specification
class ColorSpecification(Specification):
    def __init__(self, color):
        self.color = color

    def is_satisfied(self, item):
        return item.color == self.color

class SizeSpecification(Specification):
    def __init__(self, size):
        self.size = size

    def is_satisfied(self, item):
        return item.size == self.size

class AndSpecification(Specification):
    def __init__(self, *args):
        self.args = args

    def is_satisfied(self, item):
        return all(map(
            lambda spec: spec.is_satisfied(item), self.args
        ))

class BetterFilter(Filter):
    def filter(self, items, spec):
        for i in items:
            if spec.is_satisfied(i):
                yield i

# ^^ AFTER

if __name__ == "__main__":
    apple = Product("Apple", Color.GREEN, Size.SMALL)
    tree = Product("Tree", Color.GREEN, Size.LARGE)
    house = Product("House", Color.BLUE, Size.LARGE)

    products = [apple, tree, house]

    pf = ProductFilter()
    print("Green products (old):")
    for p in pf.filter_by_color(products, Color.GREEN):
        print(f" - {p.name} is green")

    bf = BetterFilter()
    print("Green products (new):")
    green = ColorSpecification(Color.GREEN)
    for p in bf.filter(products, green):
        print(f" - {p.name} is green")

    print("Large products:")
    large = SizeSpecification(Size.LARGE)
    for p in bf.filter(products, large):
        print(f" - {p.name} is large")

    print("Large blue items:")
    large_blue = AndSpecification(large, ColorSpecification(Color.BLUE))
    for p in bf.filter(products, large_blue):
        print(f" - {p.name} is large and blue")

# Output:
# Green products (old):
#  - Apple is green
# Green products (new):
#  - Apple is green
#  - Tree is green
# Large products:
#  - Tree is large
#  - House is large
# Large blue items:
#  - House is large and blue

# Path: Design Patterns/Solid Principles/3.Liskov Substitution Principle.py
# Compare this snippet from Design Patterns/Solid Principles/1.Single Responsibilty Principe.py:
# # SRP
# # Separation of concerns
#
#
# # A class should have only one responsibility
#
#
# class Journal:
#     def __init__(self):
#         self.entries = []
#         self.count = 0
#
#     def add_entry(self, text):
#         self.count += 1
#         self.entries.append(f"{self.count}: {text}")
#
#     def remove_entry(self, pos):
#         del self.entries[pos]
#
#     def __str__(self):
#        return "\n".join(self.entries)

# And this snippet from Design Patterns/Solid Principles/2.Open Closed Principle.py:
# # OCP
# # Open for extension, closed for modification
