video-stream-downloader

Helps to download video stream using terminal

Some times urls like this http://st100.u1.videomega.tv/v/75c71f8cf72902e267838f7444e1c621.mp4?st=AYcdpSR23gCzHN4QZJSAjQ
gices server error.

For single stream URLs

vid_single.py -U http://st100.u1.videomega.tv/v/75c71f8cf72902e267838f7444e1c621.mp4?st=AYcdpSR23gCzHN4QZJSAjQ -n video_output.mp4

For fragmented video URLs use this

python vid.py -u 'http://c5.vkcache.com/sec/ZWm-VoA6SGZRiFXyY2t6Zw/1412625600/hls-vod-s4/flv/api/files/videos/2014/10/01/1412132931a40c5.mp4Frag$Num$.ts' -s 1
