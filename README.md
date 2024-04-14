
> # It is not maintained.
# 📷 CamSimulate
- CamSimulate is a python application which stream Videos from local file or from a URL to video devices of your device.
- It uses v4l2loopback for creating a Virtual Video device if no physical device is available.
- It uses ffmpeg to stream the selected video to the video device either from local file or a URL.

> [!NOTE]
> It works only for UNIX-like operating system.
## Usage
- ### Clone this repository.
   ```
   git clone https://github.com/MK-1407/CamSimulate.git
   ```
- ### Install v4l2loopback.
   ```
   sudo apt install v4l2loopback-dkms
   ```
- ### Execute the main.py file.
   ```
   python3 main.py
   ```
- ### Choose Video Device.
- ### Choose file or Choose URL.
> [!WARNING]
> The URL of the video should be direct URL not of the page where you saw video. 
> example.com/video_422mp4 ✅️  
> youtube.com/this-awesome-video ❌️
- ### Use the Camera on any site you want.
> [!TIP]
> If you are using a local file then it should be in same directory as the directory from where program is executed.
## Upcoming Feature and Changes
- ✅️ *~~TUI menu.~~* - Done
- ✅️ *~~Video input from URL.~~* - Done
- [ ] Selecting Video Resolution.
- ✅️ *~~Whole FileSystem Access.~~* - Done
- ✅️ *~~New and Enhanced Menu.~~* - Done
- [ ] Windows Support.
- [ ] Youtube Video Support.
- [ ] Virtual Audio Support.
- [ ] Android as Source Support.
