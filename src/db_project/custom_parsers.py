import os
import re
import sys
from inspect import getblock, getmodule, getsourcefile, linecache

from IPython.display import Markdown, display

from .basics import res_to_df as rtd
from .basics import run_query as rq


def collect_relevant_solutions(module, query_id=1):
    query_identifier = "query_{:02d}".format(query_id)

    # Dynamic manipulation of loaded module.
    setattr(module, "run_query", rq)
    setattr(module, "res_to_df", rtd)

    relevant_function_names = [f for f in dir(module) if f.startswith(query_identifier)]
    relevant_functions = [
        getattr(module, method_name) for method_name in relevant_function_names
    ]

    relevant_sources = [_get_source(f, module=module) for f in relevant_functions]

    return list(zip(relevant_function_names, relevant_functions, relevant_sources))


def parse_markdown(f, section_number=1):
    """
    Parse markdown file for display in jupyter.

    This is useful because it allows us to write all information only once.

    Args:
        f ([type]): Filename
        section_number (int, optional): Section of the file you want to display. Defaults to 1.

    Raises:
        ValueError: [description]

    Returns:
        [type]: [description]
    """
    if not isinstance(f, str):
        f = str(f)

    if isinstance(section_number, int):
        # Get lines
        linecache.checkcache(f)
        lines = linecache.getlines(f)

        # Simple parse (Every markdown section is a section)
        sections = {}
        counter = 0

        for lnum, line in enumerate(lines):
            if line.startswith("#"):
                sections[counter] = lnum
                counter += 1
        sections[counter] = len(lines)  # Also collect final line.

        # Extract the desired section
        section = "".join(
            lines[sections[section_number - 1] : sections[section_number]]
        )

    elif isinstance(section_number, list):
        section = ""
        for sn in section_number:
            s = parse_markdown(f, section_number=sn)
            section += s
    else:
        msg = """
        Section number has to be int or list.
        Type sectionnumber passed was:     {}
        """.format(
            type(section_number)
        )
        raise ValueError(msg)

    return section


def _get_source(function, module=None):
    """
    Custom source-code parser because built-in of Python fails sometimes.

    This function parses student-solution sourcecode.
    """

    name = function.__name__
    file = getsourcefile(function)

    # Get lines
    linecache.checkcache(file)
    if module is None:
        module = getmodule(function, file)
    lines = linecache.getlines(file, module.__dict__)

    # Parse lines
    pat = re.compile("(def {}\()".format(name))  # Begin of function pattern.

    for lnum, line in enumerate(lines):
        if pat.match(line):
            break

    src = getblock(lines[lnum:])
    src = "".join(src)

    return src


def toon_uitleg(markdown_filename, sectie=None):
    """
    Show contents of a markdown file in a notebook.

    Centralizing all text-content in a few markdown files makes it a lot
    easier to keep everything in sync across multiple notebooks.
    """
    return display(Markdown(parse_markdown(markdown_filename, section_number=sectie)))
