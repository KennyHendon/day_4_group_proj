#album

def my_album(artist_name, album_name):
    """display and store the music album's info"""
    music_album = {'artist': artist_name, 'album': album_name}
    return music_album


my_album('the beatles', 'abbey road')
thealbum = my_album

print(thealbum)

