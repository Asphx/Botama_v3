import os
import sys

class SystemInteraction:
    def __init__(self):
        pass

    @staticmethod
    def download_and_store_song(song, name):
        """
        This method take an url as a parameters, and optionally a name for the song
        then use youtube-dl to download it and store it in /home/pi/Botama/bot/song/ folder with default or given name
        """
        try:
            os.system('youtube-dl {} -x --audio-format mp3 --audio-quality 0 --restrict-filenames --no-playlist --verbose -o "{}.%(ext)s"'.format(song, name))
            os.system('mv ./{}.mp3 /home/ubuntu/Workspace/Botama_v3/bot/song'.format(name))
            return 'Done'
        except Exception as e :
            print(e)
            return 'Done'


if len(sys.argv) > 1 :
    if sys.argv[1] and sys.argv[1] == 'dl-yt':
        if sys.argv[3]:
            SystemInteraction.download_and_store_song(sys.argv[2], sys.argv[3])
