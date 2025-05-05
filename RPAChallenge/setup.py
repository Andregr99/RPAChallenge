from setuptools import setup, find_packages

setup(
    name="rpa_challenge",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "playwright==1.42.0",
        "openpyxl==3.1.2",
    ],
    entry_points={
        'console_scripts': [
            'rpa-challenge=main:main',
        ],
    },
)