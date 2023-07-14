import sys


def txt_importer(path_file):
    if not path_file.endswith(".txt"):
        print("Formato inválido", file=sys.stderr)
    try:
        with open(path_file, mode="r") as file:
            file_lines = []
            for line in file.readlines():
                file_lines.append(line.strip("\n"))
            return file_lines
    except FileNotFoundError:
        print(f"Arquivo {path_file} não encontrado", file=sys.stderr)
