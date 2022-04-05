# flask-docker-hello-world


This is creating a Flask App docker image that can do simple things.
Eventually this will be extended to handle having pickled models placed in them and then used to predict when data
is input

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/KevinMunson/datascience-notebook/HEAD)

The built image is [hosted on Docker-Hub](https://hub.docker.com/layers/kevinmunson/my-datascience-notebook/latest/images/sha256:fcc8c98fe3672dfdbb84f8e5060a4d0177216ce28a094e53bc91188256954eb6).

## Using this repo
### With `docker`
Build:

```bash

# run this command to build the image

docker build --rm -t flask/flask-docker-hello-world
#this is renaming it for upload

#This is tagging the image
docker tag jupyter/my-datascience-notebook kevinmunson/my-datascience-notebook

```

Run:

```bash

# - This publishes on port 8888
# - It mount the local directory as a volume in the
#   container's home directory
# - It `--rm` container when done
# - It uses `-it` mode meaning you can cancel when you want
docker run --rm -p 8888:8888 -it -v ${pwd}:/home/jovyan/work jupyter/my-datascience-notebook
