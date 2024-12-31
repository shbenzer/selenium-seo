from setuptools import setup, find_packages

setup(
    name="selenium-seo",
    version="1.0.0",
    author="Simon Benzer",
    author_email="SimonHBenzer@gmail.com",
    description="selenium-seo extends Selenium by providing a keyword analyzer on a given webpage",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/shbenzer/selenium-seo",
    packages=find_packages(),
    install_requires=[
        "selenium>=4.0.0",
        "beautifulsoup4>=4.10.0"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    include_package_data=True,
)