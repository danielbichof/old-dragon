# dragon

[![PyPI - Version](https://img.shields.io/pypi/v/dragon.svg)](https://pypi.org/project/dragon)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/dragon.svg)](https://pypi.org/project/dragon)

---

## Table of Contents

- [Como rodar (Poetry)](#como-rodar-o-projeto-localmente-poetry)
- [License](#license)

## Como rodar o projeto localmente (Poetry)

### Pré-requisitos

- Python 3.8 ou superior
- Poetry instalado

### 1. Instale o Poetry (se ainda não tiver)

```fish
python3 -m pip install --user poetry
```

### 2. Instale as dependências

```fish
poetry install
```

### 3. Executar a CLI

O entrypoint `dragon` está mapeado para `dragon.cli:app`. Para abrir o gerador interativo:

```fish
poetry run dragon gerar
```

### 4. Rodar os testes

```fish
poetry run pytest -q
```

### 5. Checagem de tipos (mypy)

```fish
poetry run mypy
```

## License

`dragon` is distributed under the terms of the [MIT](https://spdx.org/licenses/MIT.html) license.
