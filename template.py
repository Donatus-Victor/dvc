import os

dirs = [
    
    os.path.join('data', 'raw'),  ## os.path.join will join it and the  result wont throw an error if the path is not found
    os.path.join('data', 'processed'),
    'notebooks',
    'saved_models',
    'src'
    ]

# Now creating the directory structure one by one
for dir_ in dirs:
    os.makedirs(dir_, exist_ok=True) # incase the folder is created of not exist_ok=True)
    with open(os.path.join(dir_, '.gitkeep'),'w' ) as f:
        pass
    
    # The different files that we want to create in the project structure
file_ = [
    'dvc.yaml',
    'params.yaml',
    'gitignore',
    os.path.join('src', '__init__.py')
    
    
]

for file in file_:
    with open(file, 'w') as f:
        pass
    