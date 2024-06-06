import os
import setuptools


def find_package_files(directory, remove_root):
    """
    Walk the filesystem from the specifed directory to get a recursive list of files. Remove the start of each
    if it matches the specified removal string to leave paths relative to their containing package

    :param directory: Path to the folder to walk
    :param remove_root: Remove this if it appears at the start of a file path
    :return: A list of file paths relative to a package folder
    """
    file_paths = []
    for (path, directories, filenames) in os.walk(directory):
        # Remove the start of the path to leave the path relative to the package folder
        if path.startswith(remove_root):
            path = path[len(remove_root):]

        for filename in filenames:
            file_paths.append(os.path.join(path, filename))

    return file_paths


# The package data for the web package includes the whole directory tree for the static files plus
# the Flask view templates
api_package_data = find_package_files("src/api/", "src/api/")


setuptools.setup(
    name="subnet_calculator",
    version="1.2.0",
    description="Subnet Calculator",
    packages=setuptools.find_packages("src"),
    include_package_data=True,
    package_dir={"": "src"},
    package_data={
        "api": api_package_data
    }
)
