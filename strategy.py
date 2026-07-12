from enum import Enum

class MissingStrategy(str, Enum):
    DROP = "drop"
    MEAN = "mean"
    MEDIAN = "median"
    FFILL = "ffill"
    BFILL = "bfill"
    MODE = "mode"
    FFILL_TO_BFILL = "ffill_to_bfill"
    BFILL_TO_FFILL = "bfill_to_ffill"
    NONE = "none"
    CONSTANT = "constant"

class OutlierStrategy(str, Enum):
    IQR = "iqr"
    ZSCORE = "zscore"
    NONE = "none"