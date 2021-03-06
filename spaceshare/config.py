import os
import yaml

# The purpose of this file is to load the yaml file in memory and pass it
# around to other module around.

config_path = os.environ.get('some shell variable if you want')
if config_path is None:
    config = yaml.load(open(os.path.dirname(__file__) + '/../settings.yaml'))
else:
    config = yaml.load(open(config_path))
