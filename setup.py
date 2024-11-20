from setuptools import setup, find_packages

setup(
    name="himpunan_ajj",  # Nama package
    version="1.0.0",  # Versi awal
    description="Library Python untuk operasi himpunan.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Alvin Yuga Pramana, Jason Bintang Setiawan, Javin Erasmus Clementino",
    author_email="",
    url="https://github.com/bigbosspramana/Himpunan_Python.git",
    license="MIT",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",  # Versi minimum Python
)
