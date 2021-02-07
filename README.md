##
# !!! This project had been put on hold / cancelled in order to focus on the higher priority creation of the [bio reactor prototype system](https://github.com/andreaskuster/igem19-ethz-phage-hw-model). !!!
##

# <img src="igem-ethz-logo.svg" alt="iGEM ETHZ Logo" width="75"/> iGEM ETH Zurich - <img src="igem19-ethz-logo.svg" alt="iGEM 19 ETHZ Logo" width="120"/> Libraries for Personalized Phage Therapy

## Project Description
Antibiotic resistance is one of the biggest threats to global health, food security and development of our society today. Without effective antibiotics, treatment of common infections and minor injuries becomes significantly harder, leading to the necessity of new therapeutic strategies. Phage therapy is an alternative method to treat bacterial infections. However, screening and engineering of phages specific to new targets remains a challenge. In our project, we aim to develop a system that allows for the efficient generation of phage libraries containing tail fiber proteins with novel binding abilities using a three-step approach based on T7 bacteriophage. First, non-conserved regions of the tail fiber protein are randomized. Then, the mutated genome sequences are packaged into phages with the original tail fiber protein in vitro. Lastly, the original host is infected with these hybrid phages, leading to the production of phages with altered tail fibers.

We are currently testing three approaches to generate these libraries.
* Yeast assembly: a plasmid containing the T7 genome is assembled by homologous recombination in yeast and a library of randomized oligos is inserted into variable region of tail fiber protein.
* Recombineering: A randomised sequence present on a plasmid is inserted into the tail fiber gene in vivo by using E. coli's homologous recombination machinery.
* In vitro: The tail fiber variable regions are ligated to the T7 genome in vitro by Gibson assembly. 

# Phage Specificity Prediction Model

## Motivation
...

## Software Design
...

### Structure
<img src="software-structure.svg" alt="Software Structure" width="800"/>

#### Predicion Model
#### Data Sources
* Virus Host Database (www.genome.jp/virushostdb)
* National Center for Biotechnology Information (NCBI) (www.ncbi.nlm.nih.gov)
* ...

#### Connector (Database)
...

## License
This project is published under the GNU General Public License v3.0, see [LICENSE](LICENSE).
