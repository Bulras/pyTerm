import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyterm-bulras",
    version="0.0.1",
    author="Bulras",
    author_email="chateauvision@outlook.com",
    description="Python module that you can import in your project to run a terminal",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Bulras/pyTerm",
    project_urls={
        "Bug Tracker": "https://github.com/Bulras/pyTerm/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)