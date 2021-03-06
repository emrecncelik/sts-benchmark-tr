# STSb Turkish

Semantic textual similarity dataset for the Turkish language. It is a machine translation (Azure) of the [STSb English](http://ixa2.si.ehu.eus/stswiki/index.php/STSbenchmark) dataset. This dataset is not reviewed by expert human translators. Also available in [HuggingFace Datasets](https://huggingface.co/datasets/emrecan/stsb-mt-turkish).

## Download
### From the repository
```python
import io
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

### From [HuggingFace Datasets](https://huggingface.co/datasets/emrecan/stsb-mt-turkish)

```python
from datasets import load_dataset

dataset = load_dataset("emrecan/stsb-mt-turkish")
```
