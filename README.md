# 🎥 YouTube Downloader App

This is a Kivy-based desktop application that allows users to download YouTube videos and entire playlists. The application has two sections:
1. **Single Video Download** 
2. **Playlist Download** 

Both sections are neatly separated in the app window for ease of use.

## ✨ Features

- 📥 Download single videos from YouTube by entering the video URL.
- 📃 Download complete playlists by entering the playlist URL.
- 📊 Separate progress bars for both playlist and single video downloads.
- ⚙️ Progress indicator for the currently downloading video in both modes.
- 📂 Downloads are saved to a folder named `YT Downloader` on your desktop.

## 🛠️ Technologies Used
**Python Libraries**
- **Kivy**: For the graphical user interface (GUI).
- **Pytube**: To handle playlists and retrieve video URLs.
- **yt-dlp**: For downloading videos and playlists.
- **Colorama**: Provides colored terminal output (though not used in the GUI).

## 🚀 Installation

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/your-username/yt-downloader.git
    cd yt-downloader
    ```

2. **Install Dependencies**:
    ```bash
    pip install kivy pytube colorama yt-dlp
    ```

3. **Run the Application**:
    ```bash
    python merger.py
    ```

## 💡 How It Works

### Main Sections

The application consists of two main sections:

1. **Single Video Download**:
    - Enter the YouTube video URL in the input field.
    - Click "Download Video" to start the download.
    - The progress bar and output label will show the status of the video download.

2. **Playlist Download**:
    - Enter the YouTube playlist URL in the input field.
    - Click "Download Playlist" to start downloading all videos in the playlist.
    - A playlist progress bar shows the progress for the entire playlist.
    - Another progress bar shows the status of the currently downloading video.

### 📊 Progress Bars
- **Current Video Progress**: Tracks the percentage of the ongoing video download.
- **Playlist Progress**: Tracks the overall progress of the playlist download (if downloading a playlist).


## 📝 Usage

1. **Single Video Download**:
    - Copy the YouTube video URL.
    - Paste it into the **Single Video** section input field.
    - Click the "Download Video" button to start the download.
    - Track the download progress via the progress bar.

2. **Playlist Download**:
    - Copy the YouTube playlist URL.
    - Paste it into the **Playlist** section input field.
    - Click the "Download Playlist" button to start downloading the entire playlist.
    - Track both the playlist progress and the currently downloading video’s progress via the two progress bars.

## 🛑 Known Issues

- The app may temporarily freeze when handling large playlists, depending on the number of videos and your internet speed.
- If the URL is invalid, restricted, or the connection fails, the download will not proceed, and an error message will be displayed.

## 🌟 Future Improvements

- Add support for selecting specific videos from a playlist to download.
- Provide video quality options for users to choose before downloading.
- Improve performance for handling large playlists.
- Add a cancel button to stop an ongoing download.

## 📜 License

This project is licensed under the MIT License.


