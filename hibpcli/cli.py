import click

from hibpcli.keepass import check_passwords_from_db


@click.command()
def main():
    """Command line interface to the haveibeenpwned.com API."""
    path = click.prompt("Please enter the path to the database", type=click.Path(exists=True))
    master_password = click.prompt("Please enter the master password for the database", hide_input=True)
    # needs error handling
    rv = check_passwords_from_db(path=path, master_password=master_password)
    if rv:
        click.echo("The passwords of following entries are leaked:")
        click.echo(rv)
    else:
        click.echo("Hooray, everything is safe!")


if __name__ == "__main__":
    main()
