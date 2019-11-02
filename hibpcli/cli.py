import click

from hibpcli.keepass import check_passwords_from_db
from hibpcli.password import Password


@click.group()
def main():
    """Command line interface to the haveibeenpwned.com API."""
    pass


@click.command()
@click.option('--path', default=None, help='Path to KeePass database.')
@click.option('--password', default=None, help='Password to the KeePass database.')
def keepass(path, password):
    """Check all passwords stored in the keepass database."""
    if path is None:
        path = click.prompt(
            "Please enter the path to the database", type=click.Path(exists=True)
        )
    if password is None:
         password = click.prompt(
            "Please enter the master password for the database", hide_input=True
        )
    # needs error handling
    rv = check_passwords_from_db(path=path, master_password=password)
    if rv:
        click.echo("The passwords of following entries are leaked:")
        click.echo(rv)
    else:
        click.echo("Hooray, everything is safe!")


@click.command()
@click.option('--password', default=None, help='Password which should be checked.')
def password(password):
    """Check a single password."""
    #breakpoint()
    if password is None:
         password = click.prompt(
            "Please enter a password which should be checked", hide_input=True
        )
    p = Password(password)
    if p.is_leaked():
        click.echo("Please change your password!")
    else:
        click.echo("Your password is safe!")

main.add_command(keepass)
main.add_command(password)


if __name__ == "__main__":
    main()
