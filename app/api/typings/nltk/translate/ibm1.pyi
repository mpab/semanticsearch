"""
This type stub file was generated by pyright.
"""

from nltk.translate import IBMModel

"""
Lexical translation model that ignores word order.

In IBM Model 1, word order is ignored for simplicity. As long as the
word alignments are equivalent, it doesn't matter where the word occurs
in the source or target sentence. Thus, the following three alignments
are equally likely.

Source: je mange du jambon
Target: i eat some ham
Alignment: (0,0) (1,1) (2,2) (3,3)

Source: je mange du jambon
Target: some ham eat i
Alignment: (0,2) (1,3) (2,1) (3,1)

Source: du jambon je mange
Target: eat i some ham
Alignment: (0,3) (1,2) (2,0) (3,1)

Note that an alignment is represented here as
(word_index_in_target, word_index_in_source).

The EM algorithm used in Model 1 is:
E step - In the training data, count how many times a source language
         word is translated into a target language word, weighted by
         the prior probability of the translation.

M step - Estimate the new probability of translation based on the
         counts from the Expectation step.


Notations:
i: Position in the source sentence
    Valid values are 0 (for NULL), 1, 2, ..., length of source sentence
j: Position in the target sentence
    Valid values are 1, 2, ..., length of target sentence
s: A word in the source language
t: A word in the target language


References:
Philipp Koehn. 2010. Statistical Machine Translation.
Cambridge University Press, New York.

Peter E Brown, Stephen A. Della Pietra, Vincent J. Della Pietra, and
Robert L. Mercer. 1993. The Mathematics of Statistical Machine
Translation: Parameter Estimation. Computational Linguistics, 19 (2),
263-311.
"""
class IBMModel1(IBMModel):
    """
    Lexical translation model that ignores word order

    >>> bitext = []
    >>> bitext.append(AlignedSent(['klein', 'ist', 'das', 'haus'], ['the', 'house', 'is', 'small']))
    >>> bitext.append(AlignedSent(['das', 'haus', 'ist', 'ja', 'groß'], ['the', 'house', 'is', 'big']))
    >>> bitext.append(AlignedSent(['das', 'buch', 'ist', 'ja', 'klein'], ['the', 'book', 'is', 'small']))
    >>> bitext.append(AlignedSent(['das', 'haus'], ['the', 'house']))
    >>> bitext.append(AlignedSent(['das', 'buch'], ['the', 'book']))
    >>> bitext.append(AlignedSent(['ein', 'buch'], ['a', 'book']))

    >>> ibm1 = IBMModel1(bitext, 5)

    >>> print(ibm1.translation_table['buch']['book'])
    0.889...
    >>> print(ibm1.translation_table['das']['book'])
    0.061...
    >>> print(ibm1.translation_table['buch'][None])
    0.113...
    >>> print(ibm1.translation_table['ja'][None])
    0.072...

    >>> test_sentence = bitext[2]
    >>> test_sentence.words
    ['das', 'buch', 'ist', 'ja', 'klein']
    >>> test_sentence.mots
    ['the', 'book', 'is', 'small']
    >>> test_sentence.alignment
    Alignment([(0, 0), (1, 1), (2, 2), (3, 2), (4, 3)])

    """
    def __init__(self, sentence_aligned_corpus, iterations, probability_tables=...) -> None:
        """
        Train on ``sentence_aligned_corpus`` and create a lexical
        translation model.

        Translation direction is from ``AlignedSent.mots`` to
        ``AlignedSent.words``.

        :param sentence_aligned_corpus: Sentence-aligned parallel corpus
        :type sentence_aligned_corpus: list(AlignedSent)

        :param iterations: Number of iterations to run training algorithm
        :type iterations: int

        :param probability_tables: Optional. Use this to pass in custom
            probability values. If not specified, probabilities will be
            set to a uniform distribution, or some other sensible value.
            If specified, the following entry must be present:
            ``translation_table``.
            See ``IBMModel`` for the type and purpose of this table.
        :type probability_tables: dict[str]: object
        """
        ...
    
    def set_uniform_probabilities(self, sentence_aligned_corpus):
        ...
    
    def train(self, parallel_corpus):
        ...
    
    def prob_all_alignments(self, src_sentence, trg_sentence):
        """
        Computes the probability of all possible word alignments,
        expressed as a marginal distribution over target words t

        Each entry in the return value represents the contribution to
        the total alignment probability by the target word t.

        To obtain probability(alignment | src_sentence, trg_sentence),
        simply sum the entries in the return value.

        :return: Probability of t for all s in ``src_sentence``
        :rtype: dict(str): float
        """
        ...
    
    def prob_alignment_point(self, s, t):
        """
        Probability that word ``t`` in the target sentence is aligned to
        word ``s`` in the source sentence
        """
        ...
    
    def prob_t_a_given_s(self, alignment_info):
        """
        Probability of target sentence and an alignment given the
        source sentence
        """
        ...
    
    def align_all(self, parallel_corpus):
        ...
    
    def align(self, sentence_pair):
        """
        Determines the best word alignment for one sentence pair from
        the corpus that the model was trained on.

        The best alignment will be set in ``sentence_pair`` when the
        method returns. In contrast with the internal implementation of
        IBM models, the word indices in the ``Alignment`` are zero-
        indexed, not one-indexed.

        :param sentence_pair: A sentence in the source language and its
            counterpart sentence in the target language
        :type sentence_pair: AlignedSent
        """
        ...
    


