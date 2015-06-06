#!/bin/sh
### BEGIN INIT INFO
# Provides:          startap
# Required-Start:    $all
# Required-Stop:     $all
# Default-Start:     2 3 4 5
# Default-Stop:      0 1 6
# Short-Description: inicializa el access point
# Description:       Longer script description.
### END INIT INFO


echo Starting DHCP server
/etc/init.d/dnsmasq restart &
echo Starting AP software
# /usr/local/bin/hostapd /etc/hostapd.conf
/etc/init.d/hostapd restart

echo Fin Ok
