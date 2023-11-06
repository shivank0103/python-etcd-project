import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

setup(
    name='cashifypythonetcd',
    version='0.4.5',
    description='Get configurable values from ETCD',
    url='https://github.com/shivank0103/python-etcd-project',
    author='Shivank',
    author_email='shivank0103@gmail.com',
    packages=['cashifyetcd'],
    long_description=README,
    long_description_content_type="text/markdown",
    install_requires=[
        'python-etcd==0.4.5',
        'etcd==1.1.2 '
    ],
    zip_safe=False
)
