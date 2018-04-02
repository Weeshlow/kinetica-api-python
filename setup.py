# Install the GPUdb python API to the system module path.

from setuptools import setup, find_packages, Extension


from distutils.core import setup
import os
import sys


# Get a list of files in the subdirectories only.
# File paths are relative the input directory.
def package_files(directory):
    directory = os.path.normpath(directory)
    num_paths = directory.count(os.path.sep)+1
    paths = []
    for (path, directories, filenames) in os.walk(directory):
        if os.path.normpath(path) == directory :
            continue

        for filename in filenames:
            file_basename, file_extension = os.path.splitext(filename)
            if file_extension and (file_extension.lower() != ".pyc"):
                local_path = path.split(os.path.sep, num_paths)[num_paths]
                local_filepath = os.path.join(local_path, filename)
                paths.append(local_filepath)

    return paths


# Package up the files in the subdirectories too.
current_path = os.path.dirname(os.path.abspath(__file__))
extra_files = package_files(current_path+'/gpudb')


setup(
    name = 'gpudb',
    packages = ['gpudb'],
    version = '6.2.0.2',
    description = 'Python client for GPUdb',
    long_description = "The client-side Python API for Kinetica.  Create, store, retrieve, and query data with ease and speed.",
    author = 'Kinetica DB Inc.',
    author_email = 'mmahmud@kinetica.com',
    package_data = {'gpudb': extra_files},
    url = 'http://www.kinetica.com',
    download_url = 'https://github.com/kineticadb/kinetica-api-python/archive/v6.2.0.2.tar.gz',
    install_requires = [ "future" ],
    ext_modules = [ Extension( "gpudb.protocol",
                               sources = ["protocol/avro.c",
                                          "protocol/bufferrange.c",
                                          "protocol/common.c",
                                          "protocol/dt.c",
                                          "protocol/protocol.c",
                                          "protocol/record.c",
                                          "protocol/schema.c"] ) ]
)
