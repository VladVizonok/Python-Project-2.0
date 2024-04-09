from setuptools import setup, find_namespace_packages

setup(name= 'CLI_2_0',
      version= '1',
      description= 'Your personal helper.',
      url= 'https://github.com/VladVizonok/Python-Project-2.0.git',
      author= 'vlad_vznk',
      license= 'MIT',
      packages= find_namespace_packages(),
      install_requires=['pickle', 
                        'collections', 
                        'rich', 
                        'prompt_toolkit'],
      entry_points={'console_scripts': ['cli = CLI_2_0.main:main']}
      )