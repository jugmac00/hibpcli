import codecs
import os

from setuptools import find_packages, setup

HERE = os.path.abspath(os.path.dirname(__file__))
VERSION = "0.5.0"


def read(*parts):
    """Build an absolute path from *parts*...

    ... and return the contents of the resulting file.
    Assume UTF-8 encoding.

    Thanks to:
    https://hynek.me/articles/sharing-your-labor-of-love-pypi-quick-and-dirty/
    """
    with codecs.open(os.path.join(HERE, *parts), "rb", "utf-8") as f:
        return f.read()


setup(
    name="hibpcli",
    version=VERSION,
    description="A command line interface for the **haveibeenpwned.com** API - "
    "speaks keepass.",
    long_description=read("README.rst") + "\n\n" + read("CHANGES.rst"),
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Development Status :: 4 - Beta",
        "Environment :: Console",
    ],
    author="Jürgen Gmach",
    author_email="juergen.gmach@goglemail.com",
    url="https://github.com/jugmac00/hibpcli",
    license="MIT",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    extras_require={
        "test": [
            "pytest",
            "coverage",
        ],
        "dev": ["pdbpp"],
    },
    include_package_data=True,
    zip_safe=True,
    install_requires=[
        "click>=7.1.2",
        "pykeepass>=3.2.1",
        "httpx>=0.13.3",
    ],
    entry_points={"console_scripts": ["hibpcli = hibpcli.cli:main"]},
)
