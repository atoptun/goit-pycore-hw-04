from colorama import Fore, Back, Style, init


init(autoreset=True)


def catch_errors(func):
    def wraper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            return f"{Fore.RED}Error: {e}"
    return wraper

@catch_errors
def parse_input(line: str) -> tuple:
    cmd, *args = line.split(" ")
    return (cmd.strip().lower(), *args)


@catch_errors
def cmd_add_contact(contacts: dict, args: list[str]) -> str:
    name, phone = args
    contacts[name] = phone
    return f"{Fore.GREEN}Contact added."


@catch_errors
def cmd_change_contact(contacts: dict, args: list[str]) -> str:
    name, phone = args
    if name not in contacts:
        raise Exception("Contact not found.")
    contacts[name] = phone
    return f"{Fore.GREEN}Contact changed."


@catch_errors
def cmd_show_phone(contacts: dict, args: list[str]) -> str:
    name = args[0]
    if name not in contacts:
        raise Exception("Contact not found.")
    return f"{Fore.GREEN}{name}: {Fore.BLUE}{contacts[name]}"


@catch_errors
def cmd_show_all(contacts: dict, args: list) -> str:
    result = ""
    for name, phone in contacts.items():
        result += f"{Fore.GREEN}{name}: {Fore.BLUE}{phone}\n"
    return result


def main():
    print(f"{Fore.CYAN}Welcome to the assistant bot!")

    contacts = {}

    while True:
        command, *args = parse_input(input(f"{Fore.YELLOW}Enter a command:{Fore.RESET} "))

        match command:
            case "hello":
                print(f"{Fore.BLUE}How can I help you?")
            case "add":
                print(cmd_add_contact(contacts, args))
            case "change":
                print(cmd_change_contact(contacts, args))
            case "phone":
                print(cmd_show_phone(contacts, args))
            case "all":
                print(cmd_show_all(contacts, args))
            case "close" | "exit" | "quit":
                print(f"{Fore.GREEN}Have a nice day!")
                break
            case _:
                print(f"{Fore.RED}Invalid command.")


if __name__ == "__main__":
    main()