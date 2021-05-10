"""
This type stub file was generated by pyright.
"""

from abc import ABCMeta
from nltk.probability import ProbabilisticMixIn

"""
Class for representing hierarchical language structures, such as
syntax trees and morphological trees.
"""
class Tree(list):
    r"""
    A Tree represents a hierarchical grouping of leaves and subtrees.
    For example, each constituent in a syntax tree is represented by a single Tree.

    A tree's children are encoded as a list of leaves and subtrees,
    where a leaf is a basic (non-tree) value; and a subtree is a
    nested Tree.

        >>> from nltk.tree import Tree
        >>> print(Tree(1, [2, Tree(3, [4]), 5]))
        (1 2 (3 4) 5)
        >>> vp = Tree('VP', [Tree('V', ['saw']),
        ...                  Tree('NP', ['him'])])
        >>> s = Tree('S', [Tree('NP', ['I']), vp])
        >>> print(s)
        (S (NP I) (VP (V saw) (NP him)))
        >>> print(s[1])
        (VP (V saw) (NP him))
        >>> print(s[1,1])
        (NP him)
        >>> t = Tree.fromstring("(S (NP I) (VP (V saw) (NP him)))")
        >>> s == t
        True
        >>> t[1][1].set_label('X')
        >>> t[1][1].label()
        'X'
        >>> print(t)
        (S (NP I) (VP (V saw) (X him)))
        >>> t[0], t[1,1] = t[1,1], t[0]
        >>> print(t)
        (S (X him) (VP (V saw) (NP I)))

    The length of a tree is the number of children it has.

        >>> len(t)
        2

    The set_label() and label() methods allow individual constituents
    to be labeled.  For example, syntax trees use this label to specify
    phrase tags, such as "NP" and "VP".

    Several Tree methods use "tree positions" to specify
    children or descendants of a tree.  Tree positions are defined as
    follows:

      - The tree position *i* specifies a Tree's *i*\ th child.
      - The tree position ``()`` specifies the Tree itself.
      - If *p* is the tree position of descendant *d*, then
        *p+i* specifies the *i*\ th child of *d*.

    I.e., every tree position is either a single index *i*,
    specifying ``tree[i]``; or a sequence *i1, i2, ..., iN*,
    specifying ``tree[i1][i2]...[iN]``.

    Construct a new tree.  This constructor can be called in one
    of two ways:

    - ``Tree(label, children)`` constructs a new tree with the
        specified label and list of children.

    - ``Tree.fromstring(s)`` constructs a new tree by parsing the string ``s``.
    """
    def __init__(self, node, children=...) -> None:
        ...
    
    def __eq__(self, other) -> bool:
        ...
    
    def __lt__(self, other) -> bool:
        ...
    
    __ne__ = ...
    __gt__ = ...
    __le__ = ...
    __ge__ = ...
    def __mul__(self, v):
        ...
    
    def __rmul__(self, v):
        ...
    
    def __add__(self, v):
        ...
    
    def __radd__(self, v):
        ...
    
    def __getitem__(self, index):
        ...
    
    def __setitem__(self, index, value):
        ...
    
    def __delitem__(self, index):
        ...
    
    node = ...
    def label(self):
        """
        Return the node label of the tree.

            >>> t = Tree.fromstring('(S (NP (D the) (N dog)) (VP (V chased) (NP (D the) (N cat))))')
            >>> t.label()
            'S'

        :return: the node label (typically a string)
        :rtype: any
        """
        ...
    
    def set_label(self, label):
        """
        Set the node label of the tree.

            >>> t = Tree.fromstring("(S (NP (D the) (N dog)) (VP (V chased) (NP (D the) (N cat))))")
            >>> t.set_label("T")
            >>> print(t)
            (T (NP (D the) (N dog)) (VP (V chased) (NP (D the) (N cat))))

        :param label: the node label (typically a string)
        :type label: any
        """
        ...
    
    def leaves(self):
        """
        Return the leaves of the tree.

            >>> t = Tree.fromstring("(S (NP (D the) (N dog)) (VP (V chased) (NP (D the) (N cat))))")
            >>> t.leaves()
            ['the', 'dog', 'chased', 'the', 'cat']

        :return: a list containing this tree's leaves.
            The order reflects the order of the
            leaves in the tree's hierarchical structure.
        :rtype: list
        """
        ...
    
    def flatten(self):
        """
        Return a flat version of the tree, with all non-root non-terminals removed.

            >>> t = Tree.fromstring("(S (NP (D the) (N dog)) (VP (V chased) (NP (D the) (N cat))))")
            >>> print(t.flatten())
            (S the dog chased the cat)

        :return: a tree consisting of this tree's root connected directly to
            its leaves, omitting all intervening non-terminal nodes.
        :rtype: Tree
        """
        ...
    
    def height(self):
        """
        Return the height of the tree.

            >>> t = Tree.fromstring("(S (NP (D the) (N dog)) (VP (V chased) (NP (D the) (N cat))))")
            >>> t.height()
            5
            >>> print(t[0,0])
            (D the)
            >>> t[0,0].height()
            2

        :return: The height of this tree.  The height of a tree
            containing no children is 1; the height of a tree
            containing only leaves is 2; and the height of any other
            tree is one plus the maximum of its children's
            heights.
        :rtype: int
        """
        ...
    
    def treepositions(self, order=...):
        """
            >>> t = Tree.fromstring("(S (NP (D the) (N dog)) (VP (V chased) (NP (D the) (N cat))))")
            >>> t.treepositions() # doctest: +ELLIPSIS
            [(), (0,), (0, 0), (0, 0, 0), (0, 1), (0, 1, 0), (1,), (1, 0), (1, 0, 0), ...]
            >>> for pos in t.treepositions('leaves'):
            ...     t[pos] = t[pos][::-1].upper()
            >>> print(t)
            (S (NP (D EHT) (N GOD)) (VP (V DESAHC) (NP (D EHT) (N TAC))))

        :param order: One of: ``preorder``, ``postorder``, ``bothorder``,
            ``leaves``.
        """
        ...
    
    def subtrees(self, filter=...):
        """
        Generate all the subtrees of this tree, optionally restricted
        to trees matching the filter function.

            >>> t = Tree.fromstring("(S (NP (D the) (N dog)) (VP (V chased) (NP (D the) (N cat))))")
            >>> for s in t.subtrees(lambda t: t.height() == 2):
            ...     print(s)
            (D the)
            (N dog)
            (V chased)
            (D the)
            (N cat)

        :type filter: function
        :param filter: the function to filter all local trees
        """
        ...
    
    def productions(self):
        """
        Generate the productions that correspond to the non-terminal nodes of the tree.
        For each subtree of the form (P: C1 C2 ... Cn) this produces a production of the
        form P -> C1 C2 ... Cn.

            >>> t = Tree.fromstring("(S (NP (D the) (N dog)) (VP (V chased) (NP (D the) (N cat))))")
            >>> t.productions()
            [S -> NP VP, NP -> D N, D -> 'the', N -> 'dog', VP -> V NP, V -> 'chased',
            NP -> D N, D -> 'the', N -> 'cat']

        :rtype: list(Production)
        """
        ...
    
    def pos(self):
        """
        Return a sequence of pos-tagged words extracted from the tree.

            >>> t = Tree.fromstring("(S (NP (D the) (N dog)) (VP (V chased) (NP (D the) (N cat))))")
            >>> t.pos()
            [('the', 'D'), ('dog', 'N'), ('chased', 'V'), ('the', 'D'), ('cat', 'N')]

        :return: a list of tuples containing leaves and pre-terminals (part-of-speech tags).
            The order reflects the order of the leaves in the tree's hierarchical structure.
        :rtype: list(tuple)
        """
        ...
    
    def leaf_treeposition(self, index):
        """
        :return: The tree position of the ``index``-th leaf in this
            tree.  I.e., if ``tp=self.leaf_treeposition(i)``, then
            ``self[tp]==self.leaves()[i]``.

        :raise IndexError: If this tree contains fewer than ``index+1``
            leaves, or if ``index<0``.
        """
        ...
    
    def treeposition_spanning_leaves(self, start, end):
        """
        :return: The tree position of the lowest descendant of this
            tree that dominates ``self.leaves()[start:end]``.
        :raise ValueError: if ``end <= start``
        """
        ...
    
    def chomsky_normal_form(self, factor=..., horzMarkov=..., vertMarkov=..., childChar=..., parentChar=...):
        """
        This method can modify a tree in three ways:

          1. Convert a tree into its Chomsky Normal Form (CNF)
             equivalent -- Every subtree has either two non-terminals
             or one terminal as its children.  This process requires
             the creation of more"artificial" non-terminal nodes.
          2. Markov (vertical) smoothing of children in new artificial
             nodes
          3. Horizontal (parent) annotation of nodes

        :param factor: Right or left factoring method (default = "right")
        :type  factor: str = [left|right]
        :param horzMarkov: Markov order for sibling smoothing in artificial nodes (None (default) = include all siblings)
        :type  horzMarkov: int | None
        :param vertMarkov: Markov order for parent smoothing (0 (default) = no vertical annotation)
        :type  vertMarkov: int | None
        :param childChar: A string used in construction of the artificial nodes, separating the head of the
                          original subtree from the child nodes that have yet to be expanded (default = "|")
        :type  childChar: str
        :param parentChar: A string used to separate the node representation from its vertical annotation
        :type  parentChar: str
        """
        ...
    
    def un_chomsky_normal_form(self, expandUnary=..., childChar=..., parentChar=..., unaryChar=...):
        """
        This method modifies the tree in three ways:

          1. Transforms a tree in Chomsky Normal Form back to its
             original structure (branching greater than two)
          2. Removes any parent annotation (if it exists)
          3. (optional) expands unary subtrees (if previously
             collapsed with collapseUnary(...) )

        :param expandUnary: Flag to expand unary or not (default = True)
        :type  expandUnary: bool
        :param childChar: A string separating the head node from its children in an artificial node (default = "|")
        :type  childChar: str
        :param parentChar: A sting separating the node label from its parent annotation (default = "^")
        :type  parentChar: str
        :param unaryChar: A string joining two non-terminals in a unary production (default = "+")
        :type  unaryChar: str
        """
        ...
    
    def collapse_unary(self, collapsePOS=..., collapseRoot=..., joinChar=...):
        """
        Collapse subtrees with a single child (ie. unary productions)
        into a new non-terminal (Tree node) joined by 'joinChar'.
        This is useful when working with algorithms that do not allow
        unary productions, and completely removing the unary productions
        would require loss of useful information.  The Tree is modified
        directly (since it is passed by reference) and no value is returned.

        :param collapsePOS: 'False' (default) will not collapse the parent of leaf nodes (ie.
                            Part-of-Speech tags) since they are always unary productions
        :type  collapsePOS: bool
        :param collapseRoot: 'False' (default) will not modify the root production
                             if it is unary.  For the Penn WSJ treebank corpus, this corresponds
                             to the TOP -> productions.
        :type collapseRoot: bool
        :param joinChar: A string used to connect collapsed node values (default = "+")
        :type  joinChar: str
        """
        ...
    
    @classmethod
    def convert(cls, tree):
        """
        Convert a tree between different subtypes of Tree.  ``cls`` determines
        which class will be used to encode the new tree.

        :type tree: Tree
        :param tree: The tree that should be converted.
        :return: The new Tree.
        """
        ...
    
    def __copy__(self):
        ...
    
    def __deepcopy__(self, memo):
        ...
    
    def copy(self, deep=...):
        ...
    
    def freeze(self, leaf_freezer=...):
        ...
    
    @classmethod
    def fromstring(cls, s, brackets=..., read_node=..., read_leaf=..., node_pattern=..., leaf_pattern=..., remove_empty_top_bracketing=...):
        """
        Read a bracketed tree string and return the resulting tree.
        Trees are represented as nested brackettings, such as::

          (S (NP (NNP John)) (VP (V runs)))

        :type s: str
        :param s: The string to read

        :type brackets: str (length=2)
        :param brackets: The bracket characters used to mark the
            beginning and end of trees and subtrees.

        :type read_node: function
        :type read_leaf: function
        :param read_node, read_leaf: If specified, these functions
            are applied to the substrings of ``s`` corresponding to
            nodes and leaves (respectively) to obtain the values for
            those nodes and leaves.  They should have the following
            signature:

               read_node(str) -> value

            For example, these functions could be used to process nodes
            and leaves whose values should be some type other than
            string (such as ``FeatStruct``).
            Note that by default, node strings and leaf strings are
            delimited by whitespace and brackets; to override this
            default, use the ``node_pattern`` and ``leaf_pattern``
            arguments.

        :type node_pattern: str
        :type leaf_pattern: str
        :param node_pattern, leaf_pattern: Regular expression patterns
            used to find node and leaf substrings in ``s``.  By
            default, both nodes patterns are defined to match any
            sequence of non-whitespace non-bracket characters.

        :type remove_empty_top_bracketing: bool
        :param remove_empty_top_bracketing: If the resulting tree has
            an empty node label, and is length one, then return its
            single child instead.  This is useful for treebank trees,
            which sometimes contain an extra level of bracketing.

        :return: A tree corresponding to the string representation ``s``.
            If this class method is called using a subclass of Tree,
            then it will return a tree of that type.
        :rtype: Tree
        """
        ...
    
    @classmethod
    def fromlist(cls, l):
        """
        :type l: list
        :param l: a tree represented as nested lists

        :return: A tree corresponding to the list representation ``l``.
        :rtype: Tree

        Convert nested lists to a NLTK Tree
        """
        ...
    
    def draw(self):
        """
        Open a new window containing a graphical diagram of this tree.
        """
        ...
    
    def pretty_print(self, sentence=..., highlight=..., stream=..., **kwargs):
        """
        Pretty-print this tree as ASCII or Unicode art.
        For explanation of the arguments, see the documentation for
        `nltk.treeprettyprinter.TreePrettyPrinter`.
        """
        ...
    
    def __repr__(self):
        ...
    
    def __str__(self) -> str:
        ...
    
    def pprint(self, **kwargs):
        """
        Print a string representation of this Tree to 'stream'
        """
        ...
    
    def pformat(self, margin=..., indent=..., nodesep=..., parens=..., quotes=...):
        """
        :return: A pretty-printed string representation of this tree.
        :rtype: str
        :param margin: The right margin at which to do line-wrapping.
        :type margin: int
        :param indent: The indentation level at which printing
            begins.  This number is used to decide how far to indent
            subsequent lines.
        :type indent: int
        :param nodesep: A string that is used to separate the node
            from the children.  E.g., the default value ``':'`` gives
            trees like ``(S: (NP: I) (VP: (V: saw) (NP: it)))``.
        """
        ...
    
    def pformat_latex_qtree(self):
        r"""
        Returns a representation of the tree compatible with the
        LaTeX qtree package. This consists of the string ``\Tree``
        followed by the tree represented in bracketed notation.

        For example, the following result was generated from a parse tree of
        the sentence ``The announcement astounded us``::

          \Tree [.I'' [.N'' [.D The ] [.N' [.N announcement ] ] ]
              [.I' [.V'' [.V' [.V astounded ] [.N'' [.N' [.N us ] ] ] ] ] ] ]

        See http://www.ling.upenn.edu/advice/latex.html for the LaTeX
        style file for the qtree package.

        :return: A latex qtree representation of this tree.
        :rtype: str
        """
        ...
    


class ImmutableTree(Tree):
    def __init__(self, node, children=...) -> None:
        ...
    
    def __setitem__(self, index, value):
        ...
    
    def __setslice__(self, i, j, value):
        ...
    
    def __delitem__(self, index):
        ...
    
    def __delslice__(self, i, j):
        ...
    
    def __iadd__(self, other):
        ...
    
    def __imul__(self, other):
        ...
    
    def append(self, v):
        ...
    
    def extend(self, v):
        ...
    
    def pop(self, v=...):
        ...
    
    def remove(self, v):
        ...
    
    def reverse(self):
        ...
    
    def sort(self):
        ...
    
    def __hash__(self) -> int:
        ...
    
    def set_label(self, value):
        """
        Set the node label.  This will only succeed the first time the
        node label is set, which should occur in ImmutableTree.__init__().
        """
        ...
    


class AbstractParentedTree(Tree, metaclass=ABCMeta):
    """
    An abstract base class for a ``Tree`` that automatically maintains
    pointers to parent nodes.  These parent pointers are updated
    whenever any change is made to a tree's structure.  Two subclasses
    are currently defined:

      - ``ParentedTree`` is used for tree structures where each subtree
        has at most one parent.  This class should be used in cases
        where there is no"sharing" of subtrees.

      - ``MultiParentedTree`` is used for tree structures where a
        subtree may have zero or more parents.  This class should be
        used in cases where subtrees may be shared.

    Subclassing
    ===========
    The ``AbstractParentedTree`` class redefines all operations that
    modify a tree's structure to call two methods, which are used by
    subclasses to update parent information:

      - ``_setparent()`` is called whenever a new child is added.
      - ``_delparent()`` is called whenever a child is removed.
    """
    def __init__(self, node, children=...) -> None:
        ...
    
    def __delitem__(self, index):
        ...
    
    def __setitem__(self, index, value):
        ...
    
    def append(self, child):
        ...
    
    def extend(self, children):
        ...
    
    def insert(self, index, child):
        ...
    
    def pop(self, index=...):
        ...
    
    def remove(self, child):
        ...
    
    if hasattr(list, "__getslice__"):
        def __getslice__(self, start, stop):
            ...
        
        def __delslice__(self, start, stop):
            ...
        
        def __setslice__(self, start, stop, value):
            ...
        


class ParentedTree(AbstractParentedTree):
    """
    A ``Tree`` that automatically maintains parent pointers for
    single-parented trees.  The following are methods for querying
    the structure of a parented tree: ``parent``, ``parent_index``,
    ``left_sibling``, ``right_sibling``, ``root``, ``treeposition``.

    Each ``ParentedTree`` may have at most one parent.  In
    particular, subtrees may not be shared.  Any attempt to reuse a
    single ``ParentedTree`` as a child of more than one parent (or
    as multiple children of the same parent) will cause a
    ``ValueError`` exception to be raised.

    ``ParentedTrees`` should never be used in the same tree as ``Trees``
    or ``MultiParentedTrees``.  Mixing tree implementations may result
    in incorrect parent pointers and in ``TypeError`` exceptions.
    """
    def __init__(self, node, children=...) -> None:
        ...
    
    def parent(self):
        """The parent of this tree, or None if it has no parent."""
        ...
    
    def parent_index(self):
        """
        The index of this tree in its parent.  I.e.,
        ``ptree.parent()[ptree.parent_index()] is ptree``.  Note that
        ``ptree.parent_index()`` is not necessarily equal to
        ``ptree.parent.index(ptree)``, since the ``index()`` method
        returns the first child that is equal to its argument.
        """
        ...
    
    def left_sibling(self):
        """The left sibling of this tree, or None if it has none."""
        ...
    
    def right_sibling(self):
        """The right sibling of this tree, or None if it has none."""
        ...
    
    def root(self):
        """
        The root of this tree.  I.e., the unique ancestor of this tree
        whose parent is None.  If ``ptree.parent()`` is None, then
        ``ptree`` is its own root.
        """
        ...
    
    def treeposition(self):
        """
        The tree position of this tree, relative to the root of the
        tree.  I.e., ``ptree.root[ptree.treeposition] is ptree``.
        """
        ...
    


class MultiParentedTree(AbstractParentedTree):
    """
    A ``Tree`` that automatically maintains parent pointers for
    multi-parented trees.  The following are methods for querying the
    structure of a multi-parented tree: ``parents()``, ``parent_indices()``,
    ``left_siblings()``, ``right_siblings()``, ``roots``, ``treepositions``.

    Each ``MultiParentedTree`` may have zero or more parents.  In
    particular, subtrees may be shared.  If a single
    ``MultiParentedTree`` is used as multiple children of the same
    parent, then that parent will appear multiple times in its
    ``parents()`` method.

    ``MultiParentedTrees`` should never be used in the same tree as
    ``Trees`` or ``ParentedTrees``.  Mixing tree implementations may
    result in incorrect parent pointers and in ``TypeError`` exceptions.
    """
    def __init__(self, node, children=...) -> None:
        ...
    
    def parents(self):
        """
        The set of parents of this tree.  If this tree has no parents,
        then ``parents`` is the empty set.  To check if a tree is used
        as multiple children of the same parent, use the
        ``parent_indices()`` method.

        :type: list(MultiParentedTree)
        """
        ...
    
    def left_siblings(self):
        """
        A list of all left siblings of this tree, in any of its parent
        trees.  A tree may be its own left sibling if it is used as
        multiple contiguous children of the same parent.  A tree may
        appear multiple times in this list if it is the left sibling
        of this tree with respect to multiple parents.

        :type: list(MultiParentedTree)
        """
        ...
    
    def right_siblings(self):
        """
        A list of all right siblings of this tree, in any of its parent
        trees.  A tree may be its own right sibling if it is used as
        multiple contiguous children of the same parent.  A tree may
        appear multiple times in this list if it is the right sibling
        of this tree with respect to multiple parents.

        :type: list(MultiParentedTree)
        """
        ...
    
    def roots(self):
        """
        The set of all roots of this tree.  This set is formed by
        tracing all possible parent paths until trees with no parents
        are found.

        :type: list(MultiParentedTree)
        """
        ...
    
    def parent_indices(self, parent):
        """
        Return a list of the indices where this tree occurs as a child
        of ``parent``.  If this child does not occur as a child of
        ``parent``, then the empty list is returned.  The following is
        always true::

          for parent_index in ptree.parent_indices(parent):
              parent[parent_index] is ptree
        """
        ...
    
    def treepositions(self, root):
        """
        Return a list of all tree positions that can be used to reach
        this multi-parented tree starting from ``root``.  I.e., the
        following is always true::

          for treepos in ptree.treepositions(root):
              root[treepos] is ptree
        """
        ...
    


class ImmutableParentedTree(ImmutableTree, ParentedTree):
    ...


class ImmutableMultiParentedTree(ImmutableTree, MultiParentedTree):
    ...


class ProbabilisticTree(Tree, ProbabilisticMixIn):
    def __init__(self, node, children=..., **prob_kwargs) -> None:
        ...
    
    def __repr__(self):
        ...
    
    def __str__(self) -> str:
        ...
    
    def copy(self, deep=...):
        ...
    
    @classmethod
    def convert(cls, val):
        ...
    
    def __eq__(self, other) -> bool:
        ...
    
    def __lt__(self, other) -> bool:
        ...
    


class ImmutableProbabilisticTree(ImmutableTree, ProbabilisticMixIn):
    def __init__(self, node, children=..., **prob_kwargs) -> None:
        ...
    
    def __repr__(self):
        ...
    
    def __str__(self) -> str:
        ...
    
    def copy(self, deep=...):
        ...
    
    @classmethod
    def convert(cls, val):
        ...
    


def bracket_parse(s):
    """
    Use Tree.read(s, remove_empty_top_bracketing=True) instead.
    """
    ...

def sinica_parse(s):
    """
    Parse a Sinica Treebank string and return a tree.  Trees are represented as nested brackettings,
    as shown in the following example (X represents a Chinese character):
    S(goal:NP(Head:Nep:XX)|theme:NP(Head:Nhaa:X)|quantity:Dab:X|Head:VL2:X)#0(PERIODCATEGORY)

    :return: A tree corresponding to the string representation.
    :rtype: Tree
    :param s: The string to be converted
    :type s: str
    """
    ...

def demo():
    """
    A demonstration showing how Trees and Trees can be
    used.  This demonstration creates a Tree, and loads a
    Tree from the Treebank corpus,
    and shows the results of calling several of their methods.
    """
    ...

