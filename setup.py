import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="lovef",
    version="0.0.1",
    author="lovef",
    author_email="lovef.code@gmail.com",
    description="A collection of utility scripts",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    # packages=setuptools.find_packages(),
    scripts=[
        'scripts/uuid'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
