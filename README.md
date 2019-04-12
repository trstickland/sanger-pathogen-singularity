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
These are stored in sanger.yml   

The current implementation leverages conda as much as possible and uses Jinja2 templates to generate the singularity recipes   

A secondary focus is to build a set of images required by our first farm4 user.  These are stored in gerry.yml
## Building the images
### Requirements
The following must be available:
   * vagrant
   * vagrant vbguest plugin: ``` vagrant plugin install vagrant-vbguest ```

### Running under vagrant
The below command will build a box with all dependencies required to build images.  It will then build images for each of the required software
```
vagrant up
vagrant ssh
cd sanger-pathogen-singularity
./build_images.py <definition file.yml> [software to build]
```

Examples:   
To build all images for gerry
```
./build_images.py gerry.yml
```
To build beast2 and samtools for gerry
```
./build_images.py gerry.yml beast2 samtools
```   

## License
sanger-pathogen-singularity is free software, licensed under [GPLv3](https://github.com/seretol/sanger-pathogen-singularity/blob/master/LICENSE).

