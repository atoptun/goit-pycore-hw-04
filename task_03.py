from pathlib import Path
from colorama import Fore, Back, Style, init
import sys
from pprint import pprint


# Excluded directory or file names
init(autoreset=True)

exclude_names = {}

def print_dir_tree(path: str | Path, level: int = 0, prefix: str = "  "):
    """Displays a directory tree using recursion"""
    global exclude_names

    def path_sort(path: Path):
        return (not path.is_dir(), path.name.lower())

    try:
        path = Path(path)
        inner_list = sorted(path.iterdir(), key=path_sort)
        for item in inner_list:
            if item.name in exclude_names:
                continue
            if item.is_dir(): 
                print(f"{prefix * level}{Fore.BLUE}{item.name}/")
                print_dir_tree(item, level+1)
            elif item.is_file():
                print(f"{prefix * level}{Fore.GREEN}{item.name}")
    except OSError as e:
        print(f"{Fore.RED}Error '{path}': {repr(e)}")


def print_dir_tree_non_recursive(path: str | Path, prefix: str = "  "):
    """Display a directory tree without recursion"""
    global exclude_names
    path_stack = []
    path_stack.append({"path": str(path), "level": 0})
    while path_stack:
        try:
            current = path_stack.pop()
            current_path = Path(current["path"])
            current_level = current["level"]
            
            print(f"{prefix * current_level}{Fore.BLUE}{current_path.name}/")
            for item in current_path.iterdir():
                if item.name in exclude_names:
                    continue
                if item.is_dir(): 
                    path_stack.append({"path": str(item), "level": current_level + 1})
                elif item.is_file():
                    print(f"{prefix * (current_level + 1)}{Fore.GREEN}{item.name}")

        except OSError as e:
            print(f"{Fore.RED}Error '{path}': {repr(e)}")


def main():
    global exclude_names
    if len(sys.argv) < 2:
        print(f"{Fore.RED}Wrong parameters. A path is required!")
        return
    if len(sys.argv) > 2:
        exclude_names = set([item.strip() for item in sys.argv[2].split(",") if item.strip()])

    path = str(Path(sys.argv[1]).resolve())
    print(f"Dir: '{path}'")
    print_dir_tree(path)
    # print_dir_tree_non_recursive(path)


# Exec: python3 task_03.py . .venv

if __name__ == "__main__":
    main()
