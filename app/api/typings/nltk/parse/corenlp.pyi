"""
This type stub file was generated by pyright.
"""

from nltk.tag.api import TaggerI
from nltk.parse.api import ParserI
from nltk.tokenize.api import TokenizerI

_stanford_url = ...
class CoreNLPServerError(EnvironmentError):
    """Exceptions associated with the Core NLP server."""
    ...


def try_port(port=...):
    ...

class CoreNLPServer(object):
    _MODEL_JAR_PATTERN = ...
    _JAR = ...
    def __init__(self, path_to_jar=..., path_to_models_jar=..., verbose=..., java_options=..., corenlp_options=..., port=...) -> None:
        ...
    
    def start(self, stdout=..., stderr=...):
        """ Starts the CoreNLP server

        :param stdout, stderr: Specifies where CoreNLP output is redirected. Valid values are 'devnull', 'stdout', 'pipe'
        """
        ...
    
    def stop(self):
        ...
    
    def __enter__(self):
        ...
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        ...
    


class GenericCoreNLPParser(ParserI, TokenizerI, TaggerI):
    """Interface to the CoreNLP Parser."""
    def __init__(self, url=..., encoding=..., tagtype=...) -> None:
        ...
    
    def parse_sents(self, sentences, *args, **kwargs):
        """Parse multiple sentences.

        Takes multiple sentences as a list where each sentence is a list of
        words. Each sentence will be automatically tagged with this
        CoreNLPParser instance's tagger.

        If a whitespace exists inside a token, then the token will be treated as
        several tokens.

        :param sentences: Input sentences to parse
        :type sentences: list(list(str))
        :rtype: iter(iter(Tree))
        """
        ...
    
    def raw_parse(self, sentence, properties=..., *args, **kwargs):
        """Parse a sentence.

        Takes a sentence as a string; before parsing, it will be automatically
        tokenized and tagged by the CoreNLP Parser.

        :param sentence: Input sentence to parse
        :type sentence: str
        :rtype: iter(Tree)
        """
        ...
    
    def api_call(self, data, properties=..., timeout=...):
        ...
    
    def raw_parse_sents(self, sentences, verbose=..., properties=..., *args, **kwargs):
        """Parse multiple sentences.

        Takes multiple sentences as a list of strings. Each sentence will be
        automatically tokenized and tagged.

        :param sentences: Input sentences to parse.
        :type sentences: list(str)
        :rtype: iter(iter(Tree))

        """
        ...
    
    def parse_text(self, text, *args, **kwargs):
        """Parse a piece of text.

        The text might contain several sentences which will be split by CoreNLP.

        :param str text: text to be split.
        :returns: an iterable of syntactic structures.  # TODO: should it be an iterable of iterables?

        """
        ...
    
    def tokenize(self, text, properties=...):
        """Tokenize a string of text.

        >>> parser = CoreNLPParser(url='http://localhost:9000')

        >>> text = 'Good muffins cost $3.88\\nin New York.  Please buy me\\ntwo of them.\\nThanks.'
        >>> list(parser.tokenize(text))
        ['Good', 'muffins', 'cost', '$', '3.88', 'in', 'New', 'York', '.', 'Please', 'buy', 'me', 'two', 'of', 'them', '.', 'Thanks', '.']

        >>> s = "The colour of the wall is blue."
        >>> list(
        ...     parser.tokenize(
        ...         'The colour of the wall is blue.',
        ...             properties={'tokenize.options': 'americanize=true'},
        ...     )
        ... )
        ['The', 'color', 'of', 'the', 'wall', 'is', 'blue', '.']

        """
        ...
    
    def tag_sents(self, sentences):
        """
        Tag multiple sentences.

        Takes multiple sentences as a list where each sentence is a list of
        tokens.

        :param sentences: Input sentences to tag
        :type sentences: list(list(str))
        :rtype: list(list(tuple(str, str))
        """
        ...
    
    def tag(self, sentence):
        """
        Tag a list of tokens.

        :rtype: list(tuple(str, str))

        >>> parser = CoreNLPParser(url='http://localhost:9000', tagtype='ner')
        >>> tokens = 'Rami Eid is studying at Stony Brook University in NY'.split()
        >>> parser.tag(tokens)
        [('Rami', 'PERSON'), ('Eid', 'PERSON'), ('is', 'O'), ('studying', 'O'), ('at', 'O'), ('Stony', 'ORGANIZATION'),
        ('Brook', 'ORGANIZATION'), ('University', 'ORGANIZATION'), ('in', 'O'), ('NY', 'O')]

        >>> parser = CoreNLPParser(url='http://localhost:9000', tagtype='pos')
        >>> tokens = "What is the airspeed of an unladen swallow ?".split()
        >>> parser.tag(tokens)
        [('What', 'WP'), ('is', 'VBZ'), ('the', 'DT'),
        ('airspeed', 'NN'), ('of', 'IN'), ('an', 'DT'),
        ('unladen', 'JJ'), ('swallow', 'VB'), ('?', '.')]
        """
        ...
    
    def raw_tag_sents(self, sentences):
        """
        Tag multiple sentences.

        Takes multiple sentences as a list where each sentence is a string.

        :param sentences: Input sentences to tag
        :type sentences: list(str)
        :rtype: list(list(list(tuple(str, str)))
        """
        ...
    


class CoreNLPParser(GenericCoreNLPParser):
    """
    >>> parser = CoreNLPParser(url='http://localhost:9000')

    >>> next(
    ...     parser.raw_parse('The quick brown fox jumps over the lazy dog.')
    ... ).pretty_print()  # doctest: +NORMALIZE_WHITESPACE
                         ROOT
                          |
                          S
           _______________|__________________________
          |                         VP               |
          |                _________|___             |
          |               |             PP           |
          |               |     ________|___         |
          NP              |    |            NP       |
      ____|__________     |    |     _______|____    |
     DT   JJ    JJ   NN  VBZ   IN   DT      JJ   NN  .
     |    |     |    |    |    |    |       |    |   |
    The quick brown fox jumps over the     lazy dog  .

    >>> (parse_fox, ), (parse_wolf, ) = parser.raw_parse_sents(
    ...     [
    ...         'The quick brown fox jumps over the lazy dog.',
    ...         'The quick grey wolf jumps over the lazy fox.',
    ...     ]
    ... )

    >>> parse_fox.pretty_print()  # doctest: +NORMALIZE_WHITESPACE
                         ROOT
                          |
                          S
           _______________|__________________________
          |                         VP               |
          |                _________|___             |
          |               |             PP           |
          |               |     ________|___         |
          NP              |    |            NP       |
      ____|__________     |    |     _______|____    |
     DT   JJ    JJ   NN  VBZ   IN   DT      JJ   NN  .
     |    |     |    |    |    |    |       |    |   |
    The quick brown fox jumps over the     lazy dog  .

    >>> parse_wolf.pretty_print()  # doctest: +NORMALIZE_WHITESPACE
                         ROOT
                          |
                          S
           _______________|__________________________
          |                         VP               |
          |                _________|___             |
          |               |             PP           |
          |               |     ________|___         |
          NP              |    |            NP       |
      ____|_________      |    |     _______|____    |
     DT   JJ   JJ   NN   VBZ   IN   DT      JJ   NN  .
     |    |    |    |     |    |    |       |    |   |
    The quick grey wolf jumps over the     lazy fox  .

    >>> (parse_dog, ), (parse_friends, ) = parser.parse_sents(
    ...     [
    ...         "I 'm a dog".split(),
    ...         "This is my friends ' cat ( the tabby )".split(),
    ...     ]
    ... )

    >>> parse_dog.pretty_print()  # doctest: +NORMALIZE_WHITESPACE
            ROOT
             |
             S
      _______|____
     |            VP
     |    ________|___
     NP  |            NP
     |   |         ___|___
    PRP VBP       DT      NN
     |   |        |       |
     I   'm       a      dog

    >>> parse_friends.pretty_print()  # doctest: +NORMALIZE_WHITESPACE
         ROOT
          |
          S
      ____|___________
     |                VP
     |     ___________|_____________
     |    |                         NP
     |    |                  _______|_________
     |    |                 NP               PRN
     |    |            _____|_______      ____|______________
     NP   |           NP            |    |        NP         |
     |    |     ______|_________    |    |     ___|____      |
     DT  VBZ  PRP$   NNS       POS  NN -LRB-  DT       NN  -RRB-
     |    |    |      |         |   |    |    |        |     |
    This  is   my  friends      '  cat -LRB- the     tabby -RRB-

    >>> parse_john, parse_mary, = parser.parse_text(
    ...     'John loves Mary. Mary walks.'
    ... )

    >>> parse_john.pretty_print()  # doctest: +NORMALIZE_WHITESPACE
          ROOT
           |
           S
      _____|_____________
     |          VP       |
     |      ____|___     |
     NP    |        NP   |
     |     |        |    |
    NNP   VBZ      NNP   .
     |     |        |    |
    John loves     Mary  .

    >>> parse_mary.pretty_print()  # doctest: +NORMALIZE_WHITESPACE
          ROOT
           |
           S
      _____|____
     NP    VP   |
     |     |    |
    NNP   VBZ   .
     |     |    |
    Mary walks  .

    Special cases
    -------------

    >>> next(
    ...     parser.raw_parse(
    ...         'NASIRIYA, Iraq—Iraqi doctors who treated former prisoner of war '
    ...         'Jessica Lynch have angrily dismissed claims made in her biography '
    ...         'that she was raped by her Iraqi captors.'
    ...     )
    ... ).height()
    20

    >>> next(
    ...     parser.raw_parse(
    ...         "The broader Standard & Poor's 500 Index <.SPX> was 0.46 points lower, or "
    ...         '0.05 percent, at 997.02.'
    ...     )
    ... ).height()
    9

    """
    _OUTPUT_FORMAT = ...
    parser_annotator = ...
    def make_tree(self, result):
        ...
    


class CoreNLPDependencyParser(GenericCoreNLPParser):
    """Dependency parser.

    >>> dep_parser = CoreNLPDependencyParser(url='http://localhost:9000')

    >>> parse, = dep_parser.raw_parse(
    ...     'The quick brown fox jumps over the lazy dog.'
    ... )
    >>> print(parse.to_conll(4))  # doctest: +NORMALIZE_WHITESPACE
    The     DT      4       det
    quick   JJ      4       amod
    brown   JJ      4       amod
    fox     NN      5       nsubj
    jumps   VBZ     0       ROOT
    over    IN      9       case
    the     DT      9       det
    lazy    JJ      9       amod
    dog     NN      5       nmod
    .       .       5       punct

    >>> print(parse.tree())  # doctest: +NORMALIZE_WHITESPACE
    (jumps (fox The quick brown) (dog over the lazy) .)

    >>> for governor, dep, dependent in parse.triples():
    ...     print(governor, dep, dependent)  # doctest: +NORMALIZE_WHITESPACE
        ('jumps', 'VBZ') nsubj ('fox', 'NN')
        ('fox', 'NN') det ('The', 'DT')
        ('fox', 'NN') amod ('quick', 'JJ')
        ('fox', 'NN') amod ('brown', 'JJ')
        ('jumps', 'VBZ') nmod ('dog', 'NN')
        ('dog', 'NN') case ('over', 'IN')
        ('dog', 'NN') det ('the', 'DT')
        ('dog', 'NN') amod ('lazy', 'JJ')
        ('jumps', 'VBZ') punct ('.', '.')

    >>> (parse_fox, ), (parse_dog, ) = dep_parser.raw_parse_sents(
    ...     [
    ...         'The quick brown fox jumps over the lazy dog.',
    ...         'The quick grey wolf jumps over the lazy fox.',
    ...     ]
    ... )
    >>> print(parse_fox.to_conll(4))  # doctest: +NORMALIZE_WHITESPACE
    The DT      4       det
    quick       JJ      4       amod
    brown       JJ      4       amod
    fox NN      5       nsubj
    jumps       VBZ     0       ROOT
    over        IN      9       case
    the DT      9       det
    lazy        JJ      9       amod
    dog NN      5       nmod
    .   .       5       punct

    >>> print(parse_dog.to_conll(4))  # doctest: +NORMALIZE_WHITESPACE
    The DT      4       det
    quick       JJ      4       amod
    grey        JJ      4       amod
    wolf        NN      5       nsubj
    jumps       VBZ     0       ROOT
    over        IN      9       case
    the DT      9       det
    lazy        JJ      9       amod
    fox NN      5       nmod
    .   .       5       punct

    >>> (parse_dog, ), (parse_friends, ) = dep_parser.parse_sents(
    ...     [
    ...         "I 'm a dog".split(),
    ...         "This is my friends ' cat ( the tabby )".split(),
    ...     ]
    ... )
    >>> print(parse_dog.to_conll(4))  # doctest: +NORMALIZE_WHITESPACE
    I   PRP     4       nsubj
    'm  VBP     4       cop
    a   DT      4       det
    dog NN      0       ROOT

    >>> print(parse_friends.to_conll(4))  # doctest: +NORMALIZE_WHITESPACE
    This        DT      6       nsubj
    is  VBZ     6       cop
    my  PRP$    4       nmod:poss
    friends     NNS     6       nmod:poss
    '   POS     4       case
    cat NN      0       ROOT
    -LRB-       -LRB-   9       punct
    the DT      9       det
    tabby       NN      6       appos
    -RRB-       -RRB-   9       punct

    >>> parse_john, parse_mary, = dep_parser.parse_text(
    ...     'John loves Mary. Mary walks.'
    ... )

    >>> print(parse_john.to_conll(4))  # doctest: +NORMALIZE_WHITESPACE
    John        NNP     2       nsubj
    loves       VBZ     0       ROOT
    Mary        NNP     2       dobj
    .   .       2       punct

    >>> print(parse_mary.to_conll(4))  # doctest: +NORMALIZE_WHITESPACE
    Mary        NNP     2       nsubj
    walks       VBZ     0       ROOT
    .   .       2       punct

    Special cases
    -------------

    Non-breaking space inside of a token.

    >>> len(
    ...     next(
    ...         dep_parser.raw_parse(
    ...             'Anhalt said children typically treat a 20-ounce soda bottle as one '
    ...             'serving, while it actually contains 2 1/2 servings.'
    ...         )
    ...     ).nodes
    ... )
    21

    Phone  numbers.

    >>> len(
    ...     next(
    ...         dep_parser.raw_parse('This is not going to crash: 01 111 555.')
    ...     ).nodes
    ... )
    10

    >>> print(
    ...     next(
    ...         dep_parser.raw_parse('The underscore _ should not simply disappear.')
    ...     ).to_conll(4)
    ... )  # doctest: +NORMALIZE_WHITESPACE
    The         DT  3   det
    underscore  VBP 3   amod
    _           NN  7   nsubj
    should      MD  7   aux
    not         RB  7   neg
    simply      RB  7   advmod
    disappear   VB  0   ROOT
    .           .   7   punct

    >>> print(
    ...     '\\n'.join(
    ...         next(
    ...             dep_parser.raw_parse(
    ...                 'for all of its insights into the dream world of teen life , and its electronic expression through '
    ...                 'cyber culture , the film gives no quarter to anyone seeking to pull a cohesive story out of its 2 '
    ...                 '1/2-hour running time .'
    ...             )
    ...         ).to_conll(4).split('\\n')[-8:]
    ...     )
    ... )
    its	PRP$	40	nmod:poss
    2 1/2	CD	40	nummod
    -	:	40	punct
    hour	NN	31	nmod
    running	VBG	42	amod
    time	NN	40	dep
    .	.	24	punct
    <BLANKLINE>

    """
    _OUTPUT_FORMAT = ...
    parser_annotator = ...
    def make_tree(self, result):
        ...
    


def transform(sentence):
    ...

