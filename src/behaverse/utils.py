"""Generic utility functions."""

from pathlib import Path
from tqdm.auto import tqdm
import requests
import tarfile
import logging
logger = logging.getLogger(__name__)


def extract_dataset(path: Path, dest: Path) -> Path:
    """Extract the given tar.* file.

    Args;
        path: Path to the compressed tar file, e.g., with tar.gz or
                     tar.xz extension.
        dest: Destination directory to extract the file.

    Returns:
        Path: Path to the extracted directory.

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
    ext = path.suffixes[-1].replace('.', '')
    tar = tarfile.open(path, f'r:{ext}')
    # Python 3.12+ gives a deprecation warning if TarFile.extraction_filter is None.
    if hasattr(tarfile, 'fully_trusted_filter'):
        tar.extraction_filter = staticmethod(tarfile.fully_trusted_filter)  # type: ignore

    tar.extractall(dest)
    output_folder = dest / tar.getnames()[0]
    tar.close()

    logger.info(f'Extracted to {dest}')

    return output_folder


def download_dataset(url: str, dest: Path | str, **kwargs) -> Path:
    """Download dataset from the given URL.

    Args:
        url: the URL to download the dataset from.
        dest: the path to save the dataset file.
        kwargs (dict): additional arguments.
    """
    if not url or not dest:
        raise ValueError('URL and path are required.')

    chunk_size = kwargs.get('chunk_size', 8096)

    if isinstance(dest, str):
        dest = Path(dest)

    if dest.exists():
        logger.warning(f'Dataset file already exists: {dest.as_posix()}')
        extract_dataset(dest, dest.parent)
        return dest

    dest.parent.mkdir(parents=True, exist_ok=True)

    with requests.get(url, stream=True) as r:
        r.raise_for_status()

        with open(dest, 'wb') as f:
            for chunk in tqdm(r.iter_content(chunk_size=chunk_size), leave=False, unit='B'):
                f.write(chunk)

    output_path = extract_file(dest, dest.parent)
    logger.info(f'Extracted dataset to {output_path}')
    return output_path
