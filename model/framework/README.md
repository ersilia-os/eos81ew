# **MODEL EOS74BO**

This repository contains the code for the QSAR models for Kinetic Aqueous Solubility endpoints. To use the application locally, you can either use [Git](https://git-scm.com/) to clone the respository, or you can simply download a ZIP file (by clicking the green "Code" button on the top right corner) and then unzip it. The next steps are described below.

`https://github.com/ersilia-os/eos8ykt.git`

#
## **Installing required software**

1. Install [anaconda or miniconda](https://docs.conda.io/projects/continuumio-conda/en/latest/user-guide/install/index.html#)
2. Install [Docker](https://www.docker.com/products/)

Python is also required but it is included with either installation of conda or miniconda.

#
## **Steps to run the application**
Either docker or conda can be used to run the application. You only have complete the steps once.


### **With Docker**
1. Build the Docker image. You need to be in the same folder as the Dockerfile to run this command.
    ```
    docker build -t '<name of env>:Dockerfile' .
    ```
2. Run the docker image
    ```
    docker run <name of env>
    ```
3. Change directory to model/checkpoints
4. Type `python main.py ../input.csv ../<outout-file>.csv` and hit Enter
Note: Ensure that the Docker service is running.

#
### **With conda**

1. Open your Anaconda terminal
2. Create environment
    ```
    conda env update --prefix ./<name-of-env> -f environment.yml
    ```
    - Wait for the environment to be created
3. Type `conda activate ./<name-of-env>` and hit Enter
4. Change directory to model/checkpoints
5. Type `python main.py <input-file>.csv <outout-file>.csv` and hit Enter
6. To close the application, hit `Ctrl + c` or `Cmd + c` in the Terminal and then type `conda deactivate` and hit Enter to close the conda environment
