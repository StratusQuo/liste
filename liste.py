import typer
from table import DirectoryLister

app = typer.Typer(name='liste', help='A rich ls alternative')

@app.command()
def main(
    directory: str = typer.Argument('.', help="Directory to list."),
    table: bool = typer.Option(False, '-t', '--table', help="Display as table.")
):
    if table:
        list_table = DirectoryLister(directory)
        list_table.list_files()
    else:
        raise typer.Exit(code = 1)


if __name__ == "__main__":
    app()


