from os import path
import sys

root_dir = path.abspath(path.dirname(__file__))


def _get_platform_str():
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
            6: 'cp36-cp36m-win_amd64',
            7: 'cp37-cp37m-win_amd64',
            8: 'cp38-cp38-win_amd64',
            9: 'cp39-cp39-win_amd64'
        }

        result = minor_version_str[sys.version_info.minor]

    return result


def get_wheel_paths():
    platform_str = _get_platform_str()

    # The order these packages are intalled  matters, which is why
    # this does not just do something like
    # `glob.glob('{}/dependancy_wheels/*.whl'.format(root_dir))`

    if (sys.version_info.major == 2):
        wheel_list = [
            (platform_str, 'pyproj-1.9.6-{}.whl'.format(platform_str)),
            (platform_str, 'Shapely-1.6.4.post2-{}.whl'.format(platform_str)),
            (platform_str, 'GDAL-2.2.4-{}.whl'.format(platform_str)),
            (platform_str, 'Fiona-1.8.13-{}.whl'.format(platform_str)),
            (platform_str, 'Rtree-0.9.3-{}.whl'.format(platform_str))
        ]
    else:
        wheel_list = [
            (platform_str, 'pyproj-3.0.0.post1-{}.whl'.format(platform_str)),
            (platform_str, 'Shapely-1.7.1-{}.whl'.format(platform_str)),
            (platform_str, 'GDAL-3.1.4-{}.whl'.format(platform_str)),
            (platform_str, 'Fiona-1.8.17-{}.whl'.format(platform_str)),
            (platform_str, 'Rtree-0.9.4-{}.whl'.format(platform_str))
        ]

    # platform netural packages. This is installed here (rather than using the
    # `install_requires` parameter, because of the dependancy on other wheel files.
    wheel_list.append(('py2.py3-none-any', 'geopandas-0.6.2-py2.py3-none-any.whl'))

    return [path.join(root_dir, 'dependency_wheels', dir_name, wheel_name) for dir_name, wheel_name in wheel_list]
