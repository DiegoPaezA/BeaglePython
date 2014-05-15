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

echo Wait a few seconds for the USB to be ready
sleep 5

echo Initialising wireless interface
ifconfig wlan0 inet 192.168.11.65
echo Starting DHCP server
/usr/sbin/udhcpd -f -S /etc/udhcpd.conf.wlan &
echo Starting AP software
# /usr/local/bin/hostapd /etc/hostapd.conf
hostapd /etc/hostapd.conf

echo Fin Ok
