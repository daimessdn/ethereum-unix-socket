# setting environment from Ubuntu 18.04
FROM ubuntu:18.04

# installing developer dependencies
RUN apt-get update && apt-get install -y nano\
                                         git \
                                         python3 python3-venv

RUN apt-get install -y python3-pip

# importing ethereum-unix-socket
## and installing Python dependencies

RUN cd /home && git clone https://github.com/daimessdn/ethereum-unix-socket && \
    cd /home/ethereum-unix-socket && \
    python3 -m venv venv && source venv/bin/activate && \
    pip install wheel && pip install-r requirements.txt
