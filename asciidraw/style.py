import math
from typing import Iterable
from warnings import warn

try:
    import colorama  # noqa: F401
    from termcolor import colored
except ImportError:
    warn(
        "colorama and termcolor are required for colored ASCII rendering",
        stacklevel=2,
    )

    def colored(text, color):  # noqa: ARG001
        return text


class Style:
    def __init__(self, style=None, color=None, wrap=lambda x: x, **kwargs):  # noqa: ARG002
        if color is None:
            self.color = lambda x: x
        else:
            self.color = lambda x: colored(x, color)
        # first custom wrap, then color
        self.wrap = lambda x: self.color(wrap(x))


class LineStyle(Style):
    def __init__(self, style=None, begin=None, end=None, **kwargs):
        super().__init__(style=style, **kwargs)

        self.index = -1
        self.begin = begin
        self.end = end

    def next(self, dirx, diry):
        self.index += 1
        return (math.atan2(diry, dirx) + math.pi) % (2 * math.pi)


class SimpleLineStyle(LineStyle):
    def __init__(self, style=None, terminate=True, **kwargs):
        super().__init__(**kwargs)

        if not isinstance(style, Iterable):
            style = [style]
        self.style = style
        self.terminate = terminate

    def get(self, index):
        if self.style is not None:
            s = self.style[index % len(self.style)]
            if s is not None:
                return s
            if self.terminate:
                self.style = None
        return None

    def next(self, dirx, diry):
        super().next(dirx, diry)
        return self.get(self.index)


class Cross(LineStyle):
    def __init__(
        self,
        vert=None,
        horz=None,
        left=None,
        up=None,
        right=None,
        down=None,
        **kwargs,
    ):
        super().__init__(**kwargs)

        if vert is not None:
            if not isinstance(vert, Iterable):
                vert = [vert]
            down = vert
            up = vert
        if horz is not None:
            if not isinstance(horz, Iterable):
                self.horz = [horz]
            right = horz
            left = horz

        self.left = SimpleLineStyle(style=left)
        self.right = SimpleLineStyle(style=right)
        self.up = SimpleLineStyle(style=up)
        self.down = SimpleLineStyle(style=down)

    def next(self, dirx, diry):
        angle = super().next(dirx, diry)
        # right
        if angle <= math.pi / 4 or angle > 7 * math.pi / 4:
            return self.left.get(self.index)
        # left
        if angle >= 3 * math.pi / 4 and angle < 5 * math.pi / 4:
            return self.right.get(self.index)
        # up
        if angle >= math.pi / 4 and angle < 3 * math.pi / 4:
            return self.up.get(self.index)
        # down
        if angle >= 5 * math.pi / 4 and angle < 7 * math.pi / 4:
            return self.down.get(self.index)
        err = "Angle not in range"
        raise Exception(err)


class Compass(LineStyle):
    def __init__(
        self,
        nn=None,
        ne=None,
        ee=None,
        se=None,
        ss=None,
        sw=None,
        ww=None,
        nw=None,
        **kwargs,
    ):
        super().__init__(**kwargs)

        self.nn = SimpleLineStyle(style=nn)
        self.ne = SimpleLineStyle(style=ne)
        self.ee = SimpleLineStyle(style=ee)
        self.se = SimpleLineStyle(style=se)
        self.ss = SimpleLineStyle(style=ss)
        self.sw = SimpleLineStyle(style=sw)
        self.ww = SimpleLineStyle(style=ww)
        self.nw = SimpleLineStyle(style=nw)

    def next(self, dirx, diry):
        angle = (super().next(dirx, diry) + math.pi * 3.0 / 2.0) % (2 * math.pi)
        # nn
        if angle < math.pi / 8 or angle > 15 * math.pi / 8:
            return self.nn.get(self.index)
        # ne
        if angle > math.pi / 8 and angle < 3 * math.pi / 8:
            return self.ne.get(self.index)
        # ee
        if angle > 3 * math.pi / 8 and angle < 5 * math.pi / 8:
            return self.ee.get(self.index)
        # se
        if angle > 5 * math.pi / 8 and angle < 7 * math.pi / 8:
            return self.se.get(self.index)
        # ss
        if angle > 7 * math.pi / 8 and angle < 9 * math.pi / 8:
            return self.ss.get(self.index)
        # sw
        if angle > 9 * math.pi / 8 and angle < 11 * math.pi / 8:
            return self.sw.get(self.index)
        # ww
        if angle > 11 * math.pi / 8 and angle < 13 * math.pi / 8:
            return self.ww.get(self.index)
        # nw
        if angle > 13 * math.pi / 8 and angle < 15 * math.pi / 8:
            return self.nw.get(self.index)
        err = "Angle not in range"
        raise Exception(err)
