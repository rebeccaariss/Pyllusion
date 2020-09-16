"""
Pyllusion submodule.
"""

from .delboeuf import delboeuf_parameters, delboeuf_image
from .ebbinghaus import ebbinghaus_parameters, ebbinghaus_image
from .ponzo import ponzo_parameters, ponzo_image
from .rodframe import rodframe_parameters, rodframe_image
from .mullerlyer import mullerlyer_parameters, mullerlyer_image
from .verticalhorizontal import verticalhorizontal_parameters, verticalhorizontal_image
from .zollner import zollner_parameters, zollner_image
from .poggendorff import poggendorff_parameters, poggendorff_image
from .contrast import contrast_parameters, contrast_image
from .white import white_parameters, white_image
from .autostereogram import autostereogram
from .pareidolia import pareidolia

__all__ = [
    "delboeuf_parameters",
    "delboeuf_image",
    "ebbinghaus_parameters",
    "ebbinghaus_image",
    "ponzo_parameters",
    "ponzo_image",
    "rodframe_parameters",
    "rodframe_image",
    "mullerlyer_parameters",
    "mullerlyer_image",
    "verticalhorizontal_parameters",
    "verticalhorizontal_image",
    "zollner_parameters",
    "zollner_image",
    "poggendorff_parameters",
    "poggendorff_image",
    "contrast_parameters",
    "contrast_image",
    "white_parameters",
    "white_image",
    "autostereogram",
    "pareidolia",
]
