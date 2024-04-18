"""Functional interface for datasets.

This module provides a functional interface to interact with datasets.

"""

from .dataset import Dataset
from .dataset_info import DatasetInfo
from pathlib import Path
import pandas as pd
import logging
logger = logging.getLogger(__name__)


def list_datasets() -> pd.DataFrame:
    """List available datasets.

    Returns:
        DataFrame: List of available datasets including name, description, and url.

    """
    # use requests to get the list of datasets and parse it using yaml
    import requests
    import yaml
    url = 'https://morteza.github.io/datasets/behaverse.yml'
    response = requests.get(url)
    if response.status_code == 200:
        datasets = pd.DataFrame(yaml.safe_load(response.text))
        return datasets
    else:
        logger.error(f'Failed to get the list of datasets from {url}.')
        raise Exception(f'Failed to get the list of datasets from {url}.')


def download_dataset(name: str, dest: Path | str) -> Path:
    """Download the dataset with the given name.

    Args:
        name: Name of the dataset to download.
        dest: Destination path to save the dataset.

    Returns:
        Path: Path to the downloaded dataset.

    """
    raise NotImplementedError('Not implemented yet.')


def load_dataset(name: str, **kwargs) -> Dataset:
    """Load the dataset with the given name.

    Args:
        name: Name of the dataset to load.
        kwargs (dict): Additional arguments.

    Returns:
        Dataset: Loaded dataset.

    """
    raise NotImplementedError('Not implemented yet.')


def get_dataset_info(name: str) -> DatasetInfo:
    """Describe the dataset with the given name.

    Args:
        name: Name of the dataset to describe.

    Returns:
        str: Description of the dataset.

    """
    raise NotImplementedError('Not implemented yet.')


def validate_dataset(name: str) -> bool:
    """Validate the dataset with the given name.

    Args:
        name: Name of the dataset to validate.

    Returns:
        bool: True if the dataset is valid, False otherwise.

    """
    raise NotImplementedError('Not implemented yet.')
