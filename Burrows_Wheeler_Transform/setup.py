import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="BWT_EmanuelSoda", # Replace with your own username
    version="0.0.1",
    author="Emanuel Michele Soda",
    author_email="emanuelsoda@gmail.com",
    description="A simple implementation of the BWT",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/EmanuelSoda/ProgrammingR",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
