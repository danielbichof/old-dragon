# dragon

[![PyPI - Version](https://img.shields.io/pypi/v/dragon.svg)](https://pypi.org/project/dragon)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/dragon.svg)](https://pypi.org/project/dragon)

---

## Table of Contents

- [Installation](#installation)
- [License](#license)

## Como rodar o projeto localmente

### Pré-requisitos

- Python 3.8 ou superior

### 1. Crie e ative um ambiente virtual (venv)

```bash
python3 -m venv .venv
# Ative o venv:
# No Linux/macOS (bash/zsh):
source .venv/bin/activate
# No fish shell:
source .venv/bin/activate.fish
# No Windows (cmd):
.venv\Scripts\activate.bat
```

### 2. Instale o Hatch

```bash
pip install hatch
```

### 3. Instale as dependências do projeto

```bash
hatch env create
```

### 4. Rode o projeto

```bash
hatch run dragon
```

#### Testes e checagem de tipos

- Para rodar os testes:

```bash
hatch run test
```

- Para checar tipos (mypy):

```bash
hatch run types:check
```

## License

`dragon` is distributed under the terms of the [MIT](https://spdx.org/licenses/MIT.html) license.
