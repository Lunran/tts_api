import json

from flask import (
    Flask, request, send_file
)
from scipy.io.wavfile import write

from tsukuyomichan_talksoft.tsukuyomichan_talksoft import TsukuyomichanTalksoft


FS = 24000
GACHA = 0
WAV_FILENAME = "./tmp.wav"

tsukuyomichan_talksoft = TsukuyomichanTalksoft(model_version='v.1.2.0')

app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False


@app.route('/tts', methods=['POST'])
def tts():
    if request.method == 'POST':
        text = request.json['text']
        wav = tsukuyomichan_talksoft.generate_voice(text, GACHA)
        write(WAV_FILENAME, FS, wav)
        return send_file(WAV_FILENAME, mimetype="audio/wav", as_attachment=True)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8002, debug=True)
