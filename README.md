# whale-client
The SDK for Whale

## Install Poetry

We use [Poetry](https://python-poetry.org/) for dependency management.

```bash
# Install Poetry
curl -sSL https://install.python-poetry.org | python3 -
```

Or follow installation instructions from [Poetry website](https://python-poetry.org/docs/#installation).

## Setup Virtual Environment

It is recommended to use Python virtual environment, so you don't pollute your system Python environment.

```bash
# Install dependencies
poetry install
```

```bash
# Update/upgrade dependencies
poetry update
```

```bash
# Activate Python virtual environment
poetry shell
```

## Environment Variables
Copy an existing environment template file and fill in all the necessary values:
```bash
# Create .env file (by copying from .env.example)
cp .env.example .env
```

### Check style

Run the following command at the root of the repository
`black .`
