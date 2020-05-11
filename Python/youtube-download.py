# Author: Jean J Barros
# Github: https://github.com/jjeanjacques10/

# --- Baixar vídeos no youtube ---
from __future__ import unicode_literals
import youtube_dl

ydl_opts = {}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download(['https://youtu.be/lhfhS1NfrMo'])