import logging
from pathlib import Path

import typer
import pandas as pd


app = typer.Typer()


@app.callback()
def main() -> None:
    """Determine animal shelter outcomes."""
    logging.basicConfig(
        level=logging.INFO,
        format="[%(asctime)-15s] %(name)s - %(levelname)s - %(message)s",
    )


@app.command()
def train(input_path: Path, model_path: Path) -> None:
    """Trains a model on the given dataset."""

    logger = logging.getLogger(__name__)

    logger.info("Loading input dataset from %s", input_path)
    train_dataset = pd.read_csv(input_path)
    logger.info("Found %i rows", len(train_dataset))

    # TODO: Fill in your solution.
    # - Separate X from y
    # - Fit a model
    # - Log the final score
    # - Save model

    logger.info(f"Wrote model to {model_path}")
