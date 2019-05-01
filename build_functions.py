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
template = env.get_template('function.template')
if len(sys.argv) >= 3:
    softwares = filter(lambda x: x['name'] in sys.argv[1:], softwares);

for software in softwares:
    image = software['name'] + '-' + software['version'] + '.simg'
    for function in software['functions']:
        data = function.split("=")
        (name, executable) = (data[0], data[1]) if len(data) == 2 else (data[0], data[0])
        print(template.render(function=name, executable=executable, image=image))
