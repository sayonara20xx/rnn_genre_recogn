from importlib.resources import path
from os import sep
import pandas as pd

paths_file = pd.read_csv('./meta.csv', sep=';')
print(paths_file)

new_paths_list = []
for p in paths_file['path']:
    # нужно было просто убрать те пути, которые были у меня в
    # облачном хранилище, беру три последних куска
    new_paths_list.append('./' + '/'.join(p.split(sep='/')[-3:]))

new_paths_file = pd.DataFrame(data={
    'genre': paths_file['genre'], 'path': new_paths_list
})

print(new_paths_file)
new_paths_file.to_csv('./local_meta.csv')