#!/usr/bin/python3

from jinja2 import Environment, FileSystemLoader
import subprocess


env = Environment(
    loader=FileSystemLoader('.')
)
template = env.get_template('conda_template.singularity')

conda_based_installs = [
        ('samtools', '1.9', '', ''),
        ('bcftools', '1.9', '', ''),
        ('bedtools', '2.27.1', '', ''),
        ('bwa', '0.7.17', '', ''),
        ('fastqc', '0.11.8', 
"""
apt-get install -q -y libxtst6
apt-get install -q -y xauth
""", ''),
        ('picard', '2.18.27', """
apt-get clean && apt-get update && apt-get install -y locales
echo en_US.UTF-8 UTF-8 >> /etc/locale.gen
locale-gen en_US.UTF-8
""", ''),
        ('vcftools', '0.1.16', '', ''),
        ('gatk','3.8', '',
"""
wget -q 'https://software.broadinstitute.org/gatk/download/auth?package=GATK-archive&version=3.8-1-0-gf15c1c3ef' -O /tmp/GatkInstall-3.8-1.tar.bz2
/opt/conda/bin/gatk3-register /tmp/GatkInstall-3.8-1.tar.bz2
rm /tmp/GatkInstall-3.8-1.tar.bz2
"""),
        ]
for (software, version, pre_install_instructions, post_install_instruction) in conda_based_installs:
    recipe = software + '-' + version + '.recipe'
    image = software + '-' + version + '.simg'
    with open(recipe, 'w') as recipe_file:
        print(template.render(name=software, version=version, preinstall=pre_install_instructions, postinstall=post_install_instruction), file=recipe_file)
    subprocess.run(["rm", "-f", image]) 
    subprocess.run(["sudo", "singularity", "build", image, recipe])
    print("Built image %s from recipe %s" % (image, recipe))
