# pyarchetype
Skeleton for containerized project with [pydoit](https://pydoit.org/) managed tasks

For similar archetype that is managed by Gradle, see [archetype](https://github.com/xiawei918/archetype). The main difference is pyarchetype uses doit which only requires python, so it's more friendly to mac users as mac comes with its own python interpreter. On the other hand, Gradle requires Java JDK which maybe too strong a requirement.

# Getting Started

First, clone the pyarchetype project by doing

```git clone https://github.com/xiawei918/pyarchetype```

under a desired directory on your local machine.

## Installing Prerequisites

Make sure a working python is intalled on your machine. For more information, see [Python's offical page](https://www.python.org/). 

### Installing doit
pyarchetype uses [doit](https://pydoit.org/) as its build/task manager that standards all the task one can execute within archetype project. 

To start, first install doit by following the instructions [here](https://pydoit.org/install.html). Doit requires python and pip which can be verified by trying

```
python --version
pip --version
```

If on MacOS, doit can be installed via pip

```pip install doit```

### Installing Docker
pyarchetype leverages docker to containerize code for projects. Containers ensure the project can be always run in a independent and reliable environment, which will make the code easily reproducible and easy to run. 

If docker is not installed, please install docker by following the instruction [here](https://docs.docker.com/get-docker/).

## Quick start
To verify if doit is up and running, try

```doit list```

which will return a list of tasks specified in the `dodo.py` file. An example output may look like the following
```
buildimage       
dockerrun        
get_image_name   
mkdirs           
notebook         
```

Now that prerequisites are installed, one can quickly spin up a Jupyter notebook by running the following command

```doit notebook```

This will spin up a Jupyterlab on [http://0.0.0.0:8888/lab](http://0.0.0.0:8888/lab). The current directory is also mounted as a volume in the container's `project/` directory, which means any modifications you make to the notebook or any files added under the `project` directory within the docker container will be saved to your local machine.

In the background, docker will pull a Python 3.8.0 base image and install poetry that will install and manage Python related dependencies. The initial python dependencies included are:

* `python = "3.8.0"`
* `numpy = "1.19.0"`
* `dataclasses = "^0.6"`
* `matplotlib = "3.1.2"`
* `pandas = "1.0.0"`
* `notebook = "6.1.3"`
* `jupyterlab = "2.2.6"`

And the project directories structure looks like the following:

```
└── project
    ├── src
    ├── data
    └── notebooks
```

### doit tasks
There are in total 4 tasks specified in `dodo.py`, which can be checked using the `doit list1 command.
* `buildimage` - this task builds a docker image using the `Dockerfile` that comes with pyarchetype and tag it with the name of the current directory and a version of `0.1.0` which is specified in the `dodo.py` file.
* `dockerrun` - carries out the `docker run` command. The task takes the docker image created from `buildimage` task (which makes `buildimage` a dependency of `dockerrun`) and spin up a container with the current directory name.
* `get_image_name` - retrieve the current directory's name and use it plus the version number to create the name for the docker image. Used by both `buildimage` and `dockerrun`.
* `mkdir` - creates the `data`, `src`, `notebooks` directories locally so they can be mounted to the container during `dockerrun`.
* `notebook` - Opens the browser at [http://0.0.0.0:8888/lab](http://0.0.0.0:8888/lab). Depends on `dockerrun`.
