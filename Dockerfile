FROM yetongxue/ubuntu-python3.6
MAINTAINER yetongxue<me@xander-ye.com>
ENV TZ "Asia/Shanghai"

ENV DJANGO_SETTINGS_MODULE demo.settings.deploy
WORKDIR /root
RUN mkdir static log

WORKDIR /root/project
COPY ./requirements.txt ./
RUN pip3.6 install pip --upgrade
RUN pip3.6 install -r requirements.txt

COPY ./ ./

EXPOSE 80
RUN chmod +x entry_point.sh wait-for-it.sh
ENTRYPOINT ["./entry_point.sh"]