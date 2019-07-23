import vlc

vidpath = 'filename.file extention'  # for example vidpath = 'python_tutorial.mp4'
#define VLC instance
instance = vlc.Instance('--input-repeat=-1', '--fullscreen', '--mouse-hide-timeout=0')

#Define VLC player
player=instance.media_player_new()

#Define VLC media
media=instance.media_new(vidpath)

#Set player media
player.set_media(media)

#Play the media
player.play()
