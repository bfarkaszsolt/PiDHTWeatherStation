#! bin/usr/gnuplot

set xdata time;
set timefmt "%Y-%m-%d %H:%M:%S";
set terminal gif;
#set output "/etc/weather/log/gnu_output.gif";
set output "/var/www/html/gnu_output.gif";
plot "/etc/weather/log/logtest" using 1:3 title "temperature" with linespoints, "/etc/weather/log/logtest" using 1:4 title "Humidity" with linespoints
