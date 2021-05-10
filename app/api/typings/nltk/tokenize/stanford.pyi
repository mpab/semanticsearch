"""
This type stub file was generated by pyright.
"""

from nltk.tokenize.api import TokenizerI

_stanford_url = ...
class StanfordTokenizer(TokenizerI):
    r"""
    Interface to the Stanford Tokenizer

    >>> from nltk.tokenize.stanford import StanfordTokenizer
    >>> s = "Good muffins cost $3.88\nin New York.  Please buy me\ntwo of them.\nThanks."
    >>> StanfordTokenizer().tokenize(s)
    ['Good', 'muffins', 'cost', '$', '3.88', 'in', 'New', 'York', '.', 'Please', 'buy', 'me', 'two', 'of', 'them', '.', 'Thanks', '.']
    >>> s = "The colour of the wall is blue."
    >>> StanfordTokenizer(options={"americanize": True}).tokenize(s)
    ['The', 'color', 'of', 'the', 'wall', 'is', 'blue', '.']
    """
    _JAR = ...
    def __init__(self, path_to_jar=..., encoding=..., options=..., verbose=..., java_options=...) -> None:
        ...
    
    def tokenize(self, s):
        """
        Use stanford tokenizer's PTBTokenizer to tokenize multiple sentences.
        """
        ...
    


