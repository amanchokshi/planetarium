import click

from . import __version__


@click.command()
@click.version_option(version=__version__)
def main():
    """The Planetarium Python Project."""
    click.echo("A playground of planetary imaging tools")
