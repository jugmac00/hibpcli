import os

from setuptools import find_packages, setup

HERE = os.path.abspath(os.path.dirname(__file__))
VERSION = "0.8.0"


def read(*parts):
    """Build an absolute path from *parts*...

    ... and return the contents of the resulting file.
    Assume UTF-8 encoding.

    Thanks to:
    https://hynek.me/articles/sharing-your-labor-of-love-pypi-quick-and-dirty/
    """
    with open(os.path.join(HERE, *parts), encoding="utf-8") as f:
        return f.read()


setup(
    name="hibpcli",
    version=VERSION,
    description="A command line interface for the **haveibeenpwned.com** API - "
    "speaks keepass.",
    long_description=read("README.rst") + "\n\n" + read("CHANGES.rst"),
    long_description_content_type="text/x-rst",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Programming Language :: Python :: 3.14",
        "Development Status :: 4 - Beta",
        "Environment :: Console",
    ],
    python_requires=">=3.10",
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
        "pykeepass>=4.0.1",
        "httpx>=0.13.3",
    ],
    entry_points={"console_scripts": ["hibpcli = hibpcli.cli:main"]},
)
