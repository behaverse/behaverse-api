"""Dataset class."""

from pathlib import Path
import pandas as pd
from tqdm.auto import tqdm
from .utils import download_dataset
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
        name (str): the name to the dataset file. Use
                    [](`~behaverse.list_datasets`) to see available datasets.
        kwargs (dict): additional arguments.

    Raises:
        NotImplementedError: you cannot instantiate this class. Use the class methods instead.
    """

    def __init__(self, name: str, **kwargs) -> None:
        """Initialize the Dataset class."""
        if not kwargs.get('allow_instantiation', False):
            raise NotImplementedError('You cannot instantiate this class. Use the class methods instead.')

        self.name = name

        self.db_path = Path.home() / '.behaverse' / 'datasets' / name

        if not self.db_path.exists():
            raise FileNotFoundError(f'Dataset not found: {self.db_path}')

        # TODO add dataset-level attributes
        # TODO move time-consuming operations to methods and/or lazy load
        self.description = DatasetDescription()

        # SECTION subjects table
        self.subjects = pd.read_csv(self.db_path / 'subjects.csv')
        # !SECTION subjects table

        # SECTION study flow table
        study_flow_files = list(self.db_path.glob('**/study_flow.csv'))

        self.study_flow = pd.concat(
            [pd.read_csv(f, dtype={'subject_id': str, 'session_id': str})
             for f in study_flow_files], axis=0, ignore_index=True)
        # !SECTION study flow table

        # SECTION response table
        response_files = self.study_flow.apply(lambda s:
            (self.db_path /
            f'subject_{s["subject_id"]}' /
            f'session_{s["session_id"]}' /
            f'{s["activity"]}' /
            f'response_{s["attempt"]}.csv').absolute().as_posix(), axis=1).to_list()

        response_dfs = []
        for f in tqdm(response_files):
            if Path(f).exists():
                try:
                    df = pd.read_csv(f)
                    if not df.empty and len(df.columns) > 1:
                        response_dfs.append(df)
                except pd.errors.EmptyDataError:
                    logger.warning(f'Empty response file: {f}')

        self.response = pd.concat(response_dfs, axis=0, ignore_index=True)
        # !SECTION response table

        # SECTION stimulus table
        self.stimulus = ...
        # !SECTION stimulus table

        # SECTION option table
        self.option = ...
        # !SECTION option table

    def select(self) -> 'Dataset':
        """Filter the dataset given some selectors."""
        raise NotImplementedError('Not implemented yet.')

    def load(self, name: str, download: bool = True) -> 'Dataset':
        """Load the dataset with the given name.

        Args:
            name: Name of the dataset to load.
            download: whether to download the dataset if it does not exist.

        Raises:
            NotImplementedError: if the method is not implemented yet.

        """
        raise NotImplementedError('Not implemented yet.')

    @classmethod
    def load_all(cls, name: str, download: bool = True) -> 'Dataset':
        """Load the full dataset, given its name.

        Notes:
            This is a slow operation and should be used with caution.

        Args:
            name: the name to the dataset file. See `list_datasets()` for available
                  datasets.
            download: whether to download the dataset if it does not exist.

        Raises:
            FileNotFoundError: if the dataset does not exist and download is False.

        """
        path = Path.home() / '.behaverse' / 'datasets' / name

        if not path.exists():
            if not download:
                raise FileNotFoundError(f'Dataset not found: {path}')
            download_dataset(name)

        return cls(name, allow_instantiation=True)

    def describe(self) -> DatasetDescription:
        """Provides metadata and information card for the dataset."""
        return self.description

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
            path = Path.home() / '.behaverse' / 'datasets' / self.name
            assert path.exists, f'Path not found: {path.as_posix()}'
            # TODO add more rules here
            return True
        except AssertionError as e:
            logger.error(e)
            return False
