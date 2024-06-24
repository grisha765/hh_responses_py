import os

class Config:
    chrome_path: str = '/bin/chromium'
    log_level: str = "INFO"
    tests: str = "False"
    tgbot_pass: str = "123"
    hh_login: str = "test@example.com"
    hh_passw: str = "password123"

    @classmethod
    def load_from_env(cls):
        for key, value in cls.__annotations__.items():
            env_value = os.getenv(key.upper())
            if env_value is not None:
                if isinstance(value, int):
                    setattr(cls, key, int(env_value))
                else:
                    setattr(cls, key, env_value)

Config.load_from_env()

if __name__ == "__main__":
    raise RuntimeError("This module should be run only via main.py")
