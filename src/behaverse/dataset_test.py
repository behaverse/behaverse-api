"""Test the dataset module."""

from pathlib import Path

from .utils import download_dataset
from .functional import list_datasets


def test_download_dataset():
    """Download a behaverse dataset from a public OneDrive link."""
    datasets = list_datasets()
    url = datasets.query('name == "P500-L1m"')['url'].item()
    print(url)

    download_dataset(url, Path('tmp/P500-L1m.tar.gz'))
