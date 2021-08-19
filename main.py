# %%
import os
import re
import time
import json
import pandas as pd
from tqdm import tqdm
from csv import QUOTE_NONE
from translate import translate


def natural_key(string_):
    return [int(s) if s.isdigit() else s for s in re.split(r"(\d+)", string_)]


def get_translations(data, data_name, batch_size=20):
    for i in tqdm(range(0, len(data), batch_size)):
        s1_translations = translate(list(data[5][i : i + batch_size]))
        s2_translations = translate(list(data[6][i : i + batch_size]))

        with open(
            f"sts-tr/{data_name}/s1_{data_name}_{i}.json", "w", encoding="utf-8"
        ) as f:
            json.dump(s1_translations, f, ensure_ascii=False, indent=4)

        with open(
            f"sts-tr/{data_name}/s2_{data_name}_{i}.json", "w", encoding="utf-8"
        ) as f:
            json.dump(s2_translations, f, ensure_ascii=False, indent=4)
        time.sleep(0.01)


def parse_json_files(data_name):
    files = os.listdir(f"sts-tr/{data_name}")
    s1_files = [f for f in files if "s1" in f]
    s2_files = [f for f in files if "s2" in f]

    s1_files = sorted(s1_files, key=natural_key)
    s2_files = sorted(s2_files, key=natural_key)

    s1 = []
    s2 = []
    for s1_file, s2_file in zip(s1_files, s2_files):
        with open(f"sts-tr/{data_name}/{s1_file}", "r") as f:
            s1_json = json.load(f)

        with open(f"sts-tr/{data_name}/{s2_file}", "r") as f:
            s2_json = json.load(f)

        s1.extend(s1_json)
        s2.extend(s2_json)

    s1 = [s["translations"][0]["text"] for s in s1]
    s2 = [s["translations"][0]["text"] for s in s2]

    assert len(s1) == len(s2)

    return s1, s2


train = pd.read_csv(
    "stsbenchmark/sts-train.csv",
    sep="\t",
    usecols=[4, 5, 6],
    header=None,
    quoting=QUOTE_NONE,
)


dev = pd.read_csv(
    "stsbenchmark/sts-dev.csv",
    sep="\t",
    usecols=[4, 5, 6],
    header=None,
    quoting=QUOTE_NONE,
)


test = pd.read_csv(
    "stsbenchmark/sts-test.csv",
    sep="\t",
    usecols=[4, 5, 6],
    header=None,
    quoting=QUOTE_NONE,
)

char_sum = (
    train[5].str.len().sum()
    + train[6].str.len().sum()
    + dev[5].str.len().sum()
    + dev[6].str.len().sum()
    + test[5].str.len().sum()
    + test[6].str.len().sum()
)

# get_translations(train, "train")
# get_translations(train, "train")
# get_translations(train, "train")

s1_train, s2_train = parse_json_files("train")
assert len(s1_train) == len(train)
train["sentence1_tr"] = s1_train
train["sentence2_tr"] = s2_train
train.columns = [
    "score",
    "sentence1_en",
    "sentence2_en",
    "sentence1_tr",
    "sentence2_tr",
]
train.to_csv("sts-tr/sts-train-tr.csv", index=False)

s1_test, s2_test = parse_json_files("test")
assert len(s1_test) == len(test)
test["sentence1_tr"] = s1_test
test["sentence2_tr"] = s2_test
test.columns = [
    "score",
    "sentence1_en",
    "sentence2_en",
    "sentence1_tr",
    "sentence2_tr",
]
test.to_csv("sts-tr/sts-test-tr.csv", index=False)

s1_dev, s2_dev = parse_json_files("dev")
assert len(s1_dev) == len(dev)
dev["sentence1_tr"] = s1_dev
dev["sentence2_tr"] = s2_dev
dev.columns = [
    "score",
    "sentence1_en",
    "sentence2_en",
    "sentence1_tr",
    "sentence2_tr",
]
dev.to_csv("sts-tr/sts-dev-tr.csv", index=False)
