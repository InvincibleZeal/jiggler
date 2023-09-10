from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="jiggler",
    version="0.0.3",
    author="Ritesh Ganjewala",
    author_email="ritesh.ganjewala17@gmail.com",
    license="MIT",
    description="Keep your screen awake and working while you rest",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/InvincibleZeal/jiggler",
    py_modules=["jiggler"],
    packages=find_packages(),
    install_requires=["click >= 7", "pynput >= 1"],
    python_requires=">=3",
    classifiers=[
        "Intended Audience :: End Users/Desktop",
        "Topic :: Utilities",
        "Topic :: Terminals",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows :: Windows NT/2000",
        "Operating System :: POSIX",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.9",
    ],
    entry_points="""
        [console_scripts]
        jiggler=jiggler:start
    """,
)
