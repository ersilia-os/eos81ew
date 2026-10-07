# Parallel Artificial Membrane Permeability Assay 5

Predicts passive permeability in the parallel artificial membrane assay at pH 5, the acidic condition approximating the intestinal surface microclimate rather than bulk plasma pH. Williams and colleagues at NCATS measured about 6,500 samples in house, curated them to 5,227 unique compounds and split low from moderate permeability at 10x10-6 cm/s, with a graph convolutional network reaching an external AUC of 0.84. Being cell-free, the assay says nothing about transporter-mediated uptake or efflux.

This model was incorporated on 2023-01-29.Last packaged on 2026-07-06.

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
- **Interpretation:** Probability of poor passive permeability at pH 5, meaning effective permeability under 10x10-6 cm/s.

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
- **Image Size (Mb):** `2609.51`

**Computational Performance (seconds):**
- 10 inputs: `25.93`
- 100 inputs: `15.89`
- 10000 inputs: `96.43`

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
