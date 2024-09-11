# 🎥 YouTube Playlist Downloader

This Python-based app allows you to download entire YouTube playlists with video progress tracking. The app uses Kivy for the GUI and PyTube for playlist handling, along with `yt-dlp` to download the videos.

## Features 🌟

- Downloads entire YouTube playlists. 🎬
- Shows overall progress and per-video progress. 📊
- Cross-platform support (Windows, macOS, and Linux). 🌐
- Customizable file output path (set to Desktop by default). 🖥️
- Supports best video and audio quality. 🎥🔊

## Requirements ⚙️

- **Python 3.7+** 🐍
- **Kivy** 🌟
- **yt-dlp** 🎥
- **Pytube** 📺
- **Colorama** 🌈
- **FFmpeg** 🎞️

### FFmpeg Setup 🎬

This application requires FFmpeg for merging audio and video streams. Follow the steps below to set up FFmpeg:

1. **Download FFmpeg:**
   - [Download FFmpeg (Windows)](https://ffmpeg.org/download.html)
   - Unzip this folder and place it in your OS disk space (usually `C:` drive). 📦

2. **Add FFmpeg to PATH:**
   - Go to the extracted FFmpeg folder.
   - Inside the folder, locate the `bin` folder (where the FFmpeg executables reside).
   - Add the path of this `bin` folder to your system's environment variables.

   #### Steps to add to environment variables on Windows:

   - Right-click **This PC** or **My Computer** and select **Properties**. 🖱️
   - Select **Advanced system settings** from the left sidebar. ⚙️
   - Click the **Environment Variables** button. 🔧
   - In the **System variables** section, find the `Path` variable and click **Edit**. 📝
   - Add the full path to the `bin` folder, for example: `C:\ffmpeg\bin`.
   - Click **OK** to close all windows. ✅

   After this, FFmpeg should be accessible globally on your system, and the app can properly merge video and audio files. 🎉

## Installation 🛠️

1. **Clone the repository**:
    ```bash
    git clone https://github.com/your-username/YouTube-Playlist-Downloader.git
    cd YouTube-Playlist-Downloader
    ```

2. **Install required Python packages**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Ensure FFmpeg is set up as described above**. 🔄

4. **Run the application**:
    ```bash
    python main.py
    ```

## Usage 🚀

1. Enter the URL of a YouTube playlist into the text input field. 🌐
2. Click the "Download Playlist" button or press **Enter** to start the download process. 📥
3. Track the progress via the overall playlist and individual video progress bars. 📊
4. Downloaded videos will be saved to a folder on your Desktop named `YT Downloader`. 🗂️

## License 📜

This project is licensed under the MIT License. 🏅

## Acknowledgements 🙌

- [Kivy](https://kivy.org/#home) - For building the GUI. 💻
- [yt-dlp](https://github.com/yt-dlp/yt-dlp) - For downloading YouTube videos. 🎥
- [Pytube](https://pytube.io/en/latest/) - For handling YouTube playlists. 📺
