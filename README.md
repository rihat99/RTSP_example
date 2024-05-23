# RTSP_example

Test simple yet effective RTSP stream over local network.

## Installation

### Server Machine (with camera)

1. create and activate conda environment
2. `sudo apt-get install ffmpeg`
3. `pip install opencv-python Flask`
4. Download revelant version from [here](https://github.com/bluenviron/mediamtx/releases/tag/v1.8.2) (Intel processors are amd64)
5. Unzip in your project directory

### Client Machine (viewer)

Option 1: Use any media player that support RTSP links, for example VLC

Option 2: Use python script, follow steps 1-3 above to install required packages.


## Preparation

1. Obtain IP address of the machine, for example `ifconfig` in terminal.
2. Test and adjust parameters of camera frames grabing on server side, `python video_stream.py`

    a. default value for external camera index is 0 (can also try 1 or 2)

    b. change resoluton and fps if required

    c. don't forget to mirror camera settings changes to `app.py`

3. On client side, put IP address of server into `cleint.py` if script will be used.


## Running

### Server Machine

1. In terminal 1: run the server `cd mediamtx_v1.8.1_linux_amd64` and `./mediamtx`
2. In terminal 2: run camera application `python app.py`
2. In terminal 3: run ffmpeg `ffmpeg -f mjpeg -i http://<your_computer_ip>:5000/video_feed -c:v libx264 -preset ultrafast -tune zerolatency -f rtsp rtsp://localhost:8554/live.sdp`

### Client Machine

Option 1: put the link `rtsp://<your_computer_ip>/live.sdp` into the media player.

Option 2: run receiver application `python client.py`
