# RTSP_example

Test simple yet effective RTSP stream over local network.

## Installation

### Server Machine (with camera)

1. create and activate conda environment
2. `sudo apt-get install ffmpeg`
3. `pip install opencv-python`
4. Download revelant version from [here](https://github.com/bluenviron/mediamtx/releases/tag/v1.8.2) (Intel processors are amd64)
5. Unzip in your project directory

### Client Machine (viewer)

Option 1: Use any media player that support RTSP links, for example VLC
Option 2: Use python script, follow steps 1-3 above to install required packages.


## Running

### Server Machine

1. Obtain IP address of the machine, for example `ifconfig` in terminal.
2. In terminal 1: run the server `./mediamtx`
3. In terminal 2: run camera application `python app.py`
4. In terminal 3: run ffmpeg `TO DO`

### Client Machine

Option 1: put the link `TO DO` into the media player 
Option 2: run receiver application `python client.py`
