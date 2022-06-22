from setuptools import find_packages, setup

setup(
    name="TemplatePythonPackage",
    version="0.1.0",
    description="A Minimal Template Python Package",
    url="https://github.com/RealityBending/TemplatePythonPackage",
    author="Dominique Makowski",
    author_email="dom.makowski@gmail.com",
    license="MIT",
    install_requires=["numpy", "pandas", "scipy", "matplotlib"],
    packages=find_packages(),
    zip_safe=False,
)
