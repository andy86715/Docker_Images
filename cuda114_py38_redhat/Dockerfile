FROM nvcr.io/nvidia/cuda:11.4.3-cudnn8-runtime-ubi8

# install prerequisites
RUN yum update -y && yum install -y wget tar binutils make
RUN yum install -y libcudnn8-devel-8.2.4.15-1.cuda11.4
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
# https://catalog.redhat.com/software/containers/ubi8/python-38/5dde9cacbed8bd164a0af24a?container-tabs=dockerfile&architecture=amd64&image=64cab6d204b5b858e24f2f62
RUN INSTALL_PKGS="python38 python38-devel python38-setuptools python38-pip nss_wrapper \
        httpd httpd-devel mod_ssl mod_auth_gssapi mod_ldap \
        mod_session atlas-devel gcc-gfortran libffi-devel libtool-ltdl \
        enchant krb5-devel" && \
    yum -y module enable python38:3.8 httpd:2.4 && \
    yum -y --setopt=tsflags=nodocs install $INSTALL_PKGS && \
    rpm -V $INSTALL_PKGS && \
    # Remove redhat-logos-httpd (httpd dependency) to keep image size smaller.
    rpm -e --nodeps redhat-logos-httpd && \
    yum -y clean all --enablerepo='*'
RUN pip3 install pip==21.2.1
