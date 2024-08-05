#!/usr/bin/env python3

import click
from commands import create

@click.group()
def cli():
    """My Framework Command Line Interface."""
    pass

cli.add_command(create.create)

if __name__ == "__main__":
    cli()