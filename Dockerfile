FROM epinux/grass-notebook

MAINTAINER Massimo Di Stefano  <epiesasha@me.com>

USER epinux

ADD index.ipynb /home/epinux/work/
ADD mgutil.ipynb /home/epinux/work/
COPY ipygrass/ /home/epinux/work/ipygrass/
COPY GRM/ /home/epinux/work/GRM/
RUN mkdir /home/epinux/work/GRM/tmp
ENV PYTHONPATH /home/epinux/work/ipygrass:$PYTHONPATH

USER root
RUN wget http://epinux.com/epinux_data/grassdata.zip && \
unzip grassdata.zip && \
rm -rf grassdata.zip && mv /home/epinux/work/home/epinux/grassdata /home/epinux/ && rm -rf /home/epinux/work/home/epinux/
RUN chown -R epinux /home/epinux
RUN chmod -R 777 /home/epinux/work/data
RUN updatedb
RUN pip3 install grass-session

USER epinux
