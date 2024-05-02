"""Dataset class."""

from pathlib import Path
import requests
from tqdm.auto import tqdm
from .dataset_description import DatasetDescription
import logging
logger = logging.getLogger(__name__)


class Dataset():
    """Dataset provides methods to load and describe datasets.

    :::{.callout-note}

    Notes:
        You cannot manually instantiate this class. Use the class methods instead, e.g.
        `Dataset.load()`. You can also pass additional
        `allow_instantiation=True` to bypass this restriction.
    :::

    Args:
        path (Path): the path to the dataset file.
        kwargs (dict): additional arguments.

    Raises:
        NotImplementedError: you cannot instantiate this class. Use the class methods instead.
    """

    def __init__(self, path: Path, **kwargs) -> None:
        """Initialize the Dataset class."""
        if not kwargs.get('allow_instantiation', False):
            raise NotImplementedError('You cannot instantiate this class. Use the class methods instead.')

        self.path = path

        # TODO add dataset-level attributes
        self.info = DatasetDescription()
        self.subjects = ...
        self.study_flow = ...
        self.data = ...
        self.response = ...
        self.stimulus = ...
        self.option = ...

    @classmethod
    def load(cls, path: Path | str) -> 'Dataset':
        """Load the dataset from the given path.

        Args:
            path: the path to the dataset file.

        Raises:
            FileNotFoundError: if the dataset directory does not exist.

        """
        if isinstance(path, str):
            path = Path(path)

        if not path.exists():
            raise FileNotFoundError(f'File not found: {path}')

        return cls(path, allow_instantiation=True)

    def validate(self) -> bool:
        """Simple validations to check if the dataset is valid and consistent.

        :::{.callout-note}

        Notes:
            Violations will be logged as errors. Validation rules include:

                1. The dataset path should exist.
                2. TODO add more rules here.
        :::

        Returns:
            bool: True if the dataset is valid, False otherwise.

        """
        try:
            assert self.path.exists(), f'Path not found: {self.path}'
            # TODO add more rules here
            return True
        except AssertionError as e:
            logger.error(e)
            return False
