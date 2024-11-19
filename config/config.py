import os

class Config:
    chrome_path: str = '/bin/chromium'
    log_level: str = "INFO"
    tests: str = "False"
    tgbot_pass: str = "123"
    hh_login: str = "test@example.com"

    @classmethod
    def load_from_env(cls):
        for key in cls.__annotations__:
            env_value = os.getenv(key.upper())
            if env_value is not None:
                current_value = getattr(cls, key)
                if isinstance(current_value, int):
                    setattr(cls, key, int(env_value))
                elif isinstance(current_value, list):
                    setattr(cls, key, env_value.split(","))
                else:
                    setattr(cls, key, env_value)

Config.load_from_env()

if __name__ == "__main__":
    raise RuntimeError("This module should be run only via main.py")
