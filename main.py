import os
import threading
import time
from pytube import Playlist
from colorama import init
import yt_dlp as youtube_dl
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.progressbar import ProgressBar
from kivy.clock import Clock
from kivy.core.window import Window

init(autoreset=True)

# Variable to store the video progress percentage
download_percentage = 0

def download_video(url, output_path, index, video_progress_bar, output_label):
    global download_percentage
    ydl_opts = {
        'outtmpl': os.path.join(output_path, f'{index:03d} - %(title)s.%(ext)s'),
        'format': 'bestvideo+bestaudio/best',
        'merge_output_format': 'mp4',
        'postprocessors': [{'key': 'FFmpegVideoConvertor', 'preferedformat': 'mp4'}],
        'progress_hooks': [lambda d: update_video_progress(d, video_progress_bar)],
    }
    try:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(url, download=False)  # Get video info
            video_title = info_dict.get('title', 'Unknown Title')
            output_label.text = f"Downloading: {video_title}"  # Update UI with video title
            ydl.download([url])
    except Exception as e:
        return f"Error during download: {e}"

def update_video_progress(d, video_progress_bar):
    global download_percentage
    if d['status'] == 'downloading':
        total_bytes = d.get('total_bytes', 1)
        downloaded_bytes = d.get('downloaded_bytes', 0)
        progress = downloaded_bytes / total_bytes * 100
        download_percentage = progress

def playlist_downloader(link, output_label, playlist_progress_bar, video_progress_bar):
    def make_alpha_numeric(string):
        return ''.join(char for char in string if char.isalnum())

    try:
        yt_playlist = Playlist(link)
    except Exception as e:
        output_label.text = f"Failed to load playlist: {e}"
        return

    if os.name == "nt":
        desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
        storage_path = os.path.join(desktop_path, "YT Downloader")
    else:
        desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
        storage_path = os.path.join(desktop_path, "YT Downloader")

    folderName = make_alpha_numeric(yt_playlist.title)
    os.makedirs(os.path.join(storage_path, folderName), exist_ok=True)

    total_videos = len(yt_playlist.video_urls)
    for index, video_url in enumerate(yt_playlist.video_urls, start=1):
        result = download_video(video_url, os.path.join(storage_path, folderName), index, video_progress_bar, output_label)
        if result:
            output_label.text = f"Failed to download {video_url}: {result}"
        
        # Update playlist progress bar
        playlist_progress_bar.value = (index / total_videos) * 100
        playlist_progress_bar.max = total_videos
        playlist_progress_bar.text = f"{index}/{total_videos} videos downloaded"

        # Update output label with the download count
        output_label.text = f"Downloaded {index}/{total_videos} videos"

    output_label.text = f"All videos downloaded successfully! ({total_videos}/{total_videos})"

class YTDownloaderApp(App):
    def build(self):
        # Set window size
        Window.size = (600, 400)
        
        # Main layout with vertical alignment (BoxLayout)
        layout = BoxLayout(orientation='vertical', spacing=20, padding=40, size_hint=(None, None), pos_hint={'center_x': 0.5, 'center_y': 0.5})

        # Center all items in the middle
        layout.size_hint = (0.6, 0.6)  # Size of the layout, change as needed
        layout.pos_hint = {'center_x': 0.5, 'center_y': 0.5}  # Center the layout

        # Input field for YouTube Playlist URL
        self.url_input = TextInput(hint_text="Enter YouTube Playlist URL", multiline=False, size_hint_y=None, height=40)
        layout.add_widget(self.url_input)

        # Download Button
        self.download_button = Button(text="Download Playlist", size_hint_y=None, height=40)
        self.download_button.bind(on_press=self.start_download)
        layout.add_widget(self.download_button)

        # Output Label for download logs
        self.output_label = Label(size_hint_y=None, height=40, text="Download Progress:")
        layout.add_widget(self.output_label)

        # Playlist Progress Bar (for overall progress)
        self.playlist_progress_bar = ProgressBar(value=0, max=100, size_hint_y=None, height=30)
        layout.add_widget(Label(text="Overall Playlist Progress", size_hint_y=None, height=30))
        layout.add_widget(self.playlist_progress_bar)

        # Video Progress Bar (for individual video progress)
        self.video_progress_bar = ProgressBar(value=0, max=100, size_hint_y=None, height=30)
        layout.add_widget(Label(text="Current Video Progress", size_hint_y=None, height=30))
        layout.add_widget(self.video_progress_bar)

        # Bind the Enter key to start the download
        self.url_input.bind(on_text_validate=self.start_download)

        # Start a clock to update the video progress bar every 0.5 seconds
        Clock.schedule_interval(self.update_video_bar, 0.5)

        return layout

    def update_video_bar(self, dt):
        global download_percentage
        # Update the video progress bar with the current download percentage
        self.video_progress_bar.value = download_percentage

    def start_download(self, instance):
        link = self.url_input.text
        if link:
            # Start the download process in a new daemon thread (prevents crashes on app exit)
            download_thread = threading.Thread(target=self.run_downloader, args=(link,))
            download_thread.daemon = True  # Ensures thread exits when the app closes
            download_thread.start()
        else:
            self.output_label.text = "Please enter a valid URL."

    def run_downloader(self, link):
        playlist_downloader(link, self.output_label, self.playlist_progress_bar, self.video_progress_bar)

if __name__ == "__main__":
    YTDownloaderApp().run()
