import argparse
from datetime import datetime
from pathlib import Path


def update_version(version: str, variable: str, file_path: str, file_name: str):
    # File path
    file = Path(file_path, file_name)

    if not file.is_file():
        raise (FileNotFoundError(f"File {file} does not exist. Cannot update version."))

    # Determine the replacement based on the package version
    if version == "nightly":
        # Get current date and time
        dt = datetime.now().strftime("%Y%m%d-%H%M%S")
        new_version = f"nightly-{dt}"
    else:
        new_version = version

    # Read the file
    with open(file, "r") as f:
        content = f.read()

    # Update the version in the content
    current_version = get_current_version(content, variable)
    print(f"Current version: {current_version}")
    updated_content = content.replace(
        f'{variable} = "{current_version}"', f'{variable} = "{new_version}"'
    )
    print(updated_content)
    updated_content = updated_content.replace(
        f"{variable} = '{current_version}'", f'{variable} = "{new_version}"'
    )
    print(updated_content)

    # Write the updated content back to the file
    with open(file, "w") as f:
        f.write(updated_content)
        print(
            f"Successfully updated {variable} "
            f"from {current_version} to {new_version} "
            f"in {file_name}."
        )


def get_current_version(content, variable_name):
    """Extract the current version from the file content."""
    for line in content.splitlines():
        if line.startswith(f"{variable_name} ="):
            return line.split("=")[1].strip().strip('"')
    return None


def main():
    # Set up argument parsing
    parser = argparse.ArgumentParser(
        description="Update version variable value in a version file."
    )
    parser.add_argument(
        "--version",
        required=True,
        help="Version to set (e.g., 'nightly' or specific version).",
    )
    parser.add_argument(
        "--variable", required=True, help="Variable name to update in the file."
    )
    parser.add_argument(
        "--file-path", required=True, help="Path to the package directory."
    )
    parser.add_argument(
        "--file-name", required=True, help="Name of the file to update."
    )

    args = parser.parse_args()

    update_version(
        version=args.version,
        variable=args.variable,
        file_path=args.file_path,
        file_name=args.file_name,
    )


if __name__ == "__main__":
    main()
