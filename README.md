# Pushbot


# General information

Бот по расписанию отправляет ругательное сообщение дежурному и менеджеру в чате, куда добавлен.


# System requirements

- Python 3.7

## Repository structure

```tree
settings/                <= Project settings
    local.example.py     <= Local settings
tests/                   <= Tests
```

## Quick start

Copy settings:

```bash
cp settings/local.example.py settings/local.py
```
Install virtual environment package for python, for example python3-venv:

```bash
sudo apt install -y python3-venv
```

Create virtual environment in the project directory:

```bash
python3 -m venv .env
```

Activate your virtual environment:

```bash
source .env/bin/activate
```

Install requirements:

```bash
pip install -r requirements.txt
```
