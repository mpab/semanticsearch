"""
This type stub file was generated by pyright.
"""

from abc import ABCMeta, abstractmethod

"""
CCG Combinators
"""
class UndirectedBinaryCombinator(metaclass=ABCMeta):
    """
    Abstract class for representing a binary combinator.
    Merely defines functions for checking if the function and argument
    are able to be combined, and what the resulting category is.

    Note that as no assumptions are made as to direction, the unrestricted
    combinators can perform all backward, forward and crossed variations
    of the combinators; these restrictions must be added in the rule
    class.
    """
    @abstractmethod
    def can_combine(self, function, argument):
        ...
    
    @abstractmethod
    def combine(self, function, argument):
        ...
    


class DirectedBinaryCombinator(metaclass=ABCMeta):
    """
    Wrapper for the undirected binary combinator.
    It takes left and right categories, and decides which is to be
    the function, and which the argument.
    It then decides whether or not they can be combined.
    """
    @abstractmethod
    def can_combine(self, left, right):
        ...
    
    @abstractmethod
    def combine(self, left, right):
        ...
    


class ForwardCombinator(DirectedBinaryCombinator):
    """
    Class representing combinators where the primary functor is on the left.

    Takes an undirected combinator, and a predicate which adds constraints
    restricting the cases in which it may apply.
    """
    def __init__(self, combinator, predicate, suffix=...) -> None:
        ...
    
    def can_combine(self, left, right):
        ...
    
    def combine(self, left, right):
        ...
    
    def __str__(self) -> str:
        ...
    


class BackwardCombinator(DirectedBinaryCombinator):
    """
    The backward equivalent of the ForwardCombinator class.
    """
    def __init__(self, combinator, predicate, suffix=...) -> None:
        ...
    
    def can_combine(self, left, right):
        ...
    
    def combine(self, left, right):
        ...
    
    def __str__(self) -> str:
        ...
    


class UndirectedFunctionApplication(UndirectedBinaryCombinator):
    """
    Class representing function application.
    Implements rules of the form:
    X/Y Y -> X (>)
    And the corresponding backwards application rule
    """
    def can_combine(self, function, argument):
        ...
    
    def combine(self, function, argument):
        ...
    
    def __str__(self) -> str:
        ...
    


def forwardOnly(left, right):
    ...

def backwardOnly(left, right):
    ...

ForwardApplication = ...
BackwardApplication = ...
class UndirectedComposition(UndirectedBinaryCombinator):
    """
    Functional composition (harmonic) combinator.
    Implements rules of the form
    X/Y Y/Z -> X/Z (B>)
    And the corresponding backwards and crossed variations.
    """
    def can_combine(self, function, argument):
        ...
    
    def combine(self, function, argument):
        ...
    
    def __str__(self) -> str:
        ...
    


def bothForward(left, right):
    ...

def bothBackward(left, right):
    ...

def crossedDirs(left, right):
    ...

def backwardBxConstraint(left, right):
    ...

ForwardComposition = ...
BackwardComposition = ...
BackwardBx = ...
class UndirectedSubstitution(UndirectedBinaryCombinator):
    r"""
    Substitution (permutation) combinator.
    Implements rules of the form
    Y/Z (X\Y)/Z -> X/Z (<Sx)
    And other variations.
    """
    def can_combine(self, function, argument):
        ...
    
    def combine(self, function, argument):
        ...
    
    def __str__(self) -> str:
        ...
    


def forwardSConstraint(left, right):
    ...

def backwardSxConstraint(left, right):
    ...

ForwardSubstitution = ...
BackwardSx = ...
def innermostFunction(categ):
    ...

class UndirectedTypeRaise(UndirectedBinaryCombinator):
    """
    Undirected combinator for type raising.
    """
    def can_combine(self, function, arg):
        ...
    
    def combine(self, function, arg):
        ...
    
    def __str__(self) -> str:
        ...
    


def forwardTConstraint(left, right):
    ...

def backwardTConstraint(left, right):
    ...

ForwardT = ...
BackwardT = ...
