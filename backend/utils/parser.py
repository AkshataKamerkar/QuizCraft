from llama_parse import LlamaParse
import os
from dotenv import load_dotenv

load_dotenv()
LLAMA_API_KEY = os.getenv("LLAMA_CLOUD_API_KEY")

def parse_document(file_path):
    parser = LlamaParse(api_key=LLAMA_API_KEY)
    parsed = parser.load_data(file_path)
    return parsed[0].text if parsed else ""

# def parse_document(path: str = "utils/document.txt") -> str:
#     try:
#         with open(path, "r", encoding="utf-8") as file:
#             return file.read()
#     except Exception as e:
#         raise RuntimeError(f"Failed to read document: {e}")