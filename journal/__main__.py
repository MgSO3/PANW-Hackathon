import click
from .pipeline import run
@click.command
@click.option("--input", default="entries.json", help="Path to input entries file")
@click.option("--output", default="output.json", help="Path to output file")
#Runs pipeline, and prints the last 3 entries
def main(input,output):
    summary = run(input,output)
    click.echo("Last 3 Entries:")
    for item in summary:
        click.echo(f"Entry: {item['entry']}, Sentiment: {item['sentiment']}, Energy Score: {item['energy_score']}/100 ({item['confidence']}% Confidence)")
if __name__ == "__main__":
    main()