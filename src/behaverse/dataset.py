"""Dataset class."""

from pathlib import Path
import requests
from tqdm.auto import tqdm
from utils import extract_file
from .dataset_info import DatasetInfo
import logging
logger = logging.getLogger(__name__)


class Dataset():
    """Dataset provides methods to download and load datasets."""

    def __init__(self, path: Path, **kwargs) -> None:
        """Initialize the Dataset class.

        Args:
            path (Path): the path to the dataset file.
            kwargs (dict): additional arguments.

        Raises:
            NotImplementedError: you cannot instantiate this class. Use the class methods instead.
        """
        if not kwargs.get('allow_instantiation', False):
            raise NotImplementedError('You cannot instantiate this class. Use the class methods instead.')

        self.path = path

    @classmethod
    def download(cls, url: str, dest: Path | str, **kwargs) -> Path:
        """Download dataset from the given URL."""
        if not url or not dest:
            raise ValueError('URL and path are required.')

        chunk_size = kwargs.get('chunk_size', 8192)

        if not isinstance(dest, Path):
            # support string path
            dest = Path(dest)

        if dest.exists():
            logger.warning(f'Dataset file already exists: {dest.as_posix()}')
            extract_file(dest, dest.parent)
            return dest

        dest.parent.mkdir(parents=True, exist_ok=True)

        with requests.get(url, stream=True) as r:
            r.raise_for_status()

            with open(dest, 'wb') as f:
                for chunk in tqdm(r.iter_content(chunk_size=chunk_size), leave=False):
                    f.write(chunk)

        output_path = extract_file(dest, dest.parent)
        logger.info(f'Extracted dataset to {output_path}')
        return output_path

    @classmethod
    def load(cls, path: Path) -> 'Dataset':
        """Load the dataset from the given path.

        Args:
            path (Path): the path to the dataset file.

        Raises:
            FileNotFoundError: if the dataset directory does not exist.

        """
        if not path.exists():
            raise FileNotFoundError(f'File not found: {path}')

        return cls(path, allow_instantiation=True)

    def validate(self) -> bool:
        """Simple validations to check if the dataset is valid and consistent.

        Violations will be logged as errors. Validation rules include:
            - The dataset path should exist.
            - TODO add more rules here.

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

    def info(self) -> DatasetInfo:
        """Get dataset information."""
        raise NotImplementedError('Get dataset information is not implemented yet.')
