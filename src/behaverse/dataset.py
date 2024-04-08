from pathlib import Path
import requests
import tarfile
from tqdm.auto import tqdm


class Dataset():

    def __init__(self) -> None:
        raise NotImplementedError('Dataset class instantiation is not implemented yet.')

    @classmethod
    def _extract_dataset(cls, path: Path):
        if '.tar' in path.suffixes:
            # TODO support both .tar.* and .tar formats
            tar = tarfile.open(path, f'r:gz')
            # Python 3.12+ gives a deprecation warning if TarFile.extraction_filter is None.
            if hasattr(tarfile, 'fully_trusted_filter'):
                tar.extraction_filter = staticmethod(tarfile.fully_trusted_filter)  # type: ignore
            tar.extractall(path.parent)
            tar.close()
            print(f'Extracted dataset to {path.parent.as_posix()}')

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
            cls._extract_dataset(path)
            return

        path.parent.mkdir(parents=True, exist_ok=True)

        with requests.get(url, stream=True) as r:
            r.raise_for_status()

            with open(path, 'wb') as f:
                for chunk in tqdm(r.iter_content(chunk_size=chunk_size), leave=False):
                    f.write(chunk)


        print(f'Downloaded dataset to {path.as_posix()}')

        cls._extract_dataset(path)


    @classmethod
    def load_dataset(cls, path: Path):
        """Load the dataset from the given path."""
        if not path.exists():
            raise FileNotFoundError(f'File not found: {path}')

        raise NotImplementedError('Loading dataset is not implemented yet.')
