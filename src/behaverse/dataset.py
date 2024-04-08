from pathlib import Path
import requests

class Dataset():

    def __init__(self) -> None:
        raise NotImplementedError('Dataset class instantiation is not implemented yet.')

    @classmethod
    def download_dataset(cls, url, path: Path, **kwargs):
        """Download dataset from the given URL."""
        if not url or not path:
            raise ValueError('URL and path are required.')
        if Path(path).exists():
            return

        path.mkdir(parents=True, exist_ok=True)

        with requests.get(url, stream=True) as r:
            r.raise_for_status()

            with open(path, 'wb') as f:
                for chunk in r.iter_content(chunk_size=8192):
                    f.write(chunk)

        print(f'Downloaded dataset to {path.as_posix()}')

    @classmethod
    def load_dataset(cls, path: Path):
        """Load the dataset from the given path."""
        if not path.exists():
            raise FileNotFoundError(f'File not found: {path}')

        raise NotImplementedError('Loading dataset is not implemented yet.')
