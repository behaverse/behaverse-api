"""Utility functions for DVC datasets."""

import logging
from pathlib import Path
logger = logging.getLogger(__name__)


def download_dvc_dataset(name: str, **kwargs) -> Path:
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
    try:
        import dvc.api
    except ImportError as e:
        raise ImportError(
            'DVC is required to download the dataset.'
             'Please follow https://dvc.org/doc/install to install DVC.') from e

    assert name is not None, 'Dataset name is required.'

    # TODO: query DVC registry for the url of the dataset
    # NOTE: git repo: https://github.com/behaverse/behaverse.git
    # NOTE: git ssh: git@github.com:behaverse/behaverse.git
    # NOTE: rev: registry
    url = ...

    dest = Path(kwargs.get('dest',
                           Path.home() / '.behaverse' / 'datasets' / f'{name}.tar.gz'))
    chunk_size = kwargs.get('chunk_size', 8096)

    if dest.exists():
        return ...  # TODO path to the extract_dataset() call

    dest.parent.mkdir(parents=True, exist_ok=True)

    # TODO save to 'dest'

    logger.info(f'Downloaded DVC dataset to {dest}, now extracting...')

    output_path: Path = ...  # TODO extract_dataset(name)
    logger.info(f'Extracted DVC dataset to {output_path}')
    return output_path
