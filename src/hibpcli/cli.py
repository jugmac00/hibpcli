from typing import Optional

import click

from hibpcli.exceptions import ApiError, KeepassError
from hibpcli.keepass import check_passwords_from_db
from hibpcli.leaks import LeaksStore


@click.group()
def main() -> None:
    """Command line interface to the haveibeenpwned.com API."""
    pass


@click.command()
@click.argument("path")
@click.option("--password", default=None, help="Password for the KeePass database.")
def check_keepass(path: str, password: Optional[str]) -> None:
    """Check all passwords stored in the keepass database."""
    if password is None:
        password = click.prompt(
            "Please enter the master password for the database", hide_input=True
        )
    try:
        rv = check_passwords_from_db(path=path, master_password=password)
    except KeepassError:
        click.echo("The entered password is not correct. Please try again.")
    except ApiError as e:
        click.echo(str(e))
    else:
        if rv:
            click.echo("The passwords of following entries are leaked:")
            click.echo(rv)
        else:
            click.echo("Your passwords have not been reported leaked until now.")


@click.command()
@click.option("--password", default=None, help="Password which should be checked.")
def check_password(password: Optional[str]) -> None:
    """Check a single password."""
    if password is None:
        password = click.prompt(
            "Please enter a password which should be checked", hide_input=True
        )
    leaksstore = LeaksStore()
    try:
        is_leaked = password in leaksstore
    except ApiError as e:
        click.echo(str(e))
    else:
        if is_leaked:
            click.echo("Please change your password!")
        else:
            click.echo("Your password has not been reported leaked until now.")


main.add_command(check_keepass)
main.add_command(check_password)


if __name__ == "__main__":
    main()
