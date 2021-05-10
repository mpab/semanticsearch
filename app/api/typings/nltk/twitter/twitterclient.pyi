"""
This type stub file was generated by pyright.
"""

from twython import Twython, TwythonStreamer
from nltk.twitter.api import TweetHandlerI

"""
NLTK Twitter client

This module offers methods for collecting and processing Tweets. Most of the
functionality depends on access to the Twitter APIs, and this is handled via
the third party Twython library.

If one of the methods below returns an integer, it is probably a `Twitter
error code <https://dev.twitter.com/overview/api/response-codes>`_. For
example, the response of '420' means that you have reached the limit of the
requests you can currently make to the Twitter API. Currently, `rate limits
for the search API <https://dev.twitter.com/rest/public/rate-limiting>`_ are
divided into 15 minute windows.
"""
class Streamer(TwythonStreamer):
    """
    Retrieve data from the Twitter Streaming API.

    The streaming API requires
    `OAuth 1.0 <http://en.wikipedia.org/wiki/OAuth>`_ authentication.
    """
    def __init__(self, app_key, app_secret, oauth_token, oauth_token_secret) -> None:
        ...
    
    def register(self, handler):
        """
        Register a method for handling Tweets.

        :param TweetHandlerI handler: method for viewing
        """
        ...
    
    def on_success(self, data):
        """
        :param data: response from Twitter API
        """
        ...
    
    def on_error(self, status_code, data):
        """
        :param status_code: The status code returned by the Twitter API
        :param data: The response from Twitter API

        """
        ...
    
    def sample(self):
        """
        Wrapper for 'statuses / sample' API call
        """
        ...
    
    def filter(self, track=..., follow=..., lang=...):
        """
        Wrapper for 'statuses / filter' API call
        """
        ...
    


class Query(Twython):
    """
    Retrieve data from the Twitter REST API.
    """
    def __init__(self, app_key, app_secret, oauth_token, oauth_token_secret) -> None:
        ...
    
    def register(self, handler):
        """
        Register a method for handling Tweets.

        :param TweetHandlerI handler: method for viewing or writing Tweets to a file.
        """
        ...
    
    def expand_tweetids(self, ids_f, verbose=...):
        """
        Given a file object containing a list of Tweet IDs, fetch the
        corresponding full Tweets from the Twitter API.

        The API call `statuses/lookup` will fail to retrieve a Tweet if the
        user has deleted it.

        This call to the Twitter API is rate-limited. See
        <https://dev.twitter.com/rest/reference/get/statuses/lookup> for details.

        :param ids_f: input file object consisting of Tweet IDs, one to a line
        :return: iterable of Tweet objects in JSON format
        """
        ...
    
    def search_tweets(self, keywords, limit=..., lang=..., max_id=..., retries_after_twython_exception=...):
        """
        Call the REST API ``'search/tweets'`` endpoint with some plausible
        defaults. See `the Twitter search documentation
        <https://dev.twitter.com/rest/public/search>`_ for more information
        about admissible search parameters.

        :param str keywords: A list of query terms to search for, written as\
        a comma-separated string
        :param int limit: Number of Tweets to process
        :param str lang: language
        :param int max_id: id of the last tweet fetched
        :param int retries_after_twython_exception: number of retries when\
        searching Tweets before raising an exception
        :rtype: python generator
        """
        ...
    
    def user_info_from_id(self, userids):
        """
        Convert a list of userIDs into a variety of information about the users.

        See <https://dev.twitter.com/rest/reference/get/users/show>.

        :param list userids: A list of integer strings corresponding to Twitter userIDs
        :rtype: list(json)
        """
        ...
    
    def user_tweets(self, screen_name, limit, include_rts=...):
        """
        Return a collection of the most recent Tweets posted by the user

        :param str user: The user's screen name; the initial '@' symbol\
        should be omitted
        :param int limit: The number of Tweets to recover; 200 is the maximum allowed
        :param str include_rts: Whether to include statuses which have been\
        retweeted by the user; possible values are 'true' and 'false'
        """
        ...
    


class Twitter(object):
    """
    Wrapper class with restricted functionality and fewer options.
    """
    def __init__(self) -> None:
        ...
    
    def tweets(self, keywords=..., follow=..., to_screen=..., stream=..., limit=..., date_limit=..., lang=..., repeat=..., gzip_compress=...):
        """
        Process some Tweets in a simple manner.

        :param str keywords: Keywords to use for searching or filtering
        :param list follow: UserIDs to use for filtering Tweets from the public stream
        :param bool to_screen: If `True`, display the tweet texts on the screen,\
        otherwise print to a file

        :param bool stream: If `True`, use the live public stream,\
        otherwise search past public Tweets

        :param int limit: The number of data items to process in the current\
        round of processing.

        :param tuple date_limit: The date at which to stop collecting\
        new data. This should be entered as a tuple which can serve as the\
        argument to `datetime.datetime`.\
        E.g. `date_limit=(2015, 4, 1, 12, 40)` for 12:30 pm on April 1 2015.
        Note that, in the case of streaming, this is the maximum date, i.e.\
        a date in the future; if not, it is the minimum date, i.e. a date\
        in the past

        :param str lang: language

        :param bool repeat: A flag to determine whether multiple files should\
        be written. If `True`, the length of each file will be set by the\
        value of `limit`. Use only if `to_screen` is `False`. See also
        :py:func:`handle`.

        :param gzip_compress: if `True`, output files are compressed with gzip.
        """
        ...
    


class TweetViewer(TweetHandlerI):
    """
    Handle data by sending it to the terminal.
    """
    def handle(self, data):
        """
        Direct data to `sys.stdout`

        :return: return ``False`` if processing should cease, otherwise return ``True``.
        :rtype: bool
        :param data: Tweet object returned by Twitter API
        """
        ...
    
    def on_finish(self):
        ...
    


class TweetWriter(TweetHandlerI):
    """
    Handle data by writing it to a file.
    """
    def __init__(self, limit=..., upper_date_limit=..., lower_date_limit=..., fprefix=..., subdir=..., repeat=..., gzip_compress=...) -> None:
        """
        The difference between the upper and lower date limits depends on
        whether Tweets are coming in an ascending date order (i.e. when
        streaming) or descending date order (i.e. when searching past Tweets).

        :param int limit: number of data items to process in the current\
        round of processing.

        :param tuple upper_date_limit: The date at which to stop collecting new\
        data. This should be entered as a tuple which can serve as the\
        argument to `datetime.datetime`. E.g. `upper_date_limit=(2015, 4, 1, 12,\
        40)` for 12:30 pm on April 1 2015.

        :param tuple lower_date_limit: The date at which to stop collecting new\
        data. See `upper_data_limit` for formatting.

        :param str fprefix: The prefix to use in creating file names for Tweet\
        collections.

        :param str subdir: The name of the directory where Tweet collection\
        files should be stored.

        :param bool repeat: flag to determine whether multiple files should be\
        written. If `True`, the length of each file will be set by the value\
        of `limit`. See also :py:func:`handle`.

        :param gzip_compress: if `True`, ouput files are compressed with gzip.
        """
        ...
    
    def timestamped_file(self):
        """
        :return: timestamped file name
        :rtype: str
        """
        ...
    
    def handle(self, data):
        """
        Write Twitter data as line-delimited JSON into one or more files.

        :return: return `False` if processing should cease, otherwise return `True`.
        :param data: tweet object returned by Twitter API
        """
        ...
    
    def on_finish(self):
        ...
    
    def do_continue(self):
        ...
    


