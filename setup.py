import sys
from pathlib import Path

from setuptools import find_packages, setup

CURRENT_DIR = Path(__file__).parent
sys.path.insert(0, str(CURRENT_DIR))  # for setuptools.build_meta


def get_long_description() -> str:
    return (CURRENT_DIR / "README.md").read_text(encoding="utf8")


setup(
    name="catto",
    version="1.0.5.dev0",
    description="A simple command line tool that downloads cute animals images of your choice.",
    long_description=get_long_description(),
    author="KortaPo",
    author_email="bereckobrian@gmail.com",
    maintainer="KortaPo",
    maintainer_email="bereckobrian@gmail.com",
    long_description_content_type="text/markdown",
    license="BSD 3 CLAUSE LICENSE",
    packages=find_packages(where="src"),
    url="https://github.com/KortaPo/Catto",
    package_dir={"": "src"},
    include_package_data=True,
    python_requires=">=3.8",
    install_requires=[
        "certifi==2022.5.18.1; python_version >= '3.6' and python_full_version < '3.0.0' or python_full_version >= "
        "'3.6.0' and python_version >= '3.6'",
        "charset-normalizer==2.0.12; python_full_version >= '3.6.0' and python_version >= '3'",
        "click==8.1.3; python_version >= '3.7'",
        "colorama==0.4.4; (python_version >= '2.7' and python_full_version < '3.0.0') or (python_full_version >= "
        "'3.5.0')",
        "commonmark==0.9.1; python_full_version >= '3.6.3' and python_full_version < '4.0.0'",
        "idna==3.3; python_version >= '3.5' and python_full_version < '3.0.0' or python_full_version >= '3.6.0' and "
        "python_version >= '3.5'",
        "loguru==0.6.0; python_version >= '3.5'",
        "pillow==9.1.1; python_version >= '3.7'",
        "prompt-toolkit==3.0.29; python_version >= '3.6' and python_version < '4.0' and python_full_version >= '3.6.2'",
        "pyfiglet==0.8.post1",
        "pygments==2.12.0; python_full_version >= '3.6.3' and python_full_version < '4.0.0' and python_version >= 3.6'",
        "questionary==1.10.0; python_version >= '3.6' and python_version < '4.0'",
        "requests==2.27.1; (python_version >= '2.7' and python_full_version < '3.0.0') or (python_full_version >= "
        "'3.6.0')",
        "rich==12.4.4; python_full_version >= '3.6.3' and python_full_version < '4.0.0'",
        "typer==0.4.1; python_version >= '3.6'",
        "typing-extensions==4.2.0; python_full_version >= '3.6.3' and python_full_version < '4.0.0' and "
        "python_version < '3.9' and python_version >= '3.7'",
        "urllib3==1.26.9; python_version >= '2.7' and python_full_version < '3.0.0' or python_full_version >= '3.6.0' "
        "and python_version < '4'",
        "wcwidth==0.2.5; python_version >= '3.6' and python_version < '4.0' and python_full_version >= '3.6.2'",
        "win32-setctime==1.1.0; sys_platform == 'win32' and python_version >= '3.5'",
    ],
    zip_safe=False,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD CLAUSE 3 License",
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
