import os
from setuptools import setup
 
with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()
 
# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))
 
setup(
    name='reusable_threads_app',
    version='1.0.0',
    packages=['reusable_threads'],
    include_package_data=True,
    license='BSD License',  # example license
    description='Django app to create a forum',
    long_description=README,
    url='https://github.com/ChristineMWilde',
    author='Christine Wilde',
    author_email='yourname@example.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License', # example license
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    install_requires = [
        'django_forms_bootstrap',
        'django-tinymce',
        'django-emoticons',
    ],
)