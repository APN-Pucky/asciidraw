from asciidraw.line import ASCIILine
from asciidraw.pane import ASCIIPane
from asciidraw.point import ASCIIPoint
from asciidraw.style import Compass, LineStyle

pane = ASCIIPane(10, 10)


starline = ASCIILine(style=LineStyle(["*"]))
arrowline = ASCIILine(
    begin="#",
    end="#",
    style=Compass(
        ww="←",
        ee="→",
        nn="↑",
        ss="↓",
        nw="↖",
        ne="↗",
        sw="↙",
        se="↘",
    ),
)

starline.draw(pane, 0, 0, 9, 9)
arrowline.draw(pane, 0, 9, 9, 0)
ASCIIPoint("O").draw(pane, 5, 5)
print(pane)
