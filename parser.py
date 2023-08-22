# This script helps us to parse json and yaml file

import json
import yaml


#Json parsing section

json_file = "services.json"
with open(json_file,"r", encoding="utf-8") as openj:
    parsedjson = json.loads(openj.read())

jsonparsed = parsedjson["services"]


# prints service name of every cloud service provider in services.json file
for printer in 'aws','azure', 'gcp' :
    print(printer + ' : '+ (jsonparsed[printer]['name']))


#Yaml parsing section
yaml_file = "services.yaml"
with open(yaml_file,"r", encoding="utf-8") as openy:
    parsedyaml = yaml.safe_load(openy.read())

yamlparsed = parsedyaml["services"]

print(parsedyaml)

# prints service name of every cloud service provider in services.yaml file
for printer in 'aws','azure', 'gcp' :
    print(printer + ' : '+ (yamlparsed[printer]['name']))
