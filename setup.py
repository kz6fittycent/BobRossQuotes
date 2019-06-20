#!/usr/bin/env python3

from setuptools import setup

setup(
    name="bobross",
    version="1.1",
    description="A collection of quotes from Bob Ross",
    long_description=open("README.md").read(),
    license="MIT",
    packages=["libbobross"],
    scripts=["bobross"],
    package_data={"libbobross": ["data/*"]},
)
