from setuptools import setup, find_packages

setup(name='py-hartzell',
      # bumpversion, anyone?
      # keep py_hartzell/__init__.py in sync!
      version='0.1.2',
      description="George's common python modules and tools",
      url='https://github.com/hartzell/py-hartzell',
      author='George Hartzell',
      author_email='hartzell@alerce.com',
      license='none',
      packages=find_packages(),
      python_requires='>=2.7.12,<3.0',
      install_requires=[
          # add All The Things to install here
          'jinja2',
      ],
      setup_requires=[
          # Normally these would be a requirement for testing *this*
          # package.  Perhaps we want to consider install_requires so that
          # they're available for others to use.
          'pytest-flake8',
          'pytest-runner',
          # pytest must be last in the list.  sigh...
          # https://github.com/pytest-dev/pytest-runner/issues/11#issuecomment-190355698
          'pytest',
      ],
      tests_require=[
      ],
      include_package_data=True,
      zip_safe=False)
