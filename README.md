# Parallel Artificial Membrane Permeability Assay 5

Parallel Artificial Membrane Permeability (PAMPA) is an in vitro surrogate for drug cellular permeability. NIH-NCATS evaluated 5,473 unique compounds at pH 5. Peff values were converted to log Peff: <2.0 represents low/moderate permeability, >2.5 represents high permeability, and 2.0–2.5 were omitted. An SVM classifier trained on 50% of the dataset and validated on the remaining 50% achieved an AUC = 0.88. A subset of the data is available at PubChem (AID 1645871).

This model was incorporated on 2023-01-29.Last packaged on 2025-10-16.

## Information
### Identifiers
- **Ersilia Identifier:** `eos81ew`
- **Slug:** `ncats-pampa5`

### Domain
- **Task:** `Annotation`
- **Subtask:** `Property calculation or prediction`
- **Biomedical Area:** `ADMET`
- **Target Organism:** `Any`
- **Tags:** `ADME`, `Permeability`, `LogP`

### Input
- **Input:** `Compound`
- **Input Dimension:** `1`

### Output
- **Output Dimension:** `1`
- **Output Consistency:** `Fixed`
- **Interpretation:** Probability of a compound being poorly permeable (logPeff < 1)

Below are the **Output Columns** of the model:
| Name | Type | Direction | Description |
|------|------|-----------|-------------|
| pampa5_proba1 | float | high | Probability of the compound not being permeable in a PAMPA assay at pH=5 (logPeff<1) |


### Source and Deployment
- **Source:** `Local`
- **Source Type:** `External`
- **DockerHub**: [https://hub.docker.com/r/ersiliaos/eos81ew](https://hub.docker.com/r/ersiliaos/eos81ew)
- **Docker Architecture:** `AMD64`, `ARM64`
- **S3 Storage**: [https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos81ew.zip](https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos81ew.zip)

### Resource Consumption
- **Model Size (Mb):** `86`
- **Environment Size (Mb):** `2443`
- **Image Size (Mb):** `2592.77`

**Computational Performance (seconds):**
- 10 inputs: `28.8`
- 100 inputs: `18.7`
- 10000 inputs: `114.04`

### References
- **Source Code**: [https://github.com/ncats/ncats-adme](https://github.com/ncats/ncats-adme)
- **Publication**: [https://doi.org/10.1016/j.bmc.2021.116588](https://doi.org/10.1016/j.bmc.2021.116588)
- **Publication Type:** `Peer reviewed`
- **Publication Year:** `2022`
- **Ersilia Contributor:** [pauline-banye](https://github.com/pauline-banye)

### License
This package is licensed under a [GPL-3.0](https://github.com/ersilia-os/ersilia/blob/master/LICENSE) license. The model contained within this package is licensed under a [None](LICENSE) license.

**Notice**: Ersilia grants access to models _as is_, directly from the original authors, please refer to the original code repository and/or publication if you use the model in your research.


## Use
To use this model locally, you need to have the [Ersilia CLI](https://github.com/ersilia-os/ersilia) installed.
The model can be **fetched** using the following command:
```bash
# fetch model from the Ersilia Model Hub
ersilia fetch eos81ew
```
Then, you can **serve**, **run** and **close** the model as follows:
```bash
# serve the model
ersilia serve eos81ew
# generate an example file
ersilia example -n 3 -f my_input.csv
# run the model
ersilia run -i my_input.csv -o my_output.csv
# close the model
ersilia close
```

## About Ersilia
The [Ersilia Open Source Initiative](https://ersilia.io) is a tech non-profit organization fueling sustainable research in the Global South.
Please [cite](https://github.com/ersilia-os/ersilia/blob/master/CITATION.cff) the Ersilia Model Hub if you've found this model to be useful. Always [let us know](https://github.com/ersilia-os/ersilia/issues) if you experience any issues while trying to run it.
If you want to contribute to our mission, consider [donating](https://www.ersilia.io/donate) to Ersilia!
