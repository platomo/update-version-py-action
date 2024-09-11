# 🛠️ Update Version GitHub Action

## 📄 Beschreibung

Die **Update Version** Action aktualisiert die Versionsnummer in einem Python-Paket. Sie wird verwendet, um die `__version__`-Variable in der `version.py` Datei eines Python-Projekts entweder mit einer benutzerdefinierten Versionsnummer oder mit einer automatisch generierten "nightly"-Version zu aktualisieren.

## ⚙️ Inputs

| Parameter         | Beschreibung                                                                                    | Erforderlich | Standardwert                |
| ----------------- | ----------------------------------------------------------------------------------------------- | ------------ | --------------------------- |
| `package-version` | Die Versionsnummer, die gesetzt werden soll. Standardmäßig wird eine nightly-Version generiert. | Nein         | `nightly`                   |
| `package-path`    | Der Pfad zum Paket, das die `version.py` Datei enthält.                                         | Ja           | `.` (aktuelles Verzeichnis) |
| `text-pattern`    | Das Muster des Textes, das nach der Versionsnummer durchsucht wird (z.B. `__version__`).        | Nein         | `__version__`               |
| `file-name`       | Der Name der Datei, in der die Versionsnummer geändert wird.                                    | Nein         | `version.py`                |

## 🚀 Funktionsweise

Diese Action sucht in der angegebenen Datei (standardmäßig `version.py`) nach einer Zeile, die dem angegebenen Textmuster (standardmäßig `__version__`) entspricht, und ersetzt die vorhandene Versionsnummer entweder durch eine benutzerdefinierte oder eine automatisch generierte nightly-Version.

- Wenn `package-version` auf `nightly` gesetzt ist, wird eine neue nightly-Version mit dem aktuellen Datum und der Uhrzeit im Format `nightly-YYYYMMDD-HHMMSS` erstellt und gespeichert.
- Wenn eine spezifische Versionsnummer angegeben wird, wird diese anstelle der nightly-Version verwendet.

## 📦 Beispiel für die Verwendung

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
        uses: ./ # Verweis auf diese Action
        with:
          package-version: "1.0.0"
          package-path: "my_package"
          file-name: "version.py"
```

Dieses Beispiel setzt die Version des Python-Pakets in der Datei my_package/version.py auf 1.0.0. Wenn keine Version angegeben wird, wird eine nightly-Version erzeugt.

## Lizenz
