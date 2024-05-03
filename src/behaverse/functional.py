"""Functional interface for datasets.

This module provides a functional interface to interact with datasets.

"""

from .dataset import Dataset
from .dataset_description import DatasetDescription
import logging
logger = logging.getLogger(__name__)


def load_dataset(name: str, **kwargs) -> Dataset:
    """Load the dataset with the given name.

    Args:
        name: Name of the dataset to load.
        kwargs (dict): Additional arguments.

    Returns:
        Dataset: Loaded dataset.

    """
    return Dataset.load(name, **kwargs)


def describe_dataset(name: str) -> DatasetDescription:
    """Describe the dataset with the given name.

    Args:
        name: Name of the dataset to describe.

    Returns:
        DatasetDescription: Metadata and description of the dataset.

    """
    return Dataset.load(name).describe()


def validate_dataset(name: str) -> bool:
    """Validate the dataset with the given name.

    Args:
        name: Name of the dataset to validate.

    Returns:
        bool: True if the dataset is valid, False otherwise.

    """
    raise NotImplementedError('Not implemented yet.')
