"""TODO: Access Behaverse datasets via Behaverse Registry."""


import logging
from pathlib import Path
logger = logging.getLogger(__name__)


def download_dataset(name: str, **kwargs) -> Path:
    """Download a dataset from the dvc-managed Behaverse registry.

    Args:
        name: the name of the dataset to download.
        kwargs (dict): additional arguments. For example you can specify the destination
                        path (`dest`) to save the dataset file. Defaults to
                        `~/.behaverse/datasets/{name}/`. Or `chunk_size` to specify the chunk size for downloading.

    Returns:
        Path: Path to the downloaded dataset file.

    Raises:
        ImportError: if DVC is not installed.
        FileNotFoundError: if the dataset is not found.
        AssertionError: if the dataset name is not provided.
    """
    from dvc.api import DVCFileSystem

    assert name is not None, 'Dataset name is required.'

    # FIXME: query DVC registry for the url of the dataset

    repo = 'git@github.com:behaverse/behaverse.git'
    fs = DVCFileSystem(repo, rev='Registry', remote='origin')

    dest = Path(kwargs.get('dest',
                           Path.home() / '.behaverse' / 'datasets' / f'{name}.tar.gz'))

    fs.get(f'datasets/{name}.tar.gz.dvc', f'tmp/{name.replace("/", "-")}')

    if dest.exists():
        return ...  # TODO path to the extract_dataset() call

    dest.parent.mkdir(parents=True, exist_ok=True)

    # TODO save to 'dest'

    logger.info(f'Downloaded DVC dataset to {dest}, now extracting...')

    output_path: Path = ...  # TODO extract_dataset(name)
    logger.info(f'Extracted DVC dataset to {output_path}')
    return output_path
