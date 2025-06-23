# entity_search

Assignement for the course "Information Retrieval" at UFMG.

### Francisco Teixeira Rocha Aragão - 2021031726
### Lorenzo Carneiro Magalhães - 2021031505

# How to run

The corpus data should be placed inside `data/ir-20251-rc` so the code can run automatically. The paths can be changed if needed.

- First install the requirements with conda using the file `ir25-env.yaml`:
```bash
conda env create -f ir25-env.yaml
conda activate ir25
```

- It could be necessary to install Java (if not installed) so the `pyserini` library can run:
```bash
# the 17 version was used in the development
sudo apt update
sudo apt install openjdk-17-jdk
``` 

Then just run each cell of the notebook `main.ipynb` in order.

Some cells can take a while to run because the use of language models, but is just waiting for the results.

The first submission have the data loaded entirely in memory, so it can not work in all machines.

The next submissions creates new folders to handle the index data, but it is performed automatically.