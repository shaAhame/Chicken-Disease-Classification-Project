# purpose: setup source file as a local package

import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

__version__ = "0.0.0"

REPO_NAME = "Chicken-Disease-Classification-Project"
AUTHOR_USERNAME_NAME = "shaAhame"
SRC_REPO ='chicken_disease_classification'
AUTHOR_EMAIL='shakeebahamed456@gmail.com'

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USERNAME_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for chicken disease classification",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USERNAME_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USERNAME_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
)