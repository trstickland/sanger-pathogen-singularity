# sanger-pathogen-singularity
Experimentation with the building of singularity repository for sanger-pathogene
[![License: GPL v3](https://img.shields.io/badge/License-GPL%20v3-brightgreen.svg)](https://github.com/sanger-pathogens/Bio-ENA-DataSubmission/blob/master/GPL-LICENCE)    

## Introduction
Repository collecting the experimentation work on singularity image building

## Current state
The focus is to build in an automated fashion an image for our most used software:
   * samtools 1.9
   * bcftools 1.9
   * bedtools 2.27.1
   * bwa 0.7.17
   * fastqc 0.11.8
   * picard 2.18.27
   * vcftools 0.1.16
   * gatk 3.8

The current implementation leverages conda as much as possible and uses Jinja2 templates to generate the singularity recipes

## Run under vagrant
The below command will build a box with all dependencies required to build images.  It will then build images for each of the required software
```
vagrant up
```

## License
sanger-pathogen-singularity is free software, licensed under [GPLv3](https://github.com/seretol/sanger-pathogen-singularity/blob/master/LICENSE).

