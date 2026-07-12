from pydantic import BaseModel, ConfigDict, model_validator, Field
from typing import Literal, Optional, Any
from strategy import MissingStrategy, OutlierStrategy

DtypeLiteral = Literal["int", "float", "str", "bool", "datetime"]

class ColumnConfig(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True, use_enum_values=False)

    name: str
    dtype: Optional[DtypeLiteral] = None

    missing_strategy: MissingStrategy = MissingStrategy.MEAN
    fill_value: Any = None

    outlier_strategy: OutlierStrategy = OutlierStrategy.NONE

    strip_string: bool = True
    lower_case: bool = False

    allowed_values: Optional[list[Any]] = None

    @model_validator(mode="after")
    def validate_fill_value(self) -> "ColumnConfig":
        if self.missing_strategy == MissingStrategy.CONSTANT and self.fill_value is None:
            raise ValueError(
                f"Column '{self.name}': needs fill_value for CONSTANT type missing strategy"
            )
        return self

class CleaningConfig(BaseModel):
    drop_duplicated: bool = True
    duplicate_subset: Optional[list[str]] = None
    drop_col_threshold: float = Field(default=0.5, ge=0.0, le=1.0)

    column_configs: list[ColumnConfig] = Field(default_factory=list)

    def get_column_config(self, column: str) -> Optional[ColumnConfig]:
        return next((r for r in self.column_configs if r.name == column), None)
    