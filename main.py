import os
from pathlib import Path

from PyVDF import PyVDF

LOGIN_USERS = Path(Path.home() / ".local/share/Steam/config/loginusers.vdf")
REGISTRY = Path(Path.home() / ".steam/registry.vdf")


def main():
    print("Current account:", get_account())

    accounts = get_accounts()
    account = choose_account(accounts)
    set_account(account)

    if input("\nKill steam? [Y/n]: ").lower() != "n":
        os.system("killall steam")


def get_accounts():
    user_registry = PyVDF(infile=LOGIN_USERS)
    return user_registry.find("users")


def choose_account(accounts):
    accounts_to_choose = {
        account['AccountName']: [str(i), account['AccountName'], account['PersonaName']]
        for i, account in enumerate(accounts.values())
    }

    while True:
        print("\nChoose an account:")
        for i, name, username in accounts_to_choose.values():
            print(f"{i}: {name} ({username})")
        acc = input()
        for account, names in accounts_to_choose.items():
            if acc in names:
                return account


def get_account():
    registry = PyVDF(infile=REGISTRY)
    return registry.find("Registry.HKCU.Software.Valve.Steam.AutoLoginUser")


def set_account(account):
    registry = PyVDF(infile=REGISTRY)
    registry.edit("Registry.HKCU.Software.Valve.Steam.AutoLoginUser", account)
    registry.write_file(REGISTRY)


main()
