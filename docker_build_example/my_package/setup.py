from setuptools import setup, find_packages

setup(
    name="my_package",
    version="1.0.0",
    long_description=__doc__,
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
)
