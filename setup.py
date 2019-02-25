import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="docx2json",
    version="0.0.6",
    author="andremsouza",
    author_email="msouza.andre@hotmail.com",
    description="Python script that converts text from a .docx file into .json format.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/andremsouza/docx2json",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "python-docx"
    ]
)
