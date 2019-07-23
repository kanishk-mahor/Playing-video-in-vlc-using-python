import vlc

path1 = 'first_file_name.file _extention'           #video1.mp4
path2 = 'second_file_name.file _extention'          #video2.mp4

Instance = vlc.Instance('--input-repeat=-1', '--fullscreen', '--mouse-hide-timeout=0')

MediaList = Instance.media_list_new()
MediaList.add_media(Instance.media_new(path1))
MediaList.add_media(Instance.media_new(path2))

list_player = Instance.media_list_player_new()
list_player.set_media_list(MediaList)

list_player.next()
list_player.set_playback_mode(vlc.PlaybackMode.loop)
list_player.play()

