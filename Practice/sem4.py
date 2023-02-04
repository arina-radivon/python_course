from operator import add


class Color:
    END = '\033[0'
    START = '\033[1;38;2'
    MOD = 'm'
    MAX_LEVEL = 255
    MIN_LEVEL = 0

    def __init__(self, red_level, green_level, blue_level):
        self.rgb = (red_level, green_level, blue_level)
        self.__validate_level(red_level)
        self.__validate_level(green_level)
        self.__validate_level(blue_level)

    def __repr__(self):
        return (f'{self.START};{self.rgb[0]};{self.rgb[1]};'
                f'{self.rgb[2]}{self.MOD}●{self.END}{self.MOD}')

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.rgb == other.rgb
        return False

    def __add__(self, other):
        new_rgb = self.__class__(*map(add, self.rgb, other.rgb))
        # * перед map распаковывает значения 1ое, 2е, 3е и отдельно работает
        return new_rgb

    def __hash__(self):
        return hash(self.rgb)

    def __rmul__(self, c):
        return self.__class__(
            self._change_contrast(c, self.rgb[0]),
            self._change_contrast(c, self.rgb[1]),
            self._change_contrast(c, self.rgb[2]),
        )

    def _change_contrast(self, c, level):
        cl = -256*(1-c)
        F = 259*(cl + 255)/(255*(259 - cl))
        return int(F * (level - 128) + 128)

    def __validate_level(self, level):
        if level > self.MAX_LEVEL or level < self.MIN_LEVEL:
            raise ValueError(f'lev from {self.MIN_LEVEL} to {self.MAX_LEVEL}')


if __name__ == '__main__':
    red = Color(255, 0, 0)
    green = Color(0, 255, 0)
    print(red)
    print(red == green)
    print(red == 3)
    print(red + green)

    orange1 = Color(255, 165, 0)
    orange2 = Color(255, 165, 0)
    color_list = [orange1, red, green, orange2]
    print(set(color_list))
    # set принимает hash-объекты -> определили его (возвращает число)

    cont = 0.8
    print(cont * red)
