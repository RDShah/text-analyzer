import lyricscorpora as lc
import sys

for artist_name in ['Logic']:
	artist = lc.Artist(artist_name)
	for album in artist.get_album_list():
		print('\nalbum:',album)
		# if album.name in ['808s & Heartbreak','Graduation','Late Registration','My Beautiful Dark Twisted Fantasy','The College Dropout','Watch The Throne']:
		# 	print('skipping')
		# 	continue
		with open(artist_name+' - '+album.name+'.txt','w') as file:
			song_list = album.get_song_list()
			for song in song_list:
				print('song:',song)
				lyrics = lc.get_lyrics(song)
				try:
					file.write(lyrics)
				except:
					print('Bad char encountered')
					file.write(str(lyrics.encode(sys.stdout.encoding, errors='replace')))
			file.close()