import setuptools
import setuptools_git_ver

with open('readme.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name="clicolor",
    version=setuptools_git_ver.get_version("{tag}.dev+git.{sha}"),
    author="Camas",
    description="Quick python reference for terminal color escape codes",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/camas/clicolors",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
