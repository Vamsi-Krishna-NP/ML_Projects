from setuptools import setup, find_packages


HYPEN_E_DOT = "-e ."
def get_requirements(file_path: str) -> list[str]:
    """This function returns a list of requirements."""
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]
        if  HYPEN_E_DOT in requirements:
            requirements.remove("-e .")
    return requirements


setup(
    name="mlprojects",
    version="0.0.1",
    author="Vamsi Krishna",
    author_email="mr.vkjilla2024@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt")
)