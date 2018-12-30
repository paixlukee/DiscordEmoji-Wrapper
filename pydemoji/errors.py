class InvalidOption(Exception):
    """
    Exception occurs when the option or argument isn't valid.
    """
    pass

class InvalidQuery(Exception):
    """
    Exception occurs when the query given, isn't listed on the site.
    """
    pass
