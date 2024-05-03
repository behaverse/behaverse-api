"""Test the dataset module."""

from pathlib import Path
from .utils import download_dataset


def test_download_dataset():
    """Download a behaverse dataset from a public OneDrive link."""
    # datasets = list_datasets()
    # url = datasets.query('name == "P500-L1m"')['url'].item()
    # print(url)

    output = download_dataset('P500-L1m')

    assert output.exists()
    assert output.is_dir()
    assert len(list(output.iterdir())) > 0
    assert output == Path.home() / '.behaverse' / 'datasets' / 'P500-L1m'
