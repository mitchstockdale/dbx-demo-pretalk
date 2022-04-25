from setuptools import find_packages, setup
from dbx_demo_pretalk import __version__

setup(
    name="dbx_demo_pretalk",
    packages=find_packages(exclude=["tests", "tests.*"]),
    setup_requires=["wheel"],
    version=__version__,
    description="",
    author=""
)
