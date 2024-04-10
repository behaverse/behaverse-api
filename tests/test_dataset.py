"""Test the dataset module."""

from pathlib import Path

from behaverse.dataset import Dataset


def test_download_dataset_from_onedrive():
    """Download a behaverse dataset from a public OneDrive link."""
    url = ('https://uniluxembourg-my.sharepoint.com/:u:/g/personal/morteza_ansarinia_uni_lu/Ect90jSbAJBIrGNdbFqPbGUBCoH9zaeHoyvcpaKkZjSOqw?e=RUbZGh&download=1')

    Dataset.download_dataset(url, Path('tmp/P500-L1m.tar.gz'))
