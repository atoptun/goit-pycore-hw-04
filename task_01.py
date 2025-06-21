from pathlib import Path


def load_salaries(path: str) -> list[float]:
    """Parses a file and returns a list of salaries"""
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
            _, salary = line.split(",")
            salary = float(salary.strip())
            result.append(salary)
        except Exception as e:
            print(f"Wrong format of line ({ind}): '{line}'. Error: {repr(e)}")

    return result


def total_salary(path: str) -> tuple[float, float]:
    """Returns the total and average salary"""
    salaries = load_salaries(path)
    if not salaries:
        return 0, 0
    
    salary_total = sum(salaries)
    salary_avg = round(salary_total / len(salaries), 2)

    return salary_total, salary_avg


def main():
    file_path = str((Path.cwd()/"data"/"salary.txt").resolve())
    print(f"File: '{file_path}'")
    total, average = total_salary(file_path)
    print(f"Total: {total}. Average: {average}")


if __name__ == "__main__":
    main()
