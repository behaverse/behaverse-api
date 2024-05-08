# Behaverse Data/Model Registry

This repository contains a collection of datasets that can be accessed using the [`behaverse`](https://behaverse.github.io) package. The datasets are stored in the `datasets` folder and are organized by the name of the dataset. Each dataset is stored in a separate folder and contains the following files:

| File | Description |
| ---- | ----------- |
| `README.md` | A description of the dataset, including the dataset card. |
| `LICENSE` | The license of the dataset. |
| `L1.tar.gz.dvc` | DVC link to the L1 BDM data. Upon downloading the data, you can extract the data using `tar -xvzf L1.tar.gz`. |
| (optional) `L2.tar.gz.dvc`, etc | DVC pointers to the L2 data, or other processed data. |


All the large files are managed using [DVC](https://dvc.org/). You just need to [install `dvc`](https://dvc.org/doc/install) and run corresponding commands to upload or download the data.

