import sys
from glob import glob
from os.path import basename, splitext
from pathlib import Path

from setuptools import find_packages, setup

CURRENT_DIR = Path(__file__).parent
sys.path.insert(0, str(CURRENT_DIR))  # for setuptools.build_meta


def get_long_description() -> str:
    return (
            (CURRENT_DIR / "README.md").read_text(encoding="utf8")
    )


setup(
    name="catto",
    version="1.0.4",
    description="A simple command line tool that downloads cute animals images of your choice.",
    long_description=get_long_description(),
    author="KortaPo",
    author_email="bereckobrian@gmail.com",
    maintainer="KortaPo",
    maintainer_email="bereckobrian@gmail.com",
    license="BSD 3 CLAUSE LICENSE",
    packages=find_packages(where="src"),
    py_modules=[splitext(basename(path))[0] for path in glob("src/*.py")],
    package_dir={"": "src"},
    include_package_data=True,
    python_requires=">=3.8",
    install_requires=[
        "typer",
        "rich",
        "loguru",
        "requests",
        "questionary",
        "pyfiglet",
        "colorama",
        "pillow",
    ],
    zip_safe=False,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3 :: Only",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Software Development :: Quality Assurance",
    ],
    entry_points={"console_scripts": ["catto = catto:main"]},
)
