from asciidraw.line import ASCIILine
from asciidraw.pane import ASCIIPane
from asciidraw.point import ASCIIPoint
from asciidraw.style import Compass, SimpleLineStyle, colored

pane = ASCIIPane(10, 10)


starline = ASCIILine(begin=None, end="", style=SimpleLineStyle(["*"], color="red"))
arrowline = ASCIILine(
    begin="",
    end="",
    style=Compass(
        ww="←",
        ee="→",
        nn="↑",
        ss="↓",
        nw="↖",
        ne="↗",
        sw=[colored("↙", "green")],  # array here because it loops
        se="↘",
    ),
)

starline.draw(pane, 9, 9, 0, 0)
arrowline.draw(pane, 9, 0, 0, 9)
ASCIIPoint("O").draw(pane, 5, 5)
print(pane)
