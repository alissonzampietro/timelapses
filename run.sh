if pgrep fswebcam &> /dev/null ; then sudo killall fswebcam ; fi
fswebcam -r 1920x1080 --no-banner ./photos/%Y%m%d%H%M%S.jpg --loop 10 -b
