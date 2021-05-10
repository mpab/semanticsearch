"""
This type stub file was generated by pyright.
"""

class ParserI(object):
    """
    A processing class for deriving trees that represent possible
    structures for a sequence of tokens.  These tree structures are
    known as "parses".  Typically, parsers are used to derive syntax
    trees for sentences.  But parsers can also be used to derive other
    kinds of tree structure, such as morphological trees and discourse
    structures.

    Subclasses must define:
      - at least one of: ``parse()``, ``parse_sents()``.

    Subclasses may define:
      - ``grammar()``
    """
    def grammar(self):
        """
        :return: The grammar used by this parser.
        """
        ...
    
    def parse(self, sent, *args, **kwargs):
        """
        :return: An iterator that generates parse trees for the sentence.
        When possible this list is sorted from most likely to least likely.

        :param sent: The sentence to be parsed
        :type sent: list(str)
        :rtype: iter(Tree)
        """
        ...
    
    def parse_sents(self, sents, *args, **kwargs):
        """
        Apply ``self.parse()`` to each element of ``sents``.
        :rtype: iter(iter(Tree))
        """
        ...
    
    def parse_all(self, sent, *args, **kwargs):
        """:rtype: list(Tree)"""
        ...
    
    def parse_one(self, sent, *args, **kwargs):
        """:rtype: Tree or None"""
        ...
    


