import sys
from setuptools import find_packages, setup


from pathlib import Path
with open(str(Path(".") / "README.md"), "r", encoding="utf-8") as f:
    README = f.read()


setup(
    name="porygon-barcode-api",
    version="0.0.0",
    license="MIT",
    url="https://github.com/aHugues/porygon-barcode-api.git",
    description="Api to automatically get movie and serie information using their barcode",
    long_description=README,
    long_description_content_type="text/markdown",
    author="Aurélien Hugues",
    author_email="me@aurelienhugues.com",
    packages=find_packages(exclude=["tests*"]),
    include_package_data=True,
    install_requires=[
        "Flask",
    ],
    test_suite="tests",
    extras_require={
        "dev": [
            "codecov",
            "black",
            "pylint"
        ],
        "test": [
            "pytest",
            "pytest-cov",
            "pytest-isort",
            "pytest-mypy",
            "pytest-pylint",
            "pytest-flask",
            "codecov",
            "tox"
        ]
        },
    python_requires=">=3.7",
    entry_points={
        "console_scripts": [
        ]
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
)
