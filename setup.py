from setuptools import find_packages, setup

setup(
    name="ownca-rest-api",
    version="1.0.0",
    url="https://github.com/ownca/ownca-rest-api",
    author="Kairo de Araujo",
    author_email="kairo@dearaujo.nl",
    description="OwnCA REST API",
    packages=find_packages(),
    install_requires=["flask", "flask-restx", "ownca"],
)
