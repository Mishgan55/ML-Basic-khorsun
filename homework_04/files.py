from datetime import datetime


class MediaFile:

  def __init__(self, name, size, owner, storage):
    self.name = name,
    self.size = size,
    self.created_date = datetime.now(),
    self.owner = owner
    self.storage = storage

  def get_metadata(self):
    """Тут должны возвращаться какие-то данные"""
    raise NotImplementedError("Необходима реализация в классе наследнике")

  def save(self):
    self.storage.save(self)

  def update(self):
    self.storage.update(self)

  def delete(self):
    self.storage.delete(self)

  def move(self, new_storage):
    """Переместить файл в другое хранилище."""
    self.storage.delete(self)
    new_storage.save(self)
    self.storage = new_storage


class PhotoFile(MediaFile):
  def __init__(self, name, size, owner, storage, width, height, camera_model):
    super().__init__(name, size, owner, storage)
    self.width = width
    self.height = height
    self.camera_model = camera_model

  def get_metadata(self):
    return {
      "width": self.width,
      "height": self.height,
      "camera_model": self.camera_model
    }

  def resize(self, new_width, new_height):
    print(
        f"Изменяем размер {self.name} с {self.width}x{self.height} до {new_width}x{new_height}")
    self.width = new_width
    self.height = new_height


class VideoFile(MediaFile):
  def __init__(self, name, size, owner, storage, resolution, fps):
    super().__init__(name, size, owner, storage),
    self.resolution = resolution,
    self.fps = fps

  def get_metadata(self):
    return {
      'resolution': self.resolution,
      'fps': self.fps
    }

  def extract_frame(self):
    print(f"Извлечение картинки, качеством: {self.resolution}")


class AudioFile(MediaFile):
  def __init__(self, name, size, owner, storage, duration, bitrate, codec):
    super().__init__(name, size, owner, storage)
    self.duration = duration
    self.bitrate = bitrate
    self.codec = codec

  def get_metadata(self):
    return {
      "duration": self.duration,
      "bitrate": self.bitrate,
      "codec": self.codec
    }

  def convert(self, new_codec):
    print(f"Конвертация аудио {self.name} из {self.codec} в {new_codec}")
    self.codec = new_codec
