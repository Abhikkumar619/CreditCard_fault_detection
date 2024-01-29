import setuptools

__version__="0.0.0"
AUTHOR_NAME="Abhikkumar619"
AUTHOR_EMAIL="abisheky194@gmail.com"
REPO_NAME="CreditCard_fault_detection"
SRC_REPO="Credit_card_project"


setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for ml app", 
    long_description_content="text/markdown", 
    url=f"https://github.com/{AUTHOR_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker":f"https://github.com/{AUTHOR_NAME}/{REPO_NAME}/issues"
    },
    package_dir={"":"src"}, 
    packages=setuptools.find_packages(where="src")
)