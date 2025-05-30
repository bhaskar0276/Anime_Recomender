from setuptools import setup,find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="Anime Recommendation System",
    description="A recommendation system for anime based on user preferences and viewing history.",
    version="0.1",
    author="Bhaskar Reddy",
    packages=find_packages(),
    install_requires = requirements,
)