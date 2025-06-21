from pathlib import Path
from pprint import pprint


def get_cats_info(path: str) -> list[dict]: 
    """Parses a file and returns a list of cats"""
    result = []
    try:
        with open(path, mode="r", encoding="utf-8") as file:
            lines = file.readlines()
    except OSError as e:
        print(f"Open file error: {repr(e)}")
        return result
    
    for ind, line in enumerate(lines):
        try:
            line = line.strip()
            if not line: continue
            id, name, age = line.split(",")
            age = float(age.strip())
            result.append({
                "id": id,
                "name": name,
                "age": age,
            })
        except Exception as e:
            print(f"Wrong format of line ({ind}): '{line}'. Error: {repr(e)}")

    return result


def main():
    file_path = str((Path.cwd()/"data"/"cats.txt").resolve())
    print(f"File: '{file_path}'")
    cats_info = get_cats_info(file_path)
    pprint(cats_info)


if __name__ == "__main__":
    main()
