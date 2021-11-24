# STSb Turkish

Semantic textual similarity dataset for the Turkish language. It is a machine translation (Azure) of the [STSb English](http://ixa2.si.ehu.eus/stswiki/index.php/STSbenchmark) dataset. This dataset is not reviewed by expert human translators.

## How to download in Python

```python
import requests
import pandas as pd

STS_URLS = {
    "train": "https://raw.githubusercontent.com/emrecncelik/sts-benchmark-tr/main/sts-train-tr.csv",
    "dev": "https://raw.githubusercontent.com/emrecncelik/sts-benchmark-tr/main/sts-dev-tr.csv",
    "test": "https://raw.githubusercontent.com/emrecncelik/sts-benchmark-tr/main/sts-test-tr.csv",
}

def get_github_dataset(dataset_url: str):
    dataset_file = requests.get(dataset_url).content
    dataset = pd.read_csv(io.StringIO(dataset_file.decode("utf-8")))
    return dataset
```
