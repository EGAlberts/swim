FROM gabrielmoreno/omnetpp-vnc:5.4.1
LABEL Description="Docker image for SWIM"

USER root
RUN apt update && apt install -y --no-install-recommends libboost-all-dev git r-base r-cran-reshape r-cran-ggplot2 r-cran-rsqlite evince ristretto nano curl python3-dev

RUN curl -fsSL https://bootstrap.pypa.io/pip/3.5/get-pip.py | python3.5

ENV BASE_DIR=${HOME}/seams-swim

WORKDIR ${BASE_DIR}

RUN git clone https://github.com/EGAlberts/swim.git

WORKDIR ${BASE_DIR}/swim

RUN git clone https://github.com/EGAlberts/MASCed_bandits.git

RUN mv ./SWIMInternalInterface.py  ${BASE_DIR}/swim/MASCed_bandits/masced_bandits/

WORKDIR ${BASE_DIR}/swim/MASCed_bandits/



RUN pip install -r requirements.txt

RUN python3 setup.py develop 

WORKDIR ${BASE_DIR}

RUN tar xzf swim/queueinglib.tgz

WORKDIR ${BASE_DIR}/queueinglib

RUN make -j$(nproc)

WORKDIR ${BASE_DIR}/swim

RUN make cleanall && make makefiles && make -j$(nproc)

WORKDIR ${BASE_DIR}/swim/examples/simple_am

RUN make -j$(nproc)

RUN R -e 'install.packages("https://github.com/wilkelab/cowplot/archive/0.6.3.tar.gz", repos=NULL)'

# configure OMNeT++ IDE
WORKDIR ${BASE_DIR}
RUN mkdir -p workspace; $(dirname `which omnetpp`)/../ide/omnetpp -nosplash -data workspace -application org.eclipse.cdt.managedbuilder.core.headlessbuild -importAll .

WORKDIR ${HOME}
RUN mkdir -p .local/share/applications/
COPY omnetpp.desktop .local/share/applications/


