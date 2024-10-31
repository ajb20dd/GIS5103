# This is a placeholder file

from setuptools import setup, find_packages

setup(
    name="demopackage",
    version="0.1.0",
    description="A sample Python package with minor geospatial applications.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Alexander Bedine",
    author_email="ajb20dd@fsu.edu",
    url="https://github.com/ajb20dd/GIS5103",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)