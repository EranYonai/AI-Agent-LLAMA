from enum import Enum
from logging import getLogger
from pathlib import Path, PureWindowsPath

from dataclasses import dataclass
from llama_index.tools import FunctionTool
import pandas as pd

log = getLogger(__name__)


@dataclass
class FilePaths:
    note: PureWindowsPath = PureWindowsPath("data", "notes.txt")


def save_note(note: str, file_path: str = str(FilePaths.note)) -> bool:
    try:
        file_context = Path(file_path)
        if not file_context.exists()
            with file_context.open("w") as f:
                f.writelines([])
        with file_context.open("a") as f:
            f.writelines([note+"\n"])
    except Exception:
        log.exception(f"Failed writing to file {file_path}.")
    return True

@dataclass
class model_tools(Enum):
    note_engine = FunctionTool.from_defaults(
        fn=save_note,
        name="save_note",
        description="this function can save a text based note to a file for the user",
    )
