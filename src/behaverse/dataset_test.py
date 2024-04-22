"""Test the dataset module."""

from pathlib import Path

from .dataset import Dataset


def test_download_dataset_from_onedrive():
    """Download a behaverse dataset from a public OneDrive link."""
    url = ('https://edu.lu/kwmqa')

    Dataset.download(url, Path('tmp/P500-L1m.tar.gz'))
