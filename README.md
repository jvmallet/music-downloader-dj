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

- 💤 **Human-Like Download Behavior**  
  Optional rate limiting and sleep intervals to reduce throttling.

- 📂 **Organizes Your Library Automatically**  
  Everything is saved neatly and consistently without overwriting previous sessions.

---

## 📦 Requirements

- Python **3.8+**
- [`yt-dlp`](https://github.com/yt-dlp/yt-dlp)
- **FFmpeg** installed on your system  
- A valid `youtube_cookies.txt` file (optional, but recommended)

Install dependencies:

```bash
pip install -r requirements.txt

