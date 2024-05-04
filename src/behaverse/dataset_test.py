"""Test the dataset module."""

from pathlib import Path


def test_download_dataset():
    """Download a behaverse dataset from a public OneDrive link."""
    # datasets = list_datasets()
    # url = datasets.query('name == "P500-L1m"')['url'].item()
    # print(url)

    from .utils import download_dataset

    output = download_dataset('P500-L1m')

    assert output.exists()
    assert output.is_dir()
    assert len(list(output.iterdir())) > 0
    assert output == Path.home() / '.behaverse' / 'datasets' / 'P500-L1m'


def test_load_dataset():
    """Load a behaverse dataset."""
    from .dataset import Dataset

    dataset = Dataset.load_all('P500-L1m')

    assert dataset.name == 'P500-L1m'
    assert len(dataset.subjects) > 0
    assert len(dataset.study_flow) > 0
    assert len(dataset.response) > 0
