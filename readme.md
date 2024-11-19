# hh_responses_py

This project sends requests to employers on the hh.ru website.

### Initial Setup

1. **Clone the repository**: Clone this repository using `git clone`.
2. **Create Virtual Env**: Create a Python Virtual Environment `venv` to download the required dependencies and libraries.
3. **Download Dependencies**: Download the required dependencies into the Virtual Environment `venv` using `pip`.

```shell
git clone https://github.com/grisha765/hh_responses_py.git
cd hh_responses_py
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
```

## Usage

### Deploy

- Run project:
    ```bash
    .venv/bin/python main.py
    ```

- Other working env's:
    ```env
    LOG_LEVEL='DEBUG'
    CHROME_PATH='/path/to/chromium'
    HH_LOGIN='test@example.com'
    TESTS='True'
    ```

- Example:
    ```bash
    LOG_LEVEL="DEBUG" .venv/bin/python main.py
    ```

- Run tests:
    ```bash
    LOG_LEVEL="DEBUG" TESTS='True' .venv/bin/python main.py
    ```

## Implemented

- Entering login and password on the hh.ru authorization page.
