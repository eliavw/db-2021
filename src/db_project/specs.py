"""This file contains functions to automatically

1. Generate query names
2. Generate query parameters
3. Extract specific queries from a submitted python file

"""


def gen_all_q_names(nb_queries=10):
    """
    Generate list of query names

    Parameters
    ----------
    nb_queries: int
                Number of queries

    Returns
    -------

    """

    return [gen_q_name(i) for i in range(nb_queries)]


def gen_q_name(q_idx):
    """
    Generate single query name
    Parameters
    ----------
    q_idx:  int
            Index of this query name.

    Returns
    -------

    """

    result = "query_{:02d}".format(q_idx + 1)  # One-based indexing
    return result


def gen_all_q_method(module, all_q_names=None):
    """
    Extract the desirec methods from the given module.

    The `desired methods` are specified by the query names,
    as provided by the parameter `all_q_names`.

    Parameters
    ----------
    module:         module
    all_q_names:    list
                    List of desired methods to be extracted from the module.

    Returns
    -------

    """
    if all_q_names is None:
        all_q_names = gen_all_q_names()

    all_q_method = {}
    for q_name in all_q_names:
        try:
            msg = """
            Loading method: {} from module {}
            """.format(
                q_name, module.__name__
            )
            print(msg)

            all_q_method[q_name] = getattr(module, q_name)

        except BaseException as error:
            method_name = gen_all_q_method.__name__

            msg = """
            An exception occurred in method {}:
                {}

            """.format(
                method_name, error
            )
            print(msg)

    return all_q_method
