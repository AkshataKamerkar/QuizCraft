from llama_parse import LlamaParse

def parse_document(file_path):
    parser = LlamaParse()
    parsed = parser.load_data(file_path)
    return parsed[0].text if parsed else ""