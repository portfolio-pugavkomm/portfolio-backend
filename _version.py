from pathlib import Path

import toml

version = "unknown"
pyproject_toml_file = Path(__file__).parent / "pyproject.toml"
if pyproject_toml_file.exists() and pyproject_toml_file.is_file():
    data = toml.load(pyproject_toml_file)
    if "project" in data and "version" in data["project"]:
        version = data["project"]["version"]
    elif "tool" in data and "poetry" in data["tool"] and "version" in data["tool"]["poetry"]:
        version = data["tool"]["poetry"]["version"]
