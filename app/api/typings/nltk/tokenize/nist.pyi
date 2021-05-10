"""
This type stub file was generated by pyright.
"""

from nltk.tokenize.api import TokenizerI

"""
This is a NLTK port of the tokenizer used in the NIST BLEU evaluation script,
https://github.com/moses-smt/mosesdecoder/blob/master/scripts/generic/mteval-v14.pl#L926
which was also ported into Python in
https://github.com/lium-lst/nmtpy/blob/master/nmtpy/metrics/mtevalbleu.py#L162
"""
class NISTTokenizer(TokenizerI):
    """
    This NIST tokenizer is sentence-based instead of the original
    paragraph-based tokenization from mteval-14.pl; The sentence-based
    tokenization is consistent with the other tokenizers available in NLTK.

    >>> from nltk.tokenize.nist import NISTTokenizer
    >>> nist = NISTTokenizer()
    >>> s = "Good muffins cost $3.88 in New York."
    >>> expected_lower = [u'good', u'muffins', u'cost', u'$', u'3.88', u'in', u'new', u'york', u'.']
    >>> expected_cased = [u'Good', u'muffins', u'cost', u'$', u'3.88', u'in', u'New', u'York', u'.']
    >>> nist.tokenize(s, lowercase=False) == expected_cased
    True
    >>> nist.tokenize(s, lowercase=True) == expected_lower  # Lowercased.
    True

    The international_tokenize() is the preferred function when tokenizing
    non-european text, e.g.

    >>> from nltk.tokenize.nist import NISTTokenizer
    >>> nist = NISTTokenizer()

    # Input strings.
    >>> albb = u'Alibaba Group Holding Limited (Chinese: 阿里巴巴集团控股 有限公司) us a Chinese e-commerce company...'
    >>> amz = u'Amazon.com, Inc. (/ˈæməzɒn/) is an American electronic commerce...'
    >>> rkt = u'Rakuten, Inc. (楽天株式会社 Rakuten Kabushiki-gaisha) is a Japanese electronic commerce and Internet company based in Tokyo.'

    # Expected tokens.
    >>> expected_albb = [u'Alibaba', u'Group', u'Holding', u'Limited', u'(', u'Chinese', u':', u'\u963f\u91cc\u5df4\u5df4\u96c6\u56e2\u63a7\u80a1', u'\u6709\u9650\u516c\u53f8', u')']
    >>> expected_amz = [u'Amazon', u'.', u'com', u',', u'Inc', u'.', u'(', u'/', u'\u02c8\xe6', u'm']
    >>> expected_rkt = [u'Rakuten', u',', u'Inc', u'.', u'(', u'\u697d\u5929\u682a\u5f0f\u4f1a\u793e', u'Rakuten', u'Kabushiki', u'-', u'gaisha']

    >>> nist.international_tokenize(albb)[:10] == expected_albb
    True
    >>> nist.international_tokenize(amz)[:10] == expected_amz
    True
    >>> nist.international_tokenize(rkt)[:10] == expected_rkt
    True

    # Doctest for patching issue #1926
    >>> sent = u'this is a foo\u2604sentence.'
    >>> expected_sent = [u'this', u'is', u'a', u'foo', u'\u2604', u'sentence', u'.']
    >>> nist.international_tokenize(sent) == expected_sent
    True
    """
    STRIP_SKIP = ...
    STRIP_EOL_HYPHEN = ...
    PUNCT = ...
    PERIOD_COMMA_PRECEED = ...
    PERIOD_COMMA_FOLLOW = ...
    DASH_PRECEED_DIGIT = ...
    LANG_DEPENDENT_REGEXES = ...
    pup_number = ...
    pup_punct = ...
    pup_symbol = ...
    number_regex = ...
    punct_regex = ...
    symbol_regex = ...
    NONASCII = ...
    PUNCT_1 = ...
    PUNCT_2 = ...
    SYMBOLS = ...
    INTERNATIONAL_REGEXES = ...
    def lang_independent_sub(self, text):
        """Performs the language independent string substituitions. """
        ...
    
    def tokenize(self, text, lowercase=..., western_lang=..., return_str=...):
        ...
    
    def international_tokenize(self, text, lowercase=..., split_non_ascii=..., return_str=...):
        ...
    


