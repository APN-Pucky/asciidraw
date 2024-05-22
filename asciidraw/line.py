import warnings


class ASCIILine:
    def __init__(
        self,
        style,
        begin=None,
        end=None,
    ):
        self.style = style
        if begin is not None:
            warnings.warn(
                "begin is deprecated, use style.begin instead. Set it in style for now.",
                DeprecationWarning,
            )
            self.style.end = end
        if end is not None:
            warnings.warn(
                "end is deprecated, use style.end instead. Set it in style for now.",
                DeprecationWarning,
            )
            self.style.begin = begin

    def draw(
        self,
        pane,
        isrcx,
        isrcy,
        itarx,
        itary,
        scalex=1,
        scaley=1,
        kickx=0,
        kicky=0,
        wrap=lambda x: x,
        **kwargs,
    ):
        # width = len(pane[0])
        # height = len(pane)
        # TODO normalize to width and height as well
        srcx = int((isrcx + kickx) * scalex)
        srcy = int((isrcy + kicky) * scaley)
        tarx = int((itarx + kickx) * scalex)
        tary = int((itary + kicky) * scaley)

        xsign = 1 if srcx < tarx else -1
        ysign = 1 if srcy < tary else -1

        if abs(srcx - tarx) > abs(srcy - tary):
            for i in range(srcx, tarx + xsign, xsign):
                v = self.style.next(tarx - srcx, tary - srcy)
                if v is not None:
                    pane[round(srcy + (tary - srcy) * (i - srcx) / (-srcx + tarx))][
                        i
                    ] = wrap(self.style.wrap(v))
        else:
            for i in range(srcy, tary + ysign, ysign):
                v = self.style.next(tarx - srcx, tary - srcy)
                if v is not None:
                    pane[i][
                        round(srcx + (tarx - srcx) * (i - srcy) / (-srcy + tary))
                    ] = wrap(self.style.wrap(v))
        # call once to increase the index
        v = self.style.next(tarx - srcx, tary - srcy)

        if v is None:
            return
        if self.style.begin is not None and self.style.begin != "":
            pane[srcy][srcx] = wrap(self.style.wrap(self.style.begin))
        if self.style.end is not None and self.style.end != "":
            pane[tary][tarx] = wrap(self.style.wrap(self.style.end))
