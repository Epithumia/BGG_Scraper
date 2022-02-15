from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="BGG Scraper",
    version="1.0.0",
    author="Rafaël Lopez",
    author_email="rafael.lopez@universite-paris-saclay.fr",
    description="Scraper pour BGG",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Epithumia/BGG_Scraper",
    project_urls={
        "Bug Tracker": "https://github.com/Epithumia/BGG_Scraper/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.5",
    packages=["bgg_scraper"],
    install_requires=["tqdm", "sqlalchemy", "urllib3"],
    scripts=["bgg_scraper/script/bgg-scraper"]
)
