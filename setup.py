import os

import setuptools

PROJECT_NAME = "deep learning project"
VERSION = "1.0"
AUTHOR_USER_NAME = "Abderrazak Chahid"
AUTHOR_EMAIL = "abderrazak.chahid@gmail.com"
PROJECT_DESCRIPTION = "Train deep learning model  and deploy using Flask API server"
PROJECT_URL = ""


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setuptools.setup(
    name=PROJECT_NAME,
    version=VERSION,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description=(PROJECT_DESCRIPTION),
    long_description=read("README.md"),
    license="MIT",
    url=PROJECT_URL,
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT License",
    ],
)


# classifiers:
# Development Status:: 1 - Planning
# Development Status:: 2 - Pre-Alpha
# Development Status:: 3 - Alpha
# Development Status:: 4 - Beta
# Development Status:: 5 - Production/Stable
# Development Status:: 6 - Mature
# Development Status:: 7 - Inactive
