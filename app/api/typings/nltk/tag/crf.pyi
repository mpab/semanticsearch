"""
This type stub file was generated by pyright.
"""

from nltk.tag.api import TaggerI

"""
A module for POS tagging using CRFSuite
"""
class CRFTagger(TaggerI):
    """
    A module for POS tagging using CRFSuite https://pypi.python.org/pypi/python-crfsuite

    >>> from nltk.tag import CRFTagger
    >>> ct = CRFTagger()

    >>> train_data = [[('University','Noun'), ('is','Verb'), ('a','Det'), ('good','Adj'), ('place','Noun')],
    ... [('dog','Noun'),('eat','Verb'),('meat','Noun')]]

    >>> ct.train(train_data,'model.crf.tagger')
    >>> ct.tag_sents([['dog','is','good'], ['Cat','eat','meat']])
    [[('dog', 'Noun'), ('is', 'Verb'), ('good', 'Adj')], [('Cat', 'Noun'), ('eat', 'Verb'), ('meat', 'Noun')]]

    >>> gold_sentences = [[('dog','Noun'),('is','Verb'),('good','Adj')] , [('Cat','Noun'),('eat','Verb'), ('meat','Noun')]]
    >>> ct.evaluate(gold_sentences)
    1.0

    Setting learned model file
    >>> ct = CRFTagger()
    >>> ct.set_model_file('model.crf.tagger')
    >>> ct.evaluate(gold_sentences)
    1.0

    """
    def __init__(self, feature_func=..., verbose=..., training_opt=...) -> None:
        """
        Initialize the CRFSuite tagger
        :param feature_func: The function that extracts features for each token of a sentence. This function should take
        2 parameters: tokens and index which extract features at index position from tokens list. See the build in
        _get_features function for more detail.
        :param verbose: output the debugging messages during training.
        :type verbose: boolean
        :param training_opt: python-crfsuite training options
        :type training_opt : dictionary

        Set of possible training options (using LBFGS training algorithm).
         'feature.minfreq' : The minimum frequency of features.
         'feature.possible_states' : Force to generate possible state features.
         'feature.possible_transitions' : Force to generate possible transition features.
         'c1' : Coefficient for L1 regularization.
         'c2' : Coefficient for L2 regularization.
         'max_iterations' : The maximum number of iterations for L-BFGS optimization.
         'num_memories' : The number of limited memories for approximating the inverse hessian matrix.
         'epsilon' : Epsilon for testing the convergence of the objective.
         'period' : The duration of iterations to test the stopping criterion.
         'delta' : The threshold for the stopping criterion; an L-BFGS iteration stops when the
                    improvement of the log likelihood over the last ${period} iterations is no greater than this threshold.
         'linesearch' : The line search algorithm used in L-BFGS updates:
                           { 'MoreThuente': More and Thuente's method,
                              'Backtracking': Backtracking method with regular Wolfe condition,
                              'StrongBacktracking': Backtracking method with strong Wolfe condition
                           }
         'max_linesearch' :  The maximum number of trials for the line search algorithm.

        """
        ...
    
    def set_model_file(self, model_file):
        ...
    
    def tag_sents(self, sents):
        """
        Tag a list of sentences. NB before using this function, user should specify the mode_file either by
                       - Train a new model using ``train'' function
                       - Use the pre-trained model which is set via ``set_model_file'' function
        :params sentences : list of sentences needed to tag.
        :type sentences : list(list(str))
        :return : list of tagged sentences.
        :rtype : list (list (tuple(str,str)))
        """
        ...
    
    def train(self, train_data, model_file):
        """
        Train the CRF tagger using CRFSuite
        :params train_data : is the list of annotated sentences.
        :type train_data : list (list(tuple(str,str)))
        :params model_file : the model will be saved to this file.

        """
        ...
    
    def tag(self, tokens):
        """
        Tag a sentence using Python CRFSuite Tagger. NB before using this function, user should specify the mode_file either by
                       - Train a new model using ``train'' function
                       - Use the pre-trained model which is set via ``set_model_file'' function
        :params tokens : list of tokens needed to tag.
        :type tokens : list(str)
        :return : list of tagged tokens.
        :rtype : list (tuple(str,str))
        """
        ...
    


