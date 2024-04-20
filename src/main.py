import os
from dataclasses import dataclass
from logging import getLogger
from pathlib import Path, PureWindowsPath

import pandas as pd
from dotenv import load_dotenv
from llama_index.llms import openai
from llama_index.query_engine import PandasQueryEngine
from llama_index.tools import FunctionTool, QueryEngineTool, ToolMetadata
from model_interface import model_tools

log = getLogger(__name__)

if __name__ == "__main__":
    note_engine = FunctionTool.from_defaults(
        fn=save_note,
        name="save_note",
        description="this function can save a text based note to a file for the user",
    )
    pass
