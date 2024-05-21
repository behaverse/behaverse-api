"""Utility functions."""

from pathlib import Path
import tarfile
import logging
logger = logging.getLogger(__name__)


def extract_dataset(name: str, **kwargs) -> Path:
    """Extract a dataset and return the path to the extracted directory.

    Args:
        name: Name of the datasets, e.g., `P500` for a compressed file of the name
              `P500.tar.gz`.
        kwargs (dict): Additional arguments, including `dest` which is the
                       destination directory to extract the file. Defaults to (i.e.,
                       `~/.behaverse/datasets/{name}/`).

    Returns:
        Path: Path to the extracted directory.

    """
    src = (Path.home() /
           '.behaverse' /
           'datasets' /
           f'{name.replace('/', '-')}.tar.gz')

    if not src.exists():
        raise FileNotFoundError(f'{src} not found.')

    dest = Path(kwargs.get('dest', Path.home() / '.behaverse' / 'datasets'))

    if not dest.exists():
        dest.mkdir(parents=True, exist_ok=True)
        logger.info(f'Destination directory created: {dest.parent}')

    # TODO support both .tar.* and .tar formats
    ext = src.suffixes[-1].replace('.', '')
    tar = tarfile.open(src, f'r:{ext}')
    # Python 3.12+ gives a deprecation warning if TarFile.extraction_filter is None.
    if hasattr(tarfile, 'fully_trusted_filter'):
        tar.extraction_filter = staticmethod(tarfile.fully_trusted_filter)  # type: ignore

    tar.extractall(dest)
    output_folder = dest / tar.getnames()[1]
    tar.close()
    logger.info(f'Extracted to {output_folder}')

    return output_folder
