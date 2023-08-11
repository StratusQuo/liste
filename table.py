import os
import typer
from rich.console import Console
from rich.table import Table
from rich import box
from ls_modules import get_permissions, file_icon
from rich.text import Text
from color_settings import *

class DirectoryLister:
    
    def __init__(self, directory="."):
        self.directory = directory
        self.console = Console()

    def list_files(self):
       
        files = os.listdir(self.directory) # Get list of files and directories in the given directory

        #================
        # Create a table
        #================

        table = Table(show_header=True, header_style='bold green', box=box.SIMPLE_HEAD)
        table.add_column('Permissions', style = darkGrey)
        table.add_column("Name", style = canary)
        table.add_column("Type")
        table.add_column("Size (Bytes)", style = tan)        

        for file in files:
            filepath = os.path.join(self.directory, file)
            permissions = get_permissions(filepath)
            icon = file_icon(file)

            # Determine if it's a file or directory

            if os.path.isdir(filepath):
                file_type = "Directory"
                size = "-"
                file_display = Text(f'{icon} {file}', style = blue)
            else:
                file_type = "File"
                size = os.path.getsize(filepath)
                file_display = f'{icon} {file}'

            table.add_row(permissions, file_display, file_type, str(size))

        self.console.print(table)

def main(directory: str = typer.Argument(".")):
    lister = DirectoryLister(directory)
    lister.list_files()

if __name__ == "__main__":
    typer.run(main)
