#!/usr/bin/python3

from jinja2 import Environment, FileSystemLoader
import subprocess
import yaml
import sys

softwares= []
with open(sys.argv[1], 'r') as stream:
    try:
        softwares= yaml.safe_load(stream)
    except yaml.YAMLError as exc:
        print(exc)

env = Environment(
    loader=FileSystemLoader('.')
)
if len(sys.argv) >= 3:
    softwares = filter(lambda x: x['name'] in sys.argv[1:], softwares);

for software in softwares:
    recipe = software['name'] + '-' + software['version'] + '.recipe'
    image = software['name'] + '-' + software['version'] + '.simg'
    with open(recipe, 'w') as recipe_file:
        template = env.get_template(software['template'])
        print(template.render(software), file=recipe_file)
    subprocess.run(["rm", "-f", image]) 
    subprocess.run(["sudo", "singularity", "build", image, recipe])
    print("Built image %s from recipe %s" % (image, recipe))
