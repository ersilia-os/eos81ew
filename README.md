# **Parallel Artificial Membrane Permeability Assay (PAMPA) 5**

## **Model identifiers**
- Slug: parallel-artificial-membrane-permeability-assay-5
- Ersilia ID: eos81ew
- Tags: ADME
#
## **Model description**
<p align="justify">
Cell membrane permeability is important for determining oral absorption of drug molecules. Parallel Artificial Membrane Permeability Assay (PAMPA) 5 is used to measure the permeability of a substance across an artificial membrane. It is a cheap alternative to cellular models for early ADME screening.
</p>
<p align="justify">
A drug needs to have the ability to cross the cell membranes to reach the target site and achieve the desired concentration to produce a desirable pharmacological response. By measuring how permeable substances are across the membrane, PAMPA can estimate how easily a drug can penetrate cell membranes in the body and enter the bloodstream.
Drugs that have poor permeability have a lower drug absorption rate, which can render the drug ineffective. Poor permeability of drugs also leads to other issues, such as challenges with toxicity and interactions with other drugs.
</p>
<p align="justify">
This data was provided by the National Center for Advancing Translational Sciences (NCATS). A probability of below 0.5 is considered highly permeable. Probability of 0.5 or greater is considered low permeability. 
</p>

- Input: SMILES
- Output: SMILES
#
## **Source code**

Cite the source publication
[Using in vitro ADME data for lead compound selection: An emphasis on PAMPA pH 5 permeability and oral bioavailability](https://www.sciencedirect.com/science/article/pii/S0968089621005964)

- Code: [NCATS-ADME](https://github.com/ncats/ncats-adme.git)
- Checkpoints: include the link to the checkpoints used if model is a pretrained model
#
## **License**
GNU General Public License v3.0.

## **History**
- The model was incorporated into Ersilia on the 22th of January, 2023.
- Modifications to the original code.
    1. Removal of Flask functionalities and dependencies.
    2. Striping unused functions from the original code.

- To run the model, follow these [steps](model/README.md).

The [Ersilia Open Source Initiative](https://ersilia.io) is a Non Profit Organization ([1192266](https://register-of-charities.charitycommission.gov.uk/charity-search/-/charity-details/5170657/full-print)) with the mission is to equip labs, universities and clinics in LMIC with AI/ML tools for infectious disease research.

[Help us](https://www.ersilia.io/donate) achieve our mission or [volunteer](https://www.ersilia.io/volunteer) with us!
