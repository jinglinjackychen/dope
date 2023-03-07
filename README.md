# dope

## clone repo
```
    $ git clone --recursive git@github.com:jinglinjackychen/dope.git
```

*You can run this code on a GPU computer and CPU computer, but if you want to execute DOPE program, please change GPU computer to run*

---
|Device         |GPU            |IP                         |
|:-------------:|:-------------:|:-------------------------:|
|LoCoBot        |No             |10.0.0.2 and 192.168.50.2  |
|VR PC          |Yes            |10.0.0.3                   |
|DOPE PC        |Yes            |192.168.50.3               |

![Teaser](figures/network.PNG)
---

## Building docker image
```
    $ cd Docker && source build.sh
```

## **Download weights**
```
    Download [the weights](https://drive.google.com/open?id=1DfoA3m_Bm0fW8tOWXGVxi4ETlLEAgmcg) and save them to the `weights` folder, *i.e.*, `~/catkin_ws/src/Deep_Object_Pose/weights/`.
```

## How to run
On LoCoBot
```
    $ source environment.sh 192.168.50.2 192.168.50.2
    $ roslaunch realsense2_camera rs_rgbd.launch
    $ roslaunch rosbridge_server rosbridge_websocket.launch
```
On DOPE PC
```
    $ cd Docker && source docker_run.sh gpu
    Docker$ cd catkin_ws && catkin_make
    Docker$ source environment.sh 192.168.50.2 192.168.50.3
    Docker$ rosrun image_transport republish compressed in:=/camera/color/image_raw raw out:=/dope/image_raw
    Docker$ roslaunch dope dope.launch
```

## If you want to enter same container
```
    $ cd Docker && source docker_join.sh
    Docker$ source environment.sh 192.168.50.2 192.168.50.3
