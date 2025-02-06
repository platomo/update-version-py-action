# 🛠️ GitHub Action: Update Version Variable in Python File

## 📄 Description

This action updates the version number of a Python package by modifying a specific
variable (default: `__version__`) in a Python file (default: `version.py`). If the
version is set to `nightly`, the current date and time will be appended to the version.

## ⚙️ Inputs

| Name        | Description                                                      | Required |        Default         |
|-------------| ---------------------------------------------------------------- |:--------:|:----------------------:|
| `version`   | Version number to set. Defaults to generating a nightly version. |    No    |       `nightly`        |
| `variable`  | The variable to update (e.g., `__version__`).                    |    No    |     `__version__`      |
| `file-path` | Path to the directory containing the `version.py` file.          |    No    |          `.`           |
| `file-name` | Name of the file where the version variable is located.          |    No    |      `version.py`      |

## 🚀 How It Works

The action searches for a line in the specified file (default: `version.py`) that starts
with the `variable =` pattern (default: `__version__ =`). It replaces the current
version number with either a custom version or an automatically generated nightly
version.

- If `version` is set to `nightly`, a version in the format `nightly-YYYYMMDD-HHMMSS`
  will be generated.
- If a specific version is provided, it will replace the existing version.

## 📦 Usage Example

```yaml
name: Update Package Version

on:
  push:
    branches:
      - main

jobs:
  update-version:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout repository
        uses: actions/checkout@v2

      - name: Update Python package version
        uses: platomo/update-version-py-action@v1
        with:
          version: "1.0.0"
          file-path: "my_package"
```

In this example, the **version** variable in my_package/version.py is updated to 1.0.0.

## 🆕 Create a new release

To create a new release of the action, use the GitHub release function and create a new
tag according to semantic version requirements (vX.Y.Z).
The GitHub workflow `major-release-tag.yml` will automatically move the major version
tag to the new release.

## ⚖️ License

GNU GENERAL PUBLIC LICENSE Version 3
