"""CD-GPT: A Biological Foundation Model"""

from .model import (
    CDGPT,
    CDGPTResiduePairPrediction,
    CDGPTTokenPrediction,
    CDGPTSequencePrediction,
)

__version__ = "0.1.0"
__all__ = [
    "CDGPT",
    "CDGPTResiduePairPrediction",
    "CDGPTTokenPrediction",
    "CDGPTSequencePrediction",
]
