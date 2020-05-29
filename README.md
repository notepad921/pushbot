# Pushbot


# General information

Бот отправляет ругательное сообщение и информационную ссылку дежурному и менеджеру в чате, куда добавлен.


# System requirements

- Python 3.7

## Repository structure

```tree
settings/                <= Project settings
    local.example.py     <= Local settings
    dictionary.py        <= Datasets for generation
src/                     <= The most important things are here
tests/                   <= Tests
```

## Quick start

1. Copy settings:

    ```bash
    cp settings/local.example.py settings/local.py
    ```
2. Fill local.py.

3. Install virtual environment package for python, for example python3-venv:

    ```bash
    sudo apt install -y python3-venv
    ```

4. Create virtual environment in the project directory:

    ```bash
    python3 -m venv .env
    ```

5. Activate your virtual environment:

    ```bash
    source .env/bin/activate
    ```

6. Install requirements:

    ```bash
    pip install -r requirements.txt
    ```
   
7. Configure launching of the main.py script at the right time (for example, via cron).
