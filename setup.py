import setuptools


def readme():
    with open("README.md") as f:
        return f.read()


setuptools.setup(
    name="MLZ",
    version="0.1",
    description="Machine learning model to predict metallicity of galaxies",
    long_description=readme(),
    keywords="Python price calculator",
    url="",
    author="Ramesh Mainali",
    author_email="ramesh.mainali2@gmail.com",
    url = 'https://github.com/mainalir/MLZ',
    packages=setuptools.find_packages(),
    install_requires=["xgboost"],
    include_package_data=True,
    package_data={"": ["model/*"]},
)
