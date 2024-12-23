---
tags:
- text-classification
- roberta
- adapterhub:sentiment/sst-2
- adapter-transformers
language:
- en
---

# Adapter `AdapterHub/roberta-base-pf-sst2` for roberta-base

An [adapter](https://adapterhub.ml) for the `roberta-base` model that was trained on the [sentiment/sst-2](https://adapterhub.ml/explore/sentiment/sst-2/) dataset and includes a prediction head for classification.

This adapter was created for usage with the **[adapter-transformers](https://github.com/Adapter-Hub/adapter-transformers)** library.

## Usage

First, install `adapter-transformers`:

```
pip install -U adapter-transformers
```
_Note: adapter-transformers is a fork of transformers that acts as a drop-in replacement with adapter support. [More](https://docs.adapterhub.ml/installation.html)_

Now, the adapter can be loaded and activated like this:

```python
from transformers import AutoModelWithHeads

model = AutoModelWithHeads.from_pretrained("roberta-base")
adapter_name = model.load_adapter("AdapterHub/roberta-base-pf-sst2", source="hf")
model.active_adapters = adapter_name
```

## Architecture & Training

The training code for this adapter is available at https://github.com/adapter-hub/efficient-task-transfer.
In particular, training configurations for all tasks can be found [here](https://github.com/adapter-hub/efficient-task-transfer/tree/master/run_configs).


## Evaluation results

Refer to [the paper](https://arxiv.org/pdf/2104.08247) for more information on results.

## Citation

If you use this adapter, please cite our paper ["What to Pre-Train on? Efficient Intermediate Task Selection"](https://arxiv.org/pdf/2104.08247):

```bibtex
@inproceedings{poth-etal-2021-pre,
    title = "{W}hat to Pre-Train on? {E}fficient Intermediate Task Selection",
    author = {Poth, Clifton  and
      Pfeiffer, Jonas  and
      R{"u}ckl{'e}, Andreas  and
      Gurevych, Iryna},
    booktitle = "Proceedings of the 2021 Conference on Empirical Methods in Natural Language Processing",
    month = nov,
    year = "2021",
    address = "Online and Punta Cana, Dominican Republic",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2021.emnlp-main.827",
    pages = "10585--10605",
}
```