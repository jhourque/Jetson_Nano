# After first boot

## Info nvpmodel
```
sudo nvpmodel -q --verbose
sudo nvpmodel -m 0
```

## Update
```
sudo apt-get update
```

## Install swap
```
git clone https://github.com/JetsonHacksNano/installSwapfile
cd installSwapfile
./installSwapfile.sh
sudo reboot
```

## Install opencv 4
```
sudo apt update
sudo apt install -y build-essential cmake git libgtk2.0-dev pkg-config  libswscale-dev libtbb2 libtbb-dev
sudo apt install -y python-dev python3-dev python-numpy python3-numpy
sudo apt install -y curl
sudo apt install -y libjpeg-dev libpng-dev libtiff-dev 				# libjasper-dev 
sudo apt install -y libavcodec-dev libavformat-dev
sudo apt install -y libgstreamer1.0-dev libgstreamer-plugins-base1.0-dev
sudo apt install -y libv4l-dev v4l-utils qv4l2 v4l2ucp libdc1394-22-dev
curl -L https://github.com/opencv/opencv/archive/4.1.0.zip -o opencv-4.1.0.zip
curl -L https://github.com/opencv/opencv_contrib/archive/4.1.0.zip -o opencv_contrib-4.1.0.zip
unzip opencv-4.1.0.zip 
unzip opencv_contrib-4.1.0.zip 
cd opencv-4.1.0/
mkdir release
cd release/
cmake   -D WITH_CUDA=ON \
        -D OPENCV_EXTRA_MODULES_PATH=../../opencv_contrib-4.1.0/modules \
        -D WITH_GSTREAMER=ON \
        -D WITH_LIBV4L=ON \
        -D BUILD_opencv_python2=ON \
        -D BUILD_opencv_python3=ON \
        -D BUILD_TESTS=OFF \
        -D BUILD_PERF_TESTS=OFF \
        -D BUILD_EXAMPLES=OFF \
        -D CMAKE_BUILD_TYPE=RELEASE \
        -D CMAKE_INSTALL_PREFIX=/usr/local ..
make -j4
sudo make install
```

## Install tensorflow
```
sudo apt-get update
sudo apt-get install libhdf5-serial-dev hdf5-tools libhdf5-dev zlib1g-dev zip libjpeg8-dev
sudo apt-get install python3-pip
sudo pip3 install -U pip
sudo pip3 install -U numpy==1.16.1 future==0.17.1 mock==3.0.5 h5py==2.9.0 keras_preprocessing==1.0.5 keras_applications==1.0.6 enum34 
sudo pip3 install --pre --extra-index-url https://developer.download.nvidia.com/compute/redist/jp/v42 tensorflow-gpu
sudo nvpmodel -q --verbose

```
