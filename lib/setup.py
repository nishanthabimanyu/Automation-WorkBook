from setuptools import setup, find_packages

setup(
    name="n8n-tools",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "click",
    ],
    entry_points={
        "console_scripts": [
            "n8n-validate=n8n_tools.validate:main",
            "n8n-visualize=n8n_tools.visualize:main",
        ],
    },
)
