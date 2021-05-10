"""
This type stub file was generated by pyright.
"""

from nltk.corpus.reader.xmldocs import XMLCorpusReader

"""
An NLTK interface to the VerbNet verb lexicon

For details about VerbNet see:
https://verbs.colorado.edu/~mpalmer/projects/verbnet.html
"""
class VerbnetCorpusReader(XMLCorpusReader):
    """
    An NLTK interface to the VerbNet verb lexicon.

    From the VerbNet site: "VerbNet (VN) (Kipper-Schuler 2006) is the largest
    on-line verb lexicon currently available for English. It is a hierarchical
    domain-independent, broad-coverage verb lexicon with mappings to other
    lexical resources such as WordNet (Miller, 1990; Fellbaum, 1998), XTAG
    (XTAG Research Group, 2001), and FrameNet (Baker et al., 1998)."

    For details about VerbNet see:
    https://verbs.colorado.edu/~mpalmer/projects/verbnet.html
    """
    def __init__(self, root, fileids, wrap_etree=...) -> None:
        ...
    
    _LONGID_RE = ...
    _SHORTID_RE = ...
    _INDEX_RE = ...
    def lemmas(self, vnclass=...):
        """
        Return a list of all verb lemmas that appear in any class, or
        in the ``classid`` if specified.
        """
        ...
    
    def wordnetids(self, vnclass=...):
        """
        Return a list of all wordnet identifiers that appear in any
        class, or in ``classid`` if specified.
        """
        ...
    
    def classids(self, lemma=..., wordnetid=..., fileid=..., classid=...):
        """
        Return a list of the VerbNet class identifiers.  If a file
        identifier is specified, then return only the VerbNet class
        identifiers for classes (and subclasses) defined by that file.
        If a lemma is specified, then return only VerbNet class
        identifiers for classes that contain that lemma as a member.
        If a wordnetid is specified, then return only identifiers for
        classes that contain that wordnetid as a member.  If a classid
        is specified, then return only identifiers for subclasses of
        the specified VerbNet class.
        If nothing is specified, return all classids within VerbNet
        """
        ...
    
    def vnclass(self, fileid_or_classid):
        """Returns VerbNet class ElementTree

        Return an ElementTree containing the xml for the specified
        VerbNet class.

        :param fileid_or_classid: An identifier specifying which class
            should be returned.  Can be a file identifier (such as
            ``'put-9.1.xml'``), or a VerbNet class identifier (such as
            ``'put-9.1'``) or a short VerbNet class identifier (such as
            ``'9.1'``).
        """
        ...
    
    def fileids(self, vnclass_ids=...):
        """
        Return a list of fileids that make up this corpus.  If
        ``vnclass_ids`` is specified, then return the fileids that make
        up the specified VerbNet class(es).
        """
        ...
    
    def frames(self, vnclass):
        """Given a VerbNet class, this method returns VerbNet frames

        The members returned are:
        1) Example
        2) Description
        3) Syntax
        4) Semantics

        :param vnclass: A VerbNet class identifier; or an ElementTree
            containing the xml contents of a VerbNet class.
        :return: frames - a list of frame dictionaries
        """
        ...
    
    def subclasses(self, vnclass):
        """Returns subclass ids, if any exist

        Given a VerbNet class, this method returns subclass ids (if they exist)
        in a list of strings.

        :param vnclass: A VerbNet class identifier; or an ElementTree
            containing the xml contents of a VerbNet class.
        :return: list of subclasses
        """
        ...
    
    def themroles(self, vnclass):
        """Returns thematic roles participating in a VerbNet class

        Members returned as part of roles are-
        1) Type
        2) Modifiers

        :param vnclass: A VerbNet class identifier; or an ElementTree
            containing the xml contents of a VerbNet class.
        :return: themroles: A list of thematic roles in the VerbNet class
        """
        ...
    
    def longid(self, shortid):
        """Returns longid of a VerbNet class

        Given a short VerbNet class identifier (eg '37.10'), map it
        to a long id (eg 'confess-37.10').  If ``shortid`` is already a
        long id, then return it as-is"""
        ...
    
    def shortid(self, longid):
        """Returns shortid of a VerbNet class

        Given a long VerbNet class identifier (eg 'confess-37.10'),
        map it to a short id (eg '37.10').  If ``longid`` is already a
        short id, then return it as-is."""
        ...
    
    def pprint(self, vnclass):
        """Returns pretty printed version of a VerbNet class

        Return a string containing a pretty-printed representation of
        the given VerbNet class.

        :param vnclass: A VerbNet class identifier; or an ElementTree
        containing the xml contents of a VerbNet class.
        """
        ...
    
    def pprint_subclasses(self, vnclass, indent=...):
        """Returns pretty printed version of subclasses of VerbNet class

        Return a string containing a pretty-printed representation of
        the given VerbNet class's subclasses.

        :param vnclass: A VerbNet class identifier; or an ElementTree
            containing the xml contents of a VerbNet class.
        """
        ...
    
    def pprint_members(self, vnclass, indent=...):
        """Returns pretty printed version of members in a VerbNet class

        Return a string containing a pretty-printed representation of
        the given VerbNet class's member verbs.

        :param vnclass: A VerbNet class identifier; or an ElementTree
            containing the xml contents of a VerbNet class.
        """
        ...
    
    def pprint_themroles(self, vnclass, indent=...):
        """Returns pretty printed version of thematic roles in a VerbNet class

        Return a string containing a pretty-printed representation of
        the given VerbNet class's thematic roles.

        :param vnclass: A VerbNet class identifier; or an ElementTree
            containing the xml contents of a VerbNet class.
        """
        ...
    
    def pprint_frames(self, vnclass, indent=...):
        """Returns pretty version of all frames in a VerbNet class

        Return a string containing a pretty-printed representation of
        the list of frames within the VerbNet class.

        :param vnclass: A VerbNet class identifier; or an ElementTree
            containing the xml contents of a VerbNet class.
        """
        ...
    


