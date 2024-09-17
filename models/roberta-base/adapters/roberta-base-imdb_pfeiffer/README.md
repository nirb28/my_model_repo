---
tags:
- adapter-transformers
- roberta
- adapterhub:sentiment/imdb
datasets:
- imdb
license: "apache-2.0"
---

# Adapter `roberta-base-imdb_pfeiffer` for roberta-base

Pfeiffer Adapter trained on the IMDb dataset.


**This adapter was created for usage with the [Adapters](https://github.com/Adapter-Hub/adapters) library.**

## Usage

First, install `adapters`:

```
pip install -U adapters
```

Now, the adapter can be loaded and activated like this:

```python
from adapters import AutoAdapterModel

model = AutoAdapterModel.from_pretrained("roberta-base")
adapter_name = model.load_adapter("AdapterHub/roberta-base-imdb_pfeiffer")
model.set_active_adapters(adapter_name)
```

## Architecture & Training

- Adapter architecture: pfeiffer
- Prediction head: None
- Dataset: [IMDb](http://ai.stanford.edu/~amaas/data/sentiment/)

## Author Information

- Author name(s): Jonas Pfeiffer
- Author email: jonas@pfeiffer.ai
- Author links: [Website](https://pfeiffer.ai), [GitHub](https://github.com/JoPfeiff), [Twitter](https://twitter.com/@PfeiffJo)



## Citation

```bibtex
@article{Pfeiffer2020AdapterFusion,
author = {Pfeiffer, Jonas and Kamath, Aishwarya and R{\"{u}}ckl{\'{e}}, Andreas and Cho, Kyunghyun and Gurevych, Iryna},
journal = {arXiv preprint},
title = {{AdapterFusion}:  Non-Destructive Task Composition for Transfer Learning},
 url       = {https://arxiv.org/pdf/2005.00247.pdf},
year = {2020}
}

```

*This adapter has been auto-imported from https://github.com/Adapter-Hub/Hub/blob/master/adapters/ukp/roberta-base-imdb_pfeiffer.yaml*.