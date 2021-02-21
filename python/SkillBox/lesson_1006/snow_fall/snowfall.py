import simple_draw as sd

_snow_params = []


# На основе кода из практической части реализовать снегопад:
# - создать списки данных для отрисовки N снежинок
# - нарисовать падение этих N снежинок
# - создать список рандомных длинн лучей снежинок (от 10 до 100) и пусть все снежинки будут разные
def draw_flake(color=sd.COLOR_WHITE):
    sd.start_drawing()
    for flake in _snow_params:
        x, y, length = flake
        point = sd.get_point(x, y)

        sd.snowflake(center=point, length=length, color=color)
    sd.finish_drawing()


#  создать_снежинки(N) - создает N снежинок
def create_flake(count_flake):
    global _fallen_flake
    _fallen_flake = []
    global _snow_params
    _snow_params = []
    for _ in range(count_flake):
        _snow_params.append([sd.random_number(0, 1000), sd.random_number(500, 600), sd.random_number(20, 40)])


def move_flake():
    global _snow_params

    for key, flake in enumerate(_snow_params):
        if _snow_params[key][1] <= 0:
            continue

        _snow_params[key][0] += sd.random_number(-25, 25)
        _snow_params[key][1] -= sd.random_number(1, 25)




#  номера_достигших_низа_экрана() - выдает список номеров снежинок, которые вышли за границу экрана
#  удалить_снежинки(номера) - удаляет снежинки с номерами из списка
