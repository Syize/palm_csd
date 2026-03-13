"""Package with data file for default values, definitions and mappings for palm_csd."""

from os.path import abspath, dirname

RES_PATH = abspath(dirname(__file__))

CSV_LCZ_DEFINITIONS = f"{RES_PATH}/lcz_definitions.csv"
CSV_LCZ_MAPPINGS = f"{RES_PATH}/lcz_mappings.csv"
CSV_TREE_DEFAULTS = f"{RES_PATH}/tree_defaults.csv"
CSV_VALUE_DEFAULTS = f"{RES_PATH}/value_defaults.csv"


__all__ = ["CSV_LCZ_DEFINITIONS", "CSV_LCZ_MAPPINGS", "CSV_TREE_DEFAULTS", "CSV_VALUE_DEFAULTS"]
