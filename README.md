⁶# CamSimulate
- CamSimulate is a python application which stream Videos from local file or from a URL to video devices of your device.
- It uses v4l2loopback for creating a Virtual Video device if no physical device is available.
- It uses ffmpeg to stream the selected video to the video device either from local file or a URL.

> [!NOTE]
> It works only for UNIX-like operating system.
## Usage
1. ### Clone this repository.
   ```
   git clone https://github.com/MK-1407/CamSimulate.git
   ```
2. ### Install v4l2loopback.
   ```
   sudo apt install v4l2loopback-dkms
   ```
3. ### Execute the main.py file.
   ```
   python3 main.py
   ```
4. ### Choose Video Device.
5. ### Choose file or Choose URL.
> [!WARNING]
> The URL of the video should be direct URL not of the page where you saw video. 
> example.com/video_44.mp4 ✅️  
> youtube.com/this-awesome-video ❌️
6. ### Use the Camera on any site you want.
> [!TIP]
> If you are using a local file then it should be in same directory as the directory from where program is executed.
## Upcoming Feature and Changes
- [x] TUI menu.
- [x] Video input from URL.
- [ ] Selecting Video Resolution.
- [ ] Whole FileSystem Access.
- [ ] New and Enhanced Menu.
- [ ] Windows Support.
- [ ] Youtube Video Support.
