import math
from typing import Iterable


class Style:
    def __init__(self, style=None, **kwargs):
        self.index = -1

    def next(self, dirx, diry):
        self.index += 1
        return (math.atan2(diry, dirx) + math.pi) % (2 * math.pi)


class LineStyle(Style):
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


class Cross(Style):
    def __init__(
        self, vert=None, horz=None, left=None, up=None, right=None, down=None, **kwargs
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

        self.left = LineStyle(style=left)
        self.right = LineStyle(style=right)
        self.up = LineStyle(style=up)
        self.down = LineStyle(style=down)

    def next(self, dirx, diry):
        angle = super().next(dirx, diry)
        # right
        if angle <= math.pi / 4 or angle > 7 * math.pi / 4:
            return self.left.get(self.index)
        # left
        elif angle >= 3 * math.pi / 4 and angle < 5 * math.pi / 4:
            return self.right.get(self.index)
        # up
        elif angle >= math.pi / 4 and angle < 3 * math.pi / 4:
            return self.up.get(self.index)
        # down
        elif angle >= 5 * math.pi / 4 and angle < 7 * math.pi / 4:
            return self.down.get(self.index)
        else:
            raise Exception("Angle not in range")


class Compass(Style):
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
        **kwargs
    ):
        super().__init__(**kwargs)

        self.nn = LineStyle(style=nn)
        self.ne = LineStyle(style=ne)
        self.ee = LineStyle(style=ee)
        self.se = LineStyle(style=se)
        self.ss = LineStyle(style=ss)
        self.sw = LineStyle(style=sw)
        self.ww = LineStyle(style=ww)
        self.nw = LineStyle(style=nw)

    def next(self, dirx, diry):
        angle = (super().next(dirx, diry) + math.pi * 3.0 / 2.0) % (2 * math.pi)
        # nn
        if angle < math.pi / 8 or angle > 15 * math.pi / 8:
            return self.nn.get(self.index)
        # ne
        elif angle > math.pi / 8 and angle < 3 * math.pi / 8:
            return self.ne.get(self.index)
        # ee
        elif angle > 3 * math.pi / 8 and angle < 5 * math.pi / 8:
            return self.ee.get(self.index)
        # se
        elif angle > 5 * math.pi / 8 and angle < 7 * math.pi / 8:
            return self.se.get(self.index)
        # ss
        elif angle > 7 * math.pi / 8 and angle < 9 * math.pi / 8:
            return self.ss.get(self.index)
        # sw
        elif angle > 9 * math.pi / 8 and angle < 11 * math.pi / 8:
            return self.sw.get(self.index)
        # ww
        elif angle > 11 * math.pi / 8 and angle < 13 * math.pi / 8:
            return self.ww.get(self.index)
        # nw
        elif angle > 13 * math.pi / 8 and angle < 15 * math.pi / 8:
            return self.nw.get(self.index)
        else:
            raise Exception("Angle not in range")
