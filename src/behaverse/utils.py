"""Generic utility functions."""

from pathlib import Path
import tarfile
import logging
logger = logging.getLogger(__name__)


def extract_file(path: Path, dest: Path):
    """Extract the given tar.* file.

    Args;
        path: Path to the compressed tar file, e.g., with tar.gz or
                     tar.xz extension.
        dest: Destination directory to extract the file.

    """
    if '.tar' not in path.suffixes:
        raise ValueError('Only .tar files are supported.')

    if dest is None:
        dest = path.parent
        logger.info('Destination path is not provided.'
                    'Extracting to the parent directory.')

    if not dest.exists():
        dest.mkdir(parents=True, exist_ok=True)
        logger.info(f'Destination directory created: {dest}')

    # TODO support both .tar.* and .tar formats
    ext = path.suffixes[-1]
    tar = tarfile.open(path, f'r:{ext}')
    # Python 3.12+ gives a deprecation warning if TarFile.extraction_filter is None.
    if hasattr(tarfile, 'fully_trusted_filter'):
        tar.extraction_filter = staticmethod(tarfile.fully_trusted_filter)  # type: ignore

    tar.extractall(dest)
    tar.close()

    logger.info(f'Extracted to {dest}')
