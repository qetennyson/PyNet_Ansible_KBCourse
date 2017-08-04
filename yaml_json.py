import json
import yaml
from pprint import pprint as pp

my_list = range(8)
print my_list
my_list.append('bingbong')
my_list.append('hello')
my_list.append({})

print my_list[-1]

my_list[-1]['ip_addr'] = '10.1.1.1'
my_list[-1]['attribs'] = range(3)

print yaml.dump(my_list)
print yaml.dump(my_list, default_flow_style=False)

print json.dumps(my_list)

json_list = json.dumps(my_list)
yaml_list = yaml.dump(my_list, default_flow_style=False)

pp(json_list)
pp(yaml_list)