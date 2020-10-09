
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="wimstudy", 
    version="0.0.1",
    author="Katie Wimmer",
    author_email="krwim78@gmail.com",
    description="Library for study tool",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/katiewimmer/wimstudy",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
