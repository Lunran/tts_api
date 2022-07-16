# What's this?

- Flask API to use TTS engine
- Supposed to be used with https://github.com/Lunran/sts_cli


# Prerequisites

- Ubuntu 18.04.5 LTS


# How to setup

- Get source codes
  - $ git clone https://github.com/Lunran/tts_api.git
  - $ cd tts_api
- Install modules
  - $ python3 -m venv venv
  - $ . venv/bin/activate
  - $ pip install --upgrade pip
  - $ pip install -r requirements.txt
- Setup tsukuyomichan talksoft
  - (for macos) $ brew install freetype
  - (for ubuntu) $ sudo apt install libfreetype6-dev libasound2-dev
  - $ git clone https://github.com/shirowanisan/tsukuyomichan-talksoft.git
  - $ mv tsukuyomichan-talksoft tsukuyomichan_talksoft
  - $ touch tsukuyomichan_talksoft/__init__.py
  - $ vi tsukuyomichan_talksoft/tsukuyomichan_talksoft.py
    - (change the following line)
    - from tts_config import TTSConfig -> from .tts_config import TTSConfig
  - $ vi tsukuyomichan_talksoft/tts_config.py
    - (change the following line if necessary)
    - device = 'cuda' if torch.cuda.is_available() else 'cpu'


# How to use

- $ python main.py
- $ curl -X POST -H "Content-Type: application/json" -d '{"text":"こんにちは"}' "http://localhost:5000/tts"
