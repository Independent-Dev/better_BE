from os import name
from setuptools import setup, find_packages, version

setup(
    name='app',
    version='1.0',
    description="Practice API testing",
    author="Jinoh Kim",
    author_email="juju08217@daum.net",
    url="http://mystore.local/",
    packages=find_packages(),
    zip_safe=False,
    install_requires=[
        "pytest==6.2.4", 
        "pytest-html==3.1.1", 
        "requests==2.26.0", 
        "requests-oauthlib==1.3.0", 
        "PyMySQL==1.0.2", 
        "WooCommerce==3.0.0"
    ]
)
