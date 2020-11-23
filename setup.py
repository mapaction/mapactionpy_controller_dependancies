import subprocess
import sys
from setuptools import setup, find_packages
# from setuptools import find_packages
# from distutils.cmd import Command
# from distutils.command.install import install as Command
from setuptools.command.develop import develop
from setuptools.command.install import install
# from distutils.core import setup
from os import path, environ

_base_version = '0.1'

root_dir = path.abspath(path.dirname(__file__))


def install_from_wheels(command_subclass):
    """A decorator for classes subclassing one of the setuptools commands.

    It modifies the run() method so that it prints a friendly greeting.

    https://blog.niteo.co/setuptools-run-custom-code-in-setup-py/
    """
    orig_run = command_subclass.run

    def get_platform_str(self):
        result = None
        if (sys.version_info.major == 2):


            if sys.maxsize > 2**32:
                # if 64bit:
                result = 'cp27-cp27m-win_amd64'
            else:
                # 32 bit
                result = 'cp27-cp27m-win32'
        else:
            minor_version_str = {
                6 : 'cp36-cp36m-win_amd64',
                7 : 'cp37-cp37m-win_amd64',
                8 : 'cp38-cp38-win_amd64',
                9 : 'cp39-cp39-win_amd64'
            }
            
            result = minor_version_str[sys.version_info.minor]

        return result

    def modified_run(self):
        print('Custom run() method')

        if sys.platform == 'win32':
            import pip
            platform_str = self.get_platform_str()

            # The order these packages are intalled  matters, which is why
            # this does not just do something like
            # `glob.glob('{}/dependancy_wheels/*.whl'.format(root_dir))`
            wheel_list = [
                (platform_str, 'pyproj-1.9.6-{}.whl'.format(platform_str)),
                (platform_str, 'Shapely-1.6.4.post2-{}.whl'.format(platform_str)),
                (platform_str, 'GDAL-2.2.4-{}.whl'.format(platform_str)),
                (platform_str, 'Fiona-1.8.13-{}.whl'.format(platform_str)),
                (platform_str, 'Rtree-0.9.3-{}.whl'.format(platform_str))
            ]

            # platform netural packages. This is installed here (rather than using the
            # `install_requires` parameter, because of the dependancy on other wheel files.
            wheel_list.extend([('py2.py3-none-any','geopandas-0.6.2-py2.py3-none-any.whl')])

            for dir_name, wheel_name in wheel_list:
                wheel_path = path.join(root_dir, 'dependency_wheels', dir_name, wheel_name)
                print('Installing {} from wheel file.'.format(wheel_path))
                pip.main(['install', wheel_path])

        print('About to call default install run() method')
        orig_run(self)

    command_subclass.run = modified_run
    return command_subclass


@install_from_wheels
class CustomDevelopCommand(develop):
    pass


@install_from_wheels
class CustomInstallCommand(install):
    pass


def readme():
    with open(path.join(root_dir, 'README.md')) as f:
        return f.read()


# See https://packaging.python.org/guides/single-sourcing-package-version/
# This uses method 4 on this list combined with other methods.
def _get_version_number():
    travis_build = environ.get('TRAVIS_BUILD_NUMBER')
    travis_tag = environ.get('TRAVIS_TAG')

    if travis_build:
        if travis_tag:
            version = travis_tag
        else:
            version = '{}.dev{}'.format(_base_version, travis_build)

        with open(path.join(root_dir, 'VERSION'), 'w') as version_file:
            version_file.write(version.strip())
    else:
        try:
            ver = subprocess.check_output(['git', 'rev-parse', '--short', 'HEAD'])
            version = '{}+local.{}'.format(_base_version, ver.decode('ascii').strip())
        except Exception:
            with open(path.join(root_dir, 'VERSION')) as version_file:
                version = version_file.read().strip()

    return version

setup(
    name='mapactionpy_controller',
    cmdclass={
        'install': CustomInstallCommand,
        'develop': CustomDevelopCommand,
    },
    version=_get_version_number(),
    description='Controls the workflow of map and infographic production',
    long_description=readme(),
    long_description_content_type="text/markdown",
    url='http://github.com/mapaction/mapactionpy_controller',
    author='MapAction',
    author_email='github@mapaction.com',
    license='GPL3',
    packages=find_packages(),
    include_package_data=True,
    test_suite='unittest',
    tests_require=['unittest'],
    zip_safe=False,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Environment :: Win32 (MS Windows)",
        "Operating System :: Microsoft :: Windows"
    ])
