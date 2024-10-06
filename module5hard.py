import hashlib
import time

class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = User.hash_password(password)  # Вызов статического метода через имя класса
        self.age = age

    def hash_password(password):
        return hashlib.sha256(password.encode()).hexdigest()

class Video:
    def __init__(self, title, duration, adult_mode=False):
        self.title = title
        self.duration = duration
        self.adult_mode = adult_mode

class UrTube:
    def __init__(self, users, videos, current_user):
        self.users = users
        self.videos = videos
        self.current_user = current_user

    def log_in(self, nickname, password):
        for user in self.users:
            if user.nickname == nickname and user.password == User.hash_password(password):
                self.current_user = user
                print(f"Пользователь {nickname} вошел в аккаунт.")
                return
        print("Неверный логин или пароль.")

    def register(self, nickname, password, age):
        if any(user.nickname == nickname for user in self.users):
            print(f"Пользователь {nickname} уже существует")
            return
        new_user = User(nickname, password, age)
        self.users.append(new_user)
        self.current_user = new_user
        print(f"Пользователь {nickname} зарегистрирован и автоматически вошел в аккаунт.")

    def log_out(self):
        self.current_user = None
        print("Вы вышли из аккаунта.")

    def add(self, *videos):
        for video in videos:
            if not any(v.title == video.title for v in self.videos):
                self.videos.append(video)

    def get_videos(self, search_word):
        search_word_lower = search_word.lower()
        return [video.title for video in self.videos if search_word_lower in video.title.lower()]

    def watch_video(self, title):
        if not self.current_user:
            print("Войдите в аккаунт, чтобы смотреть видео")
            return
        for video in self.videos:
            if video.title == title:
                if video.adult_mode and self.current_user.age < 18:
                    print("Вам нет 18 лет, пожалуйста покиньте страницу")
                    return
                print(f"Начинаем просмотр видео: {video.title}")
                for second in range(video.duration):
                    print(f"Смотрим {video.title}: {second + 1} сек.")
                    time.sleep(1)  # Пауза в 1 секунду
                print("Конец видео")
                return
        print("Видео не найдено")

# Инициализация
users = []
videos = []
current_user = None
ur = UrTube(users, videos, current_user)

# Создание видео
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Несуществующее видео')