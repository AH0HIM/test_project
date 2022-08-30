import io

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

with io.open("requirements.txt") as f:
    required = f.read().splitlines()

with io.open("Readme.md", encoding="utf-8") as f:
    long_description = f.read()


def main():
    setup(
        name='test-project',
        version='1.0',
        description='Test Project',
        long_description=open('README.md').read(),
        long_description_content_type="text/markdown",
        url="https://github.com/AH0HIM/test_project",
        author='Ikonnikov Ilya',
        author_email='i666943097@gmail.com',
        packages=[
            'test_package',
            'test_package.src',
            'test_package.src.pages',
            'test_package.tests',
            'test_package.tests.ui',
        ],
        install_requires=[
            'pytest==7.1.2',
            'selenium==4.4.3',
            'pytest-html==3.1.1',
            'webdriver-manager==3.8.3',
            'allure-pytest==2.10.0',
            'pytest-rerunfailures==10.2',
            'pytest-testconfig==0.2.0',
            'pyvirtualdisplay',
        ],
        include_package_data=True,
        keywords="Test Project Package"
    )


if __name__ == '__main__':
    main()