import click

from hibpcli.keepass import check_passwords_from_db


@click.command()
def main():
    path = click.prompt("Please enter the path to the database")
    master_password = click.prompt("Please enter the master password for the database")
    # needs error handling
    rv = check_passwords_from_db(path=path, master_password=master_password)
    if rv:
        click.echo("The passwords of following entries are leaked:")
        click.echo(rv)
    else:
        click.echo("Hooray, everything is safe!")


if __name__ == "__main__":
    main()
