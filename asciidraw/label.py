import re

from .line import ASCIILine
from .style import Cross


class Label(ASCIILine):
    def __init__(self, label, handle_tex=True, color=None):
        if handle_tex:
            self.label = self.handle_tex(label)
        else:
            self.label = label
        super().__init__(
            style=Cross(
                vert=[*self.label, None],
                horz=[*self.label, None],
                terminate=True,
                begin=None,
                end=None,
                color=color,
            ),
        )

    @staticmethod
    def handle_tex(s):
        """
        Remove TeX commands from a string to pure ASCII.
        """
        s = s.replace("\\bar", "_")
        s = s.replace("\\tilde", "~")
        s = re.sub(r"\\[a-zA-Z]+", "", s)
        return (
            s.replace("$", "")
            .replace("{", "")
            .replace("}", "")
            .replace("\\(", "")
            .replace("\\)", "")
            .replace("\\", "")
            .replace("^", "")
        )

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
        # reduce length to 1/3 in the middle
        jsrcx = (itarx - isrcx) / 3.0 + isrcx
        jsrcy = (itary - isrcy) / 3.0 + isrcy
        jtarx = (itarx - isrcx) / 3.0 * 2.0 + isrcx
        jtary = (itary - isrcy) / 3.0 * 2.0 + isrcy

        # shift the line
        shift = 3.0
        # horizonral
        if abs(isrcx - itarx) > abs(isrcy - itary):
            # left to right -> shift up
            if isrcx < itarx:
                jsrcy -= shift / scaley
                jtary -= shift / scaley
            # right to left -> shift down
            else:
                jsrcy += shift / scaley
                jtary += shift / scaley

        # vertical
        # up to down -> shift left
        elif isrcy < itary:
            jsrcx -= shift / scalex
            jtarx -= shift / scalex
        # down to up -> shift right
        else:
            jsrcx += shift / scalex
            jtarx += shift / scalex

        super().draw(
            pane,
            jsrcx,
            jsrcy,
            jtarx,
            jtary,
            scalex,
            scaley,
            kickx,
            kicky,
            wrap,
            **kwargs,
        )
        self.index = 0
