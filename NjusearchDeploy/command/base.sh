#! /bin/bash
yum -y install vim 
yum -y install git
yum -y install gcc
yum -y install wget
yum -y install unzip
#for pillow
yum -y install zlib
yum -y install python-devel libjpeg-devel zlib-devel
#for lxml
yum -y install python-lxml
yum install libxslt-devel libxml2-devel libxml2 libxslt
#for upload things
yum -y install lrzsz

