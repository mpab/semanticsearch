"""
This type stub file was generated by pyright.
"""

import re
from nltk.tokenize import RegexpTokenizer
from nltk.corpus.util import LazyCorpusLoader
from nltk.corpus.reader import *

"""
NLTK corpus readers.  The modules in this package provide functions
that can be used to read corpus files in a variety of formats.  These
functions can be used to read both the corpus files that are
distributed in the NLTK corpus package, and corpus files that are part
of external corpora.

Available Corpora
=================

Please see http://www.nltk.org/nltk_data/ for a complete list.
Install corpora using nltk.download().

Corpus Reader Functions
=======================
Each corpus module defines one or more "corpus reader functions",
which can be used to read documents from that corpus.  These functions
take an argument, ``item``, which is used to indicate which document
should be read from the corpus:

- If ``item`` is one of the unique identifiers listed in the corpus
  module's ``items`` variable, then the corresponding document will
  be loaded from the NLTK corpus package.
- If ``item`` is a filename, then that file will be read.

Additionally, corpus reader functions can be given lists of item
names; in which case, they will return a concatenation of the
corresponding documents.

Corpus reader functions are named based on the type of information
they return.  Some common examples, and their return types, are:

- words(): list of str
- sents(): list of (list of str)
- paras(): list of (list of (list of str))
- tagged_words(): list of (str,str) tuple
- tagged_sents(): list of (list of (str,str))
- tagged_paras(): list of (list of (list of (str,str)))
- chunked_sents(): list of (Tree w/ (str,str) leaves)
- parsed_sents(): list of (Tree with str leaves)
- parsed_paras(): list of (list of (Tree with str leaves))
- xml(): A single xml ElementTree
- raw(): unprocessed corpus contents

For example, to read a list of the words in the Brown Corpus, use
``nltk.corpus.brown.words()``:

    >>> from nltk.corpus import brown
    >>> print(", ".join(brown.words()))
    The, Fulton, County, Grand, Jury, said, ...

"""
abc = ...
alpino = ...
brown = ...
cess_cat = ...
cess_esp = ...
cmudict = ...
comtrans = ...
comparative_sentences = ...
conll2000 = ...
conll2002 = ...
conll2007 = ...
crubadan = ...
dependency_treebank = ...
floresta = ...
framenet15 = ...
framenet = ...
gazetteers = ...
genesis = ...
gutenberg = ...
ieer = ...
inaugural = ...
indian = ...
jeita = ...
knbc = ...
lin_thesaurus = ...
mac_morpho = ...
machado = ...
masc_tagged = ...
movie_reviews = ...
multext_east = ...
names = ...
nps_chat = ...
opinion_lexicon = ...
ppattach = ...
product_reviews_1 = ...
product_reviews_2 = ...
pros_cons = ...
ptb = ...
qc = ...
reuters = ...
rte = ...
senseval = ...
sentence_polarity = ...
sentiwordnet = ...
shakespeare = ...
sinica_treebank = ...
state_union = ...
stopwords = ...
subjectivity = ...
swadesh = ...
swadesh110 = ...
swadesh207 = ...
switchboard = ...
timit = ...
timit_tagged = ...
toolbox = ...
treebank = ...
treebank_chunk = ...
treebank_raw = ...
twitter_samples = ...
udhr = ...
udhr2 = ...
universal_treebanks = ...
verbnet = ...
webtext = ...
wordnet = ...
wordnet_ic = ...
words = ...
propbank = ...
nombank = ...
propbank_ptb = ...
nombank_ptb = ...
semcor = ...
nonbreaking_prefixes = ...
perluniprops = ...
def demo():
    ...

if __name__ == "__main__":
    ...
