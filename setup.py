from setuptools import setup, find_packages

setup(
    name="image-enhancer-cv",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "rembg",
        "opencv-python-headless",
        "pillow"
    ],
    author="Hamza Paul",
    author_email="hamzapaul987@gmail.com",
    description="A Python library for AI-powered image processing.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/hamzapaul-sudo/image_enhancer_cv",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
