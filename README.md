# dope

## clone repo
```
    git clone --recursive git@github.com:jinglinjackychen/dope.git
```

*You can run this code on a GPU computer and CPU computer, but if you want to execute DOPE program, please change GPU computer to run*

---

## Building docker image
```
    cd Docker && source build.sh
```

## How to run
```
    cd Docker && source docker_run.sh [gpu or cpu]
    Docker $ cd catkin_ws && catkin_make
    Docker $ source environment.sh
```

## If you want to enter same container
```
    $ cd Docker && source docker_join.sh
    Docker $ source environment.sh