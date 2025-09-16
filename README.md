# dragon

[![PyPI - Version](https://img.shields.io/pypi/v/dragon.svg)](https://pypi.org/project/dragon)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/dragon.svg)](https://pypi.org/project/dragon)

---

## Table of Contents

- [Como rodar o projeto localmente](#como-rodar-o-projeto-localmente)
- [Installation](#installation)
- [License](#license)

## Installation

```console
pip install dragon
```

## Como rodar o projeto localmente

### Pré-requisitos

- Python 3.8 ou superior
- Poetry 1.2+ ([instalação do Poetry](https://python-poetry.org/docs/#installation))

### 1. Clone o repositório e navegue até a pasta

```bash
git clone <repository-url>
cd old-dragon
```

### 2. Instale as dependências do projeto

```bash
poetry install
```

### 3. Rode o projeto

```bash
poetry run dragon
```

#### Testes e checagem de tipos

- Para rodar os testes:

```bash
poetry run pytest
```

- Para checar tipos (mypy):

```bash
poetry run mypy src/dragon tests
```

## License

`dragon` is distributed under the terms of the [MIT](https://spdx.org/licenses/MIT.html) license.
