# -*- coding: utf-8 -*-
import setuptools

with open("README.md", "r") as file:
    long_description = file.read()

setuptools.setup(
    name="multiprocessor-antoniojkim",
    version="0.0.1",
    author="Antonio J Kim",
    author_email="contact@antoniojkim.com",
    description="A small wrapper for Python multiprocessing for ease of use.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/antoniojkim/Multiprocessor",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    include_package_data=True,
)
