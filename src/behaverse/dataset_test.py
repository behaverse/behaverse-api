"""Test the dataset module."""

from pathlib import Path

from behaverse import Dataset, list_datasets


def test_download_dataset_from_onedrive():
    """Download a behaverse dataset from a public OneDrive link."""
    datasets = list_datasets()
    url = datasets.query('name == "P500-L1m"')['url'].item()
    print(url)

    Dataset.download(url, Path('tmp/P500-L1m.tar.gz'))
