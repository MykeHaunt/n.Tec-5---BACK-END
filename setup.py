```python
from setuptools import setup, find_packages

setup(
    name="NTec",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "tensorflow>=2.8",
        "tensorflow-io",
        "PyYAML",
        "numpy"
    ],
    entry_points={
        "console_scripts": [
            "ntec=src.main:main",
        ],
    },
)
