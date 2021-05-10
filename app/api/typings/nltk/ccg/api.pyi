"""
This type stub file was generated by pyright.
"""

from functools import total_ordering
from abc import ABCMeta, abstractmethod

@total_ordering
class AbstractCCGCategory(metaclass=ABCMeta):
    """
    Interface for categories in combinatory grammars.
    """
    @abstractmethod
    def is_primitive(self):
        """
        Returns true if the category is primitive.
        """
        ...
    
    @abstractmethod
    def is_function(self):
        """
        Returns true if the category is a function application.
        """
        ...
    
    @abstractmethod
    def is_var(self):
        """
        Returns true if the category is a variable.
        """
        ...
    
    @abstractmethod
    def substitute(self, substitutions):
        """
        Takes a set of (var, category) substitutions, and replaces every
        occurrence of the variable with the corresponding category.
        """
        ...
    
    @abstractmethod
    def can_unify(self, other):
        """
        Determines whether two categories can be unified.
         - Returns None if they cannot be unified
         - Returns a list of necessary substitutions if they can.
        """
        ...
    
    @abstractmethod
    def __str__(self) -> str:
        ...
    
    def __eq__(self, other) -> bool:
        ...
    
    def __ne__(self, other) -> bool:
        ...
    
    def __lt__(self, other) -> bool:
        ...
    
    def __hash__(self) -> int:
        ...
    


class CCGVar(AbstractCCGCategory):
    """
    Class representing a variable CCG category.
    Used for conjunctions (and possibly type-raising, if implemented as a
    unary rule).
    """
    _maxID = ...
    def __init__(self, prim_only=...) -> None:
        """Initialize a variable (selects a new identifier)

        :param prim_only: a boolean that determines whether the variable is
                          restricted to primitives
        :type prim_only: bool
        """
        ...
    
    @classmethod
    def new_id(cls):
        """
        A class method allowing generation of unique variable identifiers.
        """
        ...
    
    @classmethod
    def reset_id(cls):
        ...
    
    def is_primitive(self):
        ...
    
    def is_function(self):
        ...
    
    def is_var(self):
        ...
    
    def substitute(self, substitutions):
        """If there is a substitution corresponding to this variable,
        return the substituted category.
        """
        ...
    
    def can_unify(self, other):
        """ If the variable can be replaced with other
        a substitution is returned.
        """
        ...
    
    def id(self):
        ...
    
    def __str__(self) -> str:
        ...
    


@total_ordering
class Direction(object):
    """
    Class representing the direction of a function application.
    Also contains maintains information as to which combinators
    may be used with the category.
    """
    def __init__(self, dir, restrictions) -> None:
        ...
    
    def is_forward(self):
        ...
    
    def is_backward(self):
        ...
    
    def dir(self):
        ...
    
    def restrs(self):
        """A list of restrictions on the combinators.
        '.' denotes that permuting operations are disallowed
        ',' denotes that function composition is disallowed
        '_' denotes that the direction has variable restrictions.
        (This is redundant in the current implementation of type-raising)
        """
        ...
    
    def is_variable(self):
        ...
    
    def can_unify(self, other):
        ...
    
    def substitute(self, subs):
        ...
    
    def can_compose(self):
        ...
    
    def can_cross(self):
        ...
    
    def __eq__(self, other) -> bool:
        ...
    
    def __ne__(self, other) -> bool:
        ...
    
    def __lt__(self, other) -> bool:
        ...
    
    def __hash__(self) -> int:
        ...
    
    def __str__(self) -> str:
        ...
    
    def __neg__(self):
        ...
    


class PrimitiveCategory(AbstractCCGCategory):
    """
    Class representing primitive categories.
    Takes a string representation of the category, and a
    list of strings specifying the morphological subcategories.
    """
    def __init__(self, categ, restrictions=...) -> None:
        ...
    
    def is_primitive(self):
        ...
    
    def is_function(self):
        ...
    
    def is_var(self):
        ...
    
    def restrs(self):
        ...
    
    def categ(self):
        ...
    
    def substitute(self, subs):
        ...
    
    def can_unify(self, other):
        ...
    
    def __str__(self) -> str:
        ...
    


class FunctionalCategory(AbstractCCGCategory):
    """
    Class that represents a function application category.
    Consists of argument and result categories, together with
    an application direction.
    """
    def __init__(self, res, arg, dir) -> None:
        ...
    
    def is_primitive(self):
        ...
    
    def is_function(self):
        ...
    
    def is_var(self):
        ...
    
    def substitute(self, subs):
        ...
    
    def can_unify(self, other):
        ...
    
    def arg(self):
        ...
    
    def res(self):
        ...
    
    def dir(self):
        ...
    
    def __str__(self) -> str:
        ...
    


