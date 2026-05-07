import setuptools
from setuptools import setup, find_packages



setup(
    name='cellSegmentation',
    version='0.0.0',
    author='Pranav4005',
    description="A cell segmentation package",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    install_requires=[]
)