import yaml 

class StateManager:
    def __init__(self):
        self.active = False
        self.settings = {}
        self.permissions = {}

    def load_settings(self):
        with open("config/settings.yaml") as f:
            self.settings = yaml.safe_load(f)

    def load_permissions(self):
        with open("config/permissions.yaml") as f:
            self.permissions = yaml.safe_load(f)

    def set_active(self, value):
        self.active = value
