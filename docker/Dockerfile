FROM python:3.8

WORKDIR /root

RUN git clone https://github.com/kakao/khaiii.git && \
    apt-get update -y && \
    apt-get upgrade -y && \
    cd /root/khaiii && \
    pip install cython && \
    pip install --upgrade pip && \
    pip install -r requirements.txt && \
    mkdir build && \
    cd /root/khaiii/build && \
    cmake .. && \
    make all && \
    make resource && \
    make package_python && \
    cd package_python && \
    pip install .

RUN apt-get install locales -y && \
    localedef -f UTF-8 -i ko_KR ko_KR.UTF-8 && \
    localedef -f UTF-8 -i en_US en_US.UTF-8
ENV LC_ALL C.UTF-8

RUN git clone https://github.com/fruit-team/fruit_knife.git 

RUN pip install flask
