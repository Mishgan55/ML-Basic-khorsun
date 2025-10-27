class BaseStorage:
  text_exception_if_not_implemented = "Необходима реализация в классе наследнике"

  def save(self, media_file):
    """Сохранение"""
    raise NotImplementedError(BaseStorage.text_exception_if_not_implemented)

  def update(self, media_file):
    """Обновление"""
    raise NotImplementedError(BaseStorage.text_exception_if_not_implemented)

  def delete(self, media_file):
    """Удаление"""
    raise NotImplementedError(BaseStorage.text_exception_if_not_implemented)


class LocaleStorage(BaseStorage):

  def save(self, media_file):
    print(f"Сохраняем {media_file.name} на локальном диске...")

  def update(self, media_file):
    print(f"Обновляем {media_file.name} на локальном диске...")

  def delete(self, media_file):
    print(f"Удаляем {media_file.name} на локальном диске...")


class CloudStorage(BaseStorage):

  def save(self, media_file):
    print(f"Сохраняем {media_file.name} на облачном диске...")

  def update(self, media_file):
    print(f"Обновляем {media_file.name} на облачном диске...")

  def delete(self, media_file):
    print(f"Удаляем {media_file.name} на облачном диске...")
