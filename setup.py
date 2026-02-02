#!/usr/bin/env python3
"""
Setup script for Purpose-AI-TTA
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="purpose-ai-tta",
    version="1.0.0",
    author="Purpose-AI Team",
    description="Adaptive AI war room for chaos-to-purpose elevation",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/JimmySogaard/Purpose-Ai-TTA",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Application Frameworks",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.8",
    install_requires=[
        "python-dotenv>=1.0.0",
        "pyyaml>=6.0",
        "numpy>=1.24.0",
        "pandas>=2.0.0",
        "openai>=1.0.0",
        "anthropic>=0.18.0",
        "aiohttp>=3.9.0",
        "click>=8.1.0",
        "rich>=13.0.0",
        "cryptography>=41.0.0",
    ],
    entry_points={
        "console_scripts": [
            "purpose-ai=main:main",
        ],
    },
)
