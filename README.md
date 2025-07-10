# WaveBrowse

**WaveBrowse** is a lightweight, native web browser built with **PyQt6** for the user interface and **CEF Python (Chromium Embedded Framework)** for real web rendering power.

Forget old-school `QWebView` — WaveBrowse embeds full **Chromium**, giving you modern HTML5, CSS, JS, WebGL, YouTube, and DevTools support in a native desktop app.

---

## Features

- Native UI built with PyQt6
- Embedded **real Chromium** using CEF Python
- Loads any website, supports full JavaScript
- Toggle DevTools (F12) like Chrome
- Resize-aware browser rendering
- Super minimal and fast

---

## Requirements

- **Python 3.10** (❗ Required — CEF Python does not support 3.11+)
- `PyQt6`
- `cefpython3==66.1`

---

## 🛠 Installation

### 1. Install Python 3.10 (if not already)

Download from [python.org](https://www.python.org/downloads/release/python-3109/)

### 2. Clone this repository

```bash
git clone https://github.com/Waves-Lab-Offical/WaveBrowse.git
cd WaveBrowse
````

### 3. Create a virtual environment

```bash
python3.10 -m venv .venv
.venv\Scripts\activate   # Windows
# or
source .venv/bin/activate  # Linux/macOS
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

---

## Running WaveBrowse

```bash
python main.py
```

---

## ⌨ Shortcuts

| Key      | Action          |
| -------- | --------------- |
| `F12`    | Toggle DevTools |
| `Alt+F4` | Quit WaveBrowse |

---

## Development Notes

* You **must use Python 3.10** due to `cefpython3` compatibility.
* For advanced usage, you can embed `CefWidget` inside tab widgets or toolbars.
* Works on Windows; Linux/macOS support may require minor path tweaks.

---

## Project Structure

```
WaveBrowse/
├── main.py              # Main app launcher
├── requirements.txt     # Required Python packages
├── README.md            # This file
├── icons/               # (Optional) Custom icons
└── .venv/               # Your Python 3.10 virtual environment
```

---

## License

MIT License
© 2025 [WavesLab](https://github.com/Waves-Lab-Offical)

You are free to fork, remix, and build your own custom browser from this base.
Just Give credits

---

## Credits

* [PyQt6](https://pypi.org/project/PyQt6/)
* [CEF Python](https://github.com/cztomczak/cefpython)

---

## Made with passion by Arham & WavesLab

> "Why settle for Chrome when you can build your own?"

```