import os
import threading
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

def download_video(url, output_path, video_progress_bar, output_label):
    global download_percentage
    ydl_opts = {
        'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s'),
        'format': 'bestvideo+bestaudio/best',
        'merge_output_format': 'mp4',
        'postprocessors': [{'key': 'FFmpegVideoConvertor', 'preferedformat': 'mp4'}],
        'progress_hooks': [lambda d: update_video_progress(d, video_progress_bar, output_label)],
    }
    try:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(url, download=False)  # Get video info
            video_title = info_dict.get('title', 'Unknown Title')
            output_label.text = f"Downloading: {video_title}"  # Update UI with video title
            ydl.download([url])
    except Exception as e:
        output_label.text = f"Error during download: {e}"

def update_video_progress(d, video_progress_bar, output_label):
    global download_percentage
    if d['status'] == 'downloading':
        total_bytes = d.get('total_bytes', 1)
        downloaded_bytes = d.get('downloaded_bytes', 0)
        progress = downloaded_bytes / total_bytes * 100
        download_percentage = progress
        video_progress_bar.value = download_percentage

    elif d['status'] == 'finished':
        # When download is finished, set the progress to 100% and display "Done"
        download_percentage = 100
        video_progress_bar.value = download_percentage
        output_label.text = "Done!"

class YTDownloaderApp(App):
    def build(self):
        # Set window size
        Window.size = (600, 400)
        layout = BoxLayout(orientation='vertical', spacing=20, padding=40, size_hint=(None, None), pos_hint={'center_x': 0.5, 'center_y': 0.5})
        layout.size_hint = (0.6, 0.6)  # Size of the layout, change as needed
        layout.pos_hint = {'center_x': 0.5, 'center_y': 0.5}  # Center the layout

        # Input field for YouTube Video URL
        self.url_input = TextInput(hint_text="Enter YouTube Video URL", multiline=False, size_hint_y=None, height=40)
        layout.add_widget(self.url_input)

        # Download Button
        self.download_button = Button(text="Download Video", size_hint_y=None, height=40)
        self.download_button.bind(on_press=self.start_download)
        layout.add_widget(self.download_button)
        
        self.output_label = Label(size_hint_y=None, height=40, text="Download Progress:")
        layout.add_widget(self.output_label)

        # Video Progress Bar (for individual video progress)
        self.video_progress_bar = ProgressBar(value=0, max=100, size_hint_y=None, height=30)
        layout.add_widget(Label(text="Current Video Progress", size_hint_y=None, height=30))
        layout.add_widget(self.video_progress_bar)

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
        # Set the output directory to the Desktop
        if os.name == "nt":
            desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
        else:
            desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")

        storage_path = os.path.join(desktop_path, "YT Downloader")
        os.makedirs(storage_path, exist_ok=True)

        # Start the video download
        download_video(link, storage_path, self.video_progress_bar, self.output_label)

if __name__ == "__main__":
    YTDownloaderApp().run()
