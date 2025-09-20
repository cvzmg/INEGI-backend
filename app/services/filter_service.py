from __future__ import annotations
import os
from dataclasses import dataclass
from typing import Optional, Dict, Any, List, Tuple
import pandas as pd
from collections import Counter


TOTAL_PATTERNS = ("Total de la entidad", "Ciudad de México")

def _standardize_alcaldia_column(df: pd.DataFrame) -> pd.DataFrame:
    rename_map = {
      "ALCALDIA": "alcaldia",
      "Alcaldia": "alcaldia",
      "Alcaldía": "alcaldia",
      "alcaldia": "alcaldia",
      "NOM_MUN": "alcaldia",
      "Demarcación territorial": "alcaldia",
      "Alcaldias": "alcaldia",
      "alcaldias": "alcaldia",
      "alcaldia_": "alcaldia",
    }
    df = df.rename(columns=rename_map)
    if "alcaldia" not in df.columns:
      # Fall back to first column if we can’t find a canonical one
      df = df.rename(columns={df.columns[0]: "alcaldia"})
    return df
