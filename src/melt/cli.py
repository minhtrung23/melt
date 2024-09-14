"cli"
import spacy

try:
    spacy.load("en_core_web_sm")
except OSError:
    print(
        "Downloading the spacy en_core_web_sm model\n"
        "(don't worry, this will only happen once)"
    )
    from spacy.cli import download

    download("en_core_web_sm")
from transformers import HfArgumentParser
from dotenv import load_dotenv
from script_arguments import ScriptArguments
from generation import generation

# from .to_sheet import to_sheet
# from .to_sheet_std import to_sheet_std

def main():
    "Cli"
    load_dotenv()
    parser = HfArgumentParser(ScriptArguments)
    args = parser.parse_args_into_dataclasses()[0]
    generation(args)
