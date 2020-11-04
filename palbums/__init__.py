from pathlib import Path

import matplotlib as mpl


__all__ = []

here = Path(__file__).parent

# register the included stylesheet in the mpl style library
_stylesheets = mpl.style.core.read_style_directory(here / 'data')
mpl.style.core.update_nested_dict(mpl.style.library, _stylesheets)

styles = tuple(_stylesheets.keys())
