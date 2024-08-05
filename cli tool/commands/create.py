#!/usr/bin/env python3

import click
import os
import json
import subprocess

@click.command()
@click.argument('name')
def create(name):
    """Create a project structure with the given NAME and a config.json file."""
    
    # Define the project structure
    project_dir = name
    files_and_dirs = {
        'app.py': '',
        'config.json': '',
        'license': '',
        'assets': '',
        'requirements.txt': ''  # Add requirements.txt to the structure
    }

    # Get user input for config.json
    name_input = click.prompt("Enter the project name", default=name)
    description_input = click.prompt("Enter the project description")
    publisher_input = click.prompt("Enter the project publisher")

    # Define the config.json content
    config_content = {
        'name': name_input,
        'description': description_input,
        'publisher': publisher_input,
        'version': '1.0.0',
        'port': 8000,
        'nginx': {
            'server_name': name_input,
            'location': '/'
        }
    }

    # Define the requirements.txt content
    requirements_content = """
click==8.0.3
"""  # Add your required packages here

    # Create the main project directory
    try:
        os.makedirs(project_dir, exist_ok=True)

        # Create files and directories
        for file_name, content in files_and_dirs.items():
            path = os.path.join(project_dir, file_name)
            if file_name == 'config.json':
                # Write JSON content to config.json
                with open(path, 'w') as f:
                    json.dump(config_content, f, indent=4)
            elif file_name == 'requirements.txt':
                # Write requirements content to requirements.txt
                with open(path, 'w') as f:
                    f.write(requirements_content)
            elif content == '':
                # If content is empty, it's a directory
                os.makedirs(path, exist_ok=True)
            else:
                # Create files with specified content
                with open(path, 'w') as f:
                    f.write(content)

        # Provide instructions
        click.echo(f"Project {name} created successfully.")
        click.echo("______________________________________")
        click.echo(f" cd {name}")
        click.echo(f" apex run")

    except Exception as e:
        click.echo(f"An error occurred: {e}")

if __name__ == '__main__':
    create()
