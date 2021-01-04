from collections import namedtuple
from typing import Any

Line = namedtuple('Line', ['begin', 'hline', 'sep', 'end'])

DataRow = namedtuple('DataRow', ['begin', 'sep', 'end'])

TableFormat = namedtuple('TableFormat', ['lineabove', 'linebelowheader', 'linebetweenrows', 'linebelow', 'headerrow', 'datarow', 'padding', 'with_header_hide'])
tabulate_formats: Any

def simple_separated_format(separator: Any): ...
def tabulate(tabular_data: Any, headers: Any = ..., tablefmt: str = ..., floatfmt: str = ..., numalign: str = ..., stralign: str = ..., missingval: str = ...): ...
