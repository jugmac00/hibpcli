from setuptools import find_packages, setup

version = "0.4.0.dev"

with open("README.rst") as readme_file:
    README = readme_file.read()

with open("CHANGES.rst") as changes_file:
    CHANGES = changes_file.read()


setup(
    name="hibpcli",
    version=version,
    description="A command line interface for the **haveibeenpwned.com** API - "
    "speaks keepass.",
    long_description=README + "\n\n" + CHANGES,
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Development Status :: 4 - Beta",
        "Environment :: Console",
    ],
    author="Jürgen Gmach",
    author_email="juergen.gmach@goglemail.com",
    url="https://github.com/jugmac00/hibpcli",
    license="MIT",
    packages=find_packages("src"),
    package_dir={"": "src"},
    extras_require={"test": ["pytest >=5.2.2", "pytest-cov",], "dev": ["pdbpp"]},
    include_package_data=True,
    zip_safe=True,
    install_requires=["click ==7.1.2", "pykeepass == 3.2.0", "httpx == 0.13.1",],
    entry_points={"console_scripts": ["hibpcli = hibpcli.cli:main"]},
)
