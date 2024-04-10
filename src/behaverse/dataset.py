"""Dataset class."""

from pathlib import Path
import requests
from tqdm.auto import tqdm
from utils import extract_file


class Dataset():
    """Dataset provides methods to download and load datasets."""

    def __init__(self) -> None:
        """Initialize the Dataset class.

        Raises:
            NotImplementedError: you cannot instantiate this class. Use the class methods instead.
        """
        raise NotImplementedError('Dataset class instantiation is not implemented yet.')

    @classmethod
    def download_dataset(cls, url: str, path: Path | str, **kwargs):
        """Download dataset from the given URL."""
        if not url or not path:
            raise ValueError('URL and path are required.')

        chunk_size = kwargs.get('chunk_size', 8192)

        if not isinstance(path, Path):
            # support string path
            path = Path(path)

        if path.exists():
            print(f'Dataset file already exists: {path.as_posix()}')
            extract_file(path, path.parent)
            return

        path.parent.mkdir(parents=True, exist_ok=True)

        with requests.get(url, stream=True) as r:
            r.raise_for_status()

            with open(path, 'wb') as f:
                for chunk in tqdm(r.iter_content(chunk_size=chunk_size), leave=False):
                    f.write(chunk)

        print(f'Downloaded dataset to {path.as_posix()}')
        extract_file(path, path.parent)

    @classmethod
    def load_dataset(cls, path: Path):
        """Load the dataset from the given path."""
        if not path.exists():
            raise FileNotFoundError(f'File not found: {path}')

        raise NotImplementedError('Loading dataset is not implemented yet.')
