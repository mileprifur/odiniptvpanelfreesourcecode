#! /bin/bash
kill $(ps aux | grep 'odiniptv' | grep -v grep | grep -v 'start_services.sh' | awk '{print $2}') 2>/dev/null
sleep 1
kill $(ps aux | grep 'odiniptv' | grep -v grep | grep -v 'start_services.sh' | awk '{print $2}') 2>/dev/null
sleep 1
kill $(ps aux | grep 'odiniptv' | grep -v grep | grep -v 'start_services.sh' | awk '{print $2}') 2>/dev/null
sleep 4
sudo rm /home/odiniptv/adtools/balancer/*.json 2>/dev/null &
echo "" > /home/odiniptv/logs/error.log 2>/dev/null &
echo "" > /home/odiniptv/logs/rtmp_error.log 2>/dev/null &
echo "" > /home/odiniptv/logs/access.log 2>/dev/null &
sleep 1
sudo -u odiniptv /home/odiniptv/php/bin/php /home/odiniptv/crons/setup_cache.php 2>/dev/null
sudo -u odiniptv /home/odiniptv/php/bin/php /home/odiniptv/tools/signal_receiver.php >/dev/null 2>/dev/null &
sudo -u odiniptv /home/odiniptv/php/bin/php /home/odiniptv/tools/pipe_reader.php >/dev/null 2>/dev/null &
chown -R odiniptv:odiniptv /sys/class/net 2>/dev/null
chown -R odiniptv:odiniptv /home/odiniptv 2>/dev/null
sleep 4
/home/odiniptv/nginx_rtmp/sbin/nginx_rtmp
/home/odiniptv/nginx/sbin/nginx
# Use daemonize if available, otherwise use php-fpm directly
if command -v daemonize &> /dev/null; then
    daemonize -p /home/odiniptv/php/VaiIb8.pid /home/odiniptv/php/sbin/php-fpm --fpm-config /home/odiniptv/php/etc/VaiIb8.conf
    daemonize -p /home/odiniptv/php/JdlJXm.pid /home/odiniptv/php/sbin/php-fpm --fpm-config /home/odiniptv/php/etc/JdlJXm.conf
    daemonize -p /home/odiniptv/php/CWcfSP.pid /home/odiniptv/php/sbin/php-fpm --fpm-config /home/odiniptv/php/etc/CWcfSP.conf
else
    /home/odiniptv/php/sbin/php-fpm --fpm-config /home/odiniptv/php/etc/VaiIb8.conf &
    /home/odiniptv/php/sbin/php-fpm --fpm-config /home/odiniptv/php/etc/JdlJXm.conf &
    /home/odiniptv/php/sbin/php-fpm --fpm-config /home/odiniptv/php/etc/CWcfSP.conf &
fi