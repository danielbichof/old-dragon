from typer import Typer

app = Typer()


@app.command
def main():
    print("Old Dragon game:")
