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
    url="https://github.com/lovef/.lovef",
    packages=setuptools.find_packages(),
    entry_points={
        'console_scripts': [
            'parse=lovef.parse:main',
            'pretty=lovef.pretty:main',
            'uuid=lovef.uuid:main',
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
