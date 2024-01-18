FROM nvcr.io/nvidia/cuda:11.4.3-cudnn8-runtime-ubuntu20.04

# install prerequisites
RUN apt -y update
RUN DEBIAN_FRONTEND=noninteractive apt install -y \
    build-essential cmake software-properties-common libssl-dev openssl wget tzdata locales

# opencv
RUN DEBIAN_FRONTEND=noninteractive apt install -y \
    libsm6 libxrender-dev libxext6 libgl1

# psycopg2
RUN DEBIAN_FRONTEND=noninteractive apt install -y libpq-dev

# zbar
RUN DEBIAN_FRONTEND=noninteractive apt install -y libzbar0

# python3.11 env
RUN apt install -y zlib1g zlib1g-dev libffi-dev libsqlite3-dev
RUN wget https://www.python.org/ftp/python/3.11.7/Python-3.11.7.tgz
RUN tar xzf Python-3.11.7.tgz

WORKDIR ./Python-3.11.7/
RUN ./configure --enable-optimizations
RUN make altinstall
RUN rm -rf /usr/bin/python3 /usr/bin/python3.8
RUN ln -s /usr/local/bin/python3.11 /usr/bin/python3
RUN ln -s /usr/local/bin/pip3.11 /usr/bin/pip3

WORKDIR ../
RUN rm -rf Python-3.11.7 Python-3.11.7.tgz

RUN TZ=Asia/Taipei \
    && ln -snf /usr/share/zoneinfo/$TZ /etc/localtime \
    && echo $TZ > /etc/timezone \
    && dpkg-reconfigure -f noninteractive tzdata 

RUN sed -i -e 's/# en_US.UTF-8 UTF-8/en_US.UTF-8 UTF-8/' /etc/locale.gen \
    && locale-gen
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8  
