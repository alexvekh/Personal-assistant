from setuptools import setup, find_namespace_packages

setup(
    name='terminal',
    version='1.0',
    description='Address Book Assistant Bot',
    url='https://github.com/alexvekh/project-team-8-Personal-assistant',
    author='Oleksy Verkhulevskyy, Aliesia Soloviova, Daniel Prokopenko, Marichka Matviiuk, Maks Pryima',
    author_email='alexvekh@yahoo.com, aliesia.soloviova@gmail.com, megaprokop3578@gmail.com, m.v.matviiuk@gmail.com, makspryima@gmail.com',
    license='MIT',
    packages=find_namespace_packages(),
    install_requires=['termcolor'],
    entry_points={'console_scripts': ['terminal = package.main:main']}
)