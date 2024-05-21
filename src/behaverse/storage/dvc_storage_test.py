"""Test for dvc.py."""

from behaverse.storage.dvc_storage import download_dataset


def test_download_dataset():
    """Test download_dataset function."""
    download_dataset('P500_9subjects/L1m')
    assert True
