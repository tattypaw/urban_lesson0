import time
class Video:
    def __init__(self, title, duration, time_now = 0, adult_mode = False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.age = age
        self.password = hash(password)

class UrTube:
    users = []
    videos = []
    current_user = None

    def __init__(self):
        self.users = UrTube.users
        self.videos = UrTube.videos
        self.current_user = UrTube.current_user

    def log_in(self, nickname, password):
        for user in UrTube.users:
            if nickname == user.nickname and hash(password) == user.password:
                self.current_user = user.nickname

    def register(self, nickname, password,age):
        find = False
        for user in UrTube.users:
            if nickname == user.nickname:
                find = True
                break
        if find:
            print(f'Пользователь {nickname} уже существует')
        else:
            self.current_user = nickname
            UrTube.users.append(User(nickname, password, age))

    def log_out(self):
        self.current_user = None

    def add(self, *args):
        for arg in args:
            find = False
            for video in UrTube.videos:
                if arg.title == video.title:
                    find = True
            if not find:
                UrTube.videos.append(arg)

    def get_videos(self, keyword):
        find = []
        for video in UrTube.videos:
            if keyword.lower() in video.title.lower():
                find.append(video.title)
        print(find)

    def watch_video(self, keyword):
        if self.current_user != None:
            for video in UrTube.videos:
                if keyword.lower() in video.title.lower():
                    age = 0
                    for user in UrTube.users:
                        if self.current_user == user.nickname:
                            age = user.age
                    if age < 18:
                        print('Вам нет 18 лет, пожалуйста покиньте страницу')
                    else:
                        for i in range(video.time_now, video.duration):
                            time.sleep(1)
                            print(i + 1, end=' ')
                        time.sleep(1)
                        print('Конец видео')
        else:
            print('Войдите в аккаунт, чтобы смотреть видео')


ur = UrTube()
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
ur.watch_video('Лучший язык программирования 2024 года!')
