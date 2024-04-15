"""Functional interface for datasets.

This module provides a functional interface to interact with datasets.

"""

from .dataset import Dataset
from .dataset_info import DatasetInfo
from pathlib import Path
import logging
logger = logging.getLogger(__name__)


def list_datasets() -> list[Dataset]:
    """List available datasets.

    Returns:
        list: List of available datasets.

    """
    raise NotImplementedError('Not implemented yet.')


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
