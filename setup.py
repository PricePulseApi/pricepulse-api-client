from setuptools import setup, find_packages

setup(
    name="pricepulse-client",
    version="1.0.0",
    description="Official Python SDK Client for PricePulse API on RapidAPI",
    author="PricePulse API Team",
    url="https://github.com/PricePulseApi/pricepulse-api-client",
    py_modules=["pricepulse_client"],
    install_requires=[
        "httpx>=0.25.0",
    ],
    entry_points={
        "console_scripts": [
            "pricepulse=cli:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)
