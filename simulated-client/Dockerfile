FROM ubuntu
RUN apt-get update && apt-get install -y locales snmpd && rm -rf /var/lib/apt/lists/* \
	&& localedef -i fr_FR -c -f UTF-8 -A /usr/share/locale/locale.alias fr_FR.UTF-8
ENV LANG fr_FR.utf8
EXPOSE 161/udp
COPY snmpd.conf /etc/snmp/snmpd.conf
CMD [ "snmpd", "-f"]