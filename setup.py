import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setuptools.setup(
    name="aeffect",
    author="Ben Trevett",
    author_email="bentrevett@gmail.com",
    description="Use NLP to tell you when to use affect/effect.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/bentrevett/aeffect",
    project_urls={
        "Bug Tracker": "https://github.com/bentrevett/aeffect/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    scripts=["scripts/aeffect"],
    python_requires=">=3.7",
    install_requires=[
        "torch",
        "transformers",
    ],
)
