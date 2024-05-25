FROM odoo:14.0
ENV TZ=Asia/Bangkok

USER root

RUN apt-get update \
    && locale -a \
    && apt -y install vim-tiny procps htop iputils-ping

RUN apt-get update \
    && apt-get -y install git curl gcc libpython3-dev \
    && apt-get -y install rustc

RUN apt-get update \
    && apt-get -yq install locales tzdata fonts-tlwg-laksaman \
    && sed -i 's/# th_/th_/' /etc/locale.gen \
    && locale-gen \
    && cp /usr/share/zoneinfo/Asia/Bangkok /etc/localtime \
    && echo "Asia/Bangkok" > /etc/timezone \
    && dpkg-reconfigure -f noninteractive tzdata

RUN echo "alias v='ls -al'" >> /etc/bash.bashrc

USER odoo
# Copy custom addons
COPY ./addons /mnt/extra-addons

# Ensure the custom modules directory has the correct permissions
RUN chown -R odoo /mnt/extra-addons
