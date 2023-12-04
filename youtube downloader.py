from pytube import YouTube

link = input("your youtube video url here: ")

pirate_at_youtube = YouTube(link)

#print(pirate_at_youtube.title)
#print(pirate_at_youtube.thumbnail_url)

video_streams = pirate_at_youtube.streams           #.filter(only_audio=True) can also be used
videos = list(enumerate(video_streams))

for i in videos:
    print(i)

chosen_stream = int(input("enter your desired stream number: "))
video_streams[chosen_stream].download()

print("download complete")

#furthermore, from pytube import Playlist is usable the same way

