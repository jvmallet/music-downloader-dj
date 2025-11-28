# 🎵 Music Downloader for DJs  
*A reliable multi-folder YouTube/SoundCloud audio downloader powered by `yt-dlp`.*

This project is designed for DJs and music collectors who frequently download tracks and want an organized, automated workflow.  
It automatically assigns downloads to unique folders (e.g., `Musicas Baixadas`, `Musicas Baixadas 2`, `Musicas Baixadas 3`...) and uses a lock-file system to prevent conflicts when multiple instances run simultaneously.

---

## ✨ Features

- 🎧 **Automatic Folder Assignment**  
  Creates new folders as needed and guarantees that each download session uses an exclusive directory.

- 🔒 **Lock System to Prevent Conflicts**  
  A `.downloader.lock` file ensures no two processes write to the same folder.

- 🎶 **High-Quality Audio Extraction**  
  Downloads the best available audio and converts it to **320kbps MP3** using FFmpeg.

- 🍪 **Cookie-Based Authentication**  
  Supports `youtube_cookies.txt` to bypass common YouTube 403 Forbidden issues.

- 📂 **Organizes Your Library Automatically**  
  Everything is saved neatly and consistently without overwriting previous sessions.

---

## 🚀 How to Use

Using the downloader is extremely simple:

1. Run the script:

```bash
python downloader.py
```

2. When prompted, paste **any YouTube or SoundCloud link**:

* 🎵 Single tracks
* 🎧 Full playlists
* 🌀 DJ mixes

3. The tool will automatically:

* Detect or create a folder like `Musicas Baixadas`, `Musicas Baixadas 2`, etc.
* Lock the folder so no other instance writes to it
* Download the audio in the best possible quality
* Convert everything to **320kbps MP3**
* Save the final files directly inside the chosen folder

No extra configuration needed — just run, paste the link, and the music appears in the folder.


## 📦 Requirements

- Python **3.8+**
- [`yt-dlp`](https://github.com/yt-dlp/yt-dlp)
- **FFmpeg** installed on your system  
- A valid `youtube_cookies.txt` file (optional, but recommended)

Install dependencies:

```bash
pip install -r requirements.txt
