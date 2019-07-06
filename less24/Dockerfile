#---------------------------------------------------------------------------
# Dockefile to build Docker Image of Python App  running on Ubuntu
#---------------------------------------------------------------------------

# Starting from base image
FROM my_ubuntu_v1:latest


# Install Python & pip
RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get install -y python3.7
RUN apt-get install python3-pip

# Install nano and bash for #debugging
RUN apt-get install -y nano
RUN apt install bash-completion

# Install dependencies via pip
WORKDIR /root/mydocker
RUN pip3 install -r /root/mydocker/requirements.txt

#COPY requirements.txt ./
#COPY ./test_ssh_service.py /root/docker
