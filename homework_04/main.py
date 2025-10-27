from files import AudioFile
from files import VideoFile
from files import PhotoFile
from storage import LocaleStorage, CloudStorage

locale_storage = LocaleStorage()
cloud_storage = CloudStorage()

print('---------Photo--------------')
photo = PhotoFile(
    "Фото",
    123,
    "Postgres",
    locale_storage,
    100,
    200,
    "Canon"
)
photo.get_metadata()
photo.save()
photo.resize(1920, 1080)
photo.delete()

print('---------Audio--------------')
song = AudioFile(
    "music.mp3",
    4000,
    "Alice",
    locale_storage,
    180,
    320,
    "mp3"
)
song.save()
song.convert("aac")
song.move(cloud_storage)

print('---------Video--------------')
video = VideoFile(
    "movie.mp4",
    100000,
    "Bob",
    locale_storage,
    "1920x1080",
    30
)
video.save()
video.extract_frame()
