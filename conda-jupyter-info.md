# Conda and Jupyter Command Line Setup

De nodige software stack en hoe die te verkrijgen wordt in detail uitlegd elders in de repo, cf. [./docs/prerequisites.pdf](./docs/prerequisites.pdf)

Dit document legt uit hoe je de `conda` setup kan verkrijgen via je terminal. Deze werkwijze is enkel getest op linux, en komt **zonder garanties**. Gezien dit voor mensen die reeds ervaring met `conda` hebben een meerwaarde kan betekenen, wordt het bijgevoegd.

## Conda Environment

The [dependencies.yaml](dependencies.yaml) file lists all that is needed. To create an environment out of this, do;

```bash
conda env create -f dependencies.yaml -n db-taak
```

## Jupyter 

By default, a `conda` environment may or may not pop up as an available _"kernel"_ in your `Jupyter` environment. 
Whether it does or not depends on OS, conda version and on the configuration of your on machine.
For guaranteed success (i.e. _expose_ this kernel manually), run the following command.

```bash
conda activate db-taak
python -m ipykernel install --user --name db-taak
```

…and, for as far the python part of the setup is concerned, you are done.
