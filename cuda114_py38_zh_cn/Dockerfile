FROM nvidia/cuda:11.4.3-cudnn8-devel-ubuntu18.04

# software-properties-common -> python 3.8
# libsm6, libxrender-dev, libxext6, libgl1 -> opencv
# libpq-dev -> psycopg2
# libzbar0 -> pyzbar
# tzdata -> time
# locales -> en_US.UTF-8
RUN apt -y update \ 
    &&  DEBIAN_FRONTEND=noninteractive apt install -y \
        build-essential \
        cmake \
        software-properties-common \
        libsm6 \
        libxrender-dev \
        libxext6 \
        libgl1 \
        libpq-dev \
        libzbar0 \
        tzdata \
        locales \
        libksba8=1.3.5-2ubuntu0.18.04.2 \
        libssl1.1=1.1.1-1ubuntu2.1~18.04.23 \
        linux-libc-dev=4.15.0-213.224 \
        openssl=1.1.1-1ubuntu2.1~18.04.23

# python3.8 env
RUN yes '' | add-apt-repository ppa:deadsnakes/ppa
RUN apt install -y python3.8-dev python3-pip
RUN rm /usr/bin/python3 && ln -s /usr/bin/python3.8 /usr/bin/python3

RUN pip3 install pip==21.2.1

RUN TZ=Asia/Taipei \
    && ln -snf /usr/share/zoneinfo/$TZ /etc/localtime \
    && echo $TZ > /etc/timezone \
    && dpkg-reconfigure -f noninteractive tzdata 

RUN sed -i -e 's/# en_US.UTF-8 UTF-8/en_US.UTF-8 UTF-8/' /etc/locale.gen \
    && locale-gen
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8  
