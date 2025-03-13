import setuptools
with open("README.md" , "r", encoding = "utf-8" ) as f:
    long_discription = f.read()


__version__ = "0.0.0"

REPO_NAME = "Chicken-Disease-Classification-Project"
AUTHOR_USER_NAME:   "zunaed-88"
SRC_REPO = "cnnClassifier"
AUTHOR_EMAIL: "junaidahmed.phy@gmail.com"

setuptools.setup(
    name = REPO_NAME,
    version= __version__,
    author = AUTHOR_USER_NAME,
    author_email= AUTHOR_EMAIL,
    description= " This is a cnn classifier based on chicken disease",
    long_description= long_discription,
    long_description_content_type= "text/markdown",
    url =f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls= {
        "Bug Tracker" : f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir= {"":  "src"},
    packages= setuptools.find_packages(where ="src"),
)
