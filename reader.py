import os
import json

class Reader():
    def __init__(self):
        print("creating loader class")

    def read_config_to_json(self):
        filename = os.path.join('config.json')
        try:
            with open(filename, mode='r') as f:
                return json.loads(f.read())
        except FileNotFoundError:
            return {}

    def parse_envs_from_json(self, config):
        for env in config["EnvVar"]:
            if env not in os.environ: 
                os.environ[env] = config["EnvVar"][env]
                # print("adding " + env + ":[" + config["EnvVar"][env] + "] to env")

    def set_up_env(self): 
        configs = self.read_config_to_json()

        for app in configs["App Configs"]:
            self.parse_envs_from_json(app)

        self.parse_envs_from_json(configs)