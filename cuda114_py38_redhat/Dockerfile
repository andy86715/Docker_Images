FROM nvcr.io/nvidia/cuda:11.4.3-cudnn8-runtime-ubi8

# install prerequisites
RUN yum update -y && yum install -y wget tar binutils make
RUN yum install -y libcudnn8-devel-8.2.2.26-1.cuda11.4
RUN yum install -y https://dl.fedoraproject.org/pub/epel/epel-release-latest-8.noarch.rpm

# opencv
RUN yum install -y mesa-libGL.x86_64

# psycopg2
RUN yum install -y gcc postgresql-devel

# zbar
RUN yum install -y http://repo.okay.com.mx/centos/8/x86_64/release/libv4l-1.14.2-3.el8.x86_64.rpm
RUN yum install -y https://dl.fedoraproject.org/pub/epel/8/Everything/x86_64/Packages/z/zbar-libs-0.23.90-5.el8.x86_64.rpm 
RUN yum install -y https://dl.fedoraproject.org/pub/epel/8/Everything/x86_64/Packages/z/zbar-devel-0.23.90-5.el8.x86_64.rpm

# python3.8 env
RUN yum install -y gcc openssl-devel bzip2-devel libffi-devel zlib-devel
RUN wget https://npm.taobao.org/mirrors/python/3.8.8/Python-3.8.8.tgz
RUN tar -zxvf Python-3.8.8.tgz
RUN cd Python-3.8.8 \
    && ./configure --prefix=/usr/local/python3 \
    && make -j2 && make install -j2 \
    && ln -s /usr/local/python3/bin/python3.8 /usr/bin/python3 \
    && ln -s /usr/local/python3/bin/pip3 /usr/bin/pip3
RUN pip3 install pip==21.2.1

# timezone
RUN TZ=Asia/Taipei \
    && ln -snf /usr/share/zoneinfo/$TZ /etc/localtime \
    && echo $TZ > /etc/timezone \
