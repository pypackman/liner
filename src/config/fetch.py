import toml, os
def loadConfig() -> dict: return toml.loads(open(os.path.join(os.path.dirname(__file__),'toml/config.toml')).read())