"""
This type stub file was generated by pyright.
"""

from nltk.tokenize import *
from nltk.corpus.reader.util import *
from nltk.corpus.reader.api import *

class DependencyCorpusReader(SyntaxCorpusReader):
    def __init__(self, root, fileids, encoding=..., word_tokenizer=..., sent_tokenizer=..., para_block_reader=...) -> None:
        ...
    
    def raw(self, fileids=...):
        """
        :return: the given file(s) as a single string.
        :rtype: str
        """
        ...
    
    def words(self, fileids=...):
        ...
    
    def tagged_words(self, fileids=...):
        ...
    
    def sents(self, fileids=...):
        ...
    
    def tagged_sents(self, fileids=...):
        ...
    
    def parsed_sents(self, fileids=...):
        ...
    


class DependencyCorpusView(StreamBackedCorpusView):
    _DOCSTART = ...
    def __init__(self, corpus_file, tagged, group_by_sent, dependencies, chunk_types=..., encoding=...) -> None:
        ...
    
    def read_block(self, stream):
        ...
    


