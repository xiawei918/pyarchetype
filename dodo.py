import os 
import webbrowser
import time

DOIT_CONFIG = {
   'action_string_formatting': 'new',
}


def task_get_image_name():
    def create_image_name():
        version = "0.1.0"
        project_name = os.path.basename(os.path.dirname(os.path.realpath(__file__)))
        image_name = f"{project_name}:{version}"
        return {"image_name": image_name, 'container_name': project_name}
    return {'actions': [(create_image_name,)]}

def task_mkdirs():
     dir_list = ["data", "notebooks", "src"]
     return {
         'actions': [f'mkdir -p {folder}' for folder in dir_list],
     }

def task_buildimage():
    return {
        'actions': ['docker build -t {image_name} .'],
        'getargs': {'image_name': ('get_image_name', 'image_name')},
        'uptodate': [False],
        'verbosity': 2,
    }

def task_dockerrun():
    return {
        'actions': ['docker run --name {container_name} --rm --detach -p 8888:8888 -v $(pwd):/project {image_name}'],
        'getargs': {'image_name': ('get_image_name', 'image_name'),
                    'container_name': ('get_image_name', 'container_name')},
        'task_dep': ['buildimage'],
        'uptodate': [False],
        'verbosity': 2,
    }

def open_notebook():
    url = "http://0.0.0.0:8888/lab"
    time.sleep(5)
    webbrowser.open_new_tab(url)

def task_notebook():
    return {
        'actions': [open_notebook],
        'task_dep': ['dockerrun'],
        'uptodate': [False],
        'verbosity': 2,
    }

