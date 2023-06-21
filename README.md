# Parallel Artificial Membrane Permeability Assay 5

Parallel Artificial Membrane Permeability is an in vitro surrogate to determine the permeability of drugs across cellular membranes. PAMPA at pH 5 was experimentally determined in a dataset of 5,473 unique compounds by the NIH-NCATS. 50% of the dataset was used to train a classifier (SVM) to predict the permeability of new compounds, and validated on the remaining 50% of the data, rendering an AUC = 0.88. The Peff was converted to logarithmic, log Peff value lower than 2.0 were considered to have low to moderate permeability, and those with a value higher than 2.5 were considered as high-permeability compounds. Compounds with a value between 2.0 and 2.5 were omitted from the dataset. A subset of the data is available at PubChem (AID 1645871)

## Identifiers

* EOS model ID: `eos81ew`
* Slug: `ncats-pampa5`

## Characteristics

* Input: `Compound`
* Input Shape: `Single`
* Task: `Classification`
* Output: `Probability`
* Output Type: `Float`
* Output Shape: `Single`
* Interpretation: Probability of a compound being poorly permeable (logPeff < 1)

## References

* [Publication](https://www.sciencedirect.com/science/article/pii/S0968089621005964)
* [Source Code](https://github.com/ncats/ncats-adme)
* Ersilia contributor: [pauline-banye](https://github.com/pauline-banye)

## Ersilia model URLs
* [GitHub](https://github.com/ersilia-os/eos81ew)
* [AWS S3](https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos81ew.zip)
* [DockerHub](https://hub.docker.com/r/ersiliaos/eos81ew) (AMD64)

## Citation

If you use this model, please cite the [original authors](https://www.sciencedirect.com/science/article/pii/S0968089621005964) of the model and the [Ersilia Model Hub](https://github.com/ersilia-os/ersilia/blob/master/CITATION.cff).

## License

This package is licensed under a GPL-3.0 license. The model contained within this package is licensed under a None license.

Notice: Ersilia grants access to these models 'as is' provided by the original authors, please refer to the original code repository and/or publication if you use the model in your research.

## About Us

The [Ersilia Open Source Initiative](https://ersilia.io) is a Non Profit Organization ([1192266](https://register-of-charities.charitycommission.gov.uk/charity-search/-/charity-details/5170657/full-print)) with the mission is to equip labs, universities and clinics in LMIC with AI/ML tools for infectious disease research.

[Help us](https://www.ersilia.io/donate) achieve our mission!