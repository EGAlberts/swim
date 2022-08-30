#!/bin/bash
CURDIR=`pwd`
DIR=`dirname $0`
cd $DIR/omnetpp-vnc
docker build . -t egalberts/omnetpp-vnc:5.4.1
cd ..
docker build . -t egalberts/swim:1.0.1
cd $CURDIR

