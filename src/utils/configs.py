import configparser


class ConfigManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(ConfigManager, cls).__new__(cls)
            cls._instance._config = configparser.ConfigParser()
            config_file = 'conf/configs.ini'
            cls._instance._config.read(config_file)
        return cls._instance
    
    # Here call open API Key using configManager
    def get_api_key(self):
        return self._config.get("OpenAI", "API_key")