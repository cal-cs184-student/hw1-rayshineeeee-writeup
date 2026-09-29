"""Generate competition.svg from an abstract study of Ray's Campanile photo."""

from math import cos, sin, pi
from pathlib import Path


elements = []


def polygon(points, color):
    coordinates = " ".join(f"{x:.2f},{y:.2f}" for x, y in points)
    elements.append(f'<polygon points="{coordinates}" fill="{color}"/>')


def rect(x, y, width, height, color):
    elements.append(
        f'<rect x="{x:.2f}" y="{y:.2f}" width="{width:.2f}" '
        f'height="{height:.2f}" fill="{color}"/>'
    )


def color_triangle(points, colors):
    coordinates = " ".join(f"{x} {y}" for x, y in points)
    rgba = []
    for color in colors:
        rgba.extend(f"{int(color[i:i + 2], 16) / 255:.6f}" for i in (1, 3, 5))
        rgba.append("1")
    elements.append(f'<colortri points="{coordinates}" colors="{" ".join(rgba)}"/>')


def arch(x, y, width, height, color):
    radius = width / 2
    points = [(x, y + height)]
    points += [(x + radius + radius * cos(pi + i * pi / 12),
                y + radius + radius * sin(pi + i * pi / 12)) for i in range(13)]
    points.append((x + width, y + height))
    polygon(points, color)


# Broad color planes preserve the photograph's amber sky and distant haze.
color_triangle([(0, 0), (800, 0), (0, 490)], ["#f5b927", "#ffe17c", "#ed691c"])
color_triangle([(800, 0), (800, 490), (0, 490)], ["#ffe17c", "#ec842f", "#ed691c"])
rect(0, 490, 800, 310, "#a96543")
polygon([(0, 421), (85, 442), (182, 427), (325, 453), (451, 435),
         (590, 452), (693, 432), (800, 447), (800, 555), (0, 555)], "#c88046")
polygon([(0, 494), (104, 466), (233, 498), (366, 471), (512, 498),
         (627, 480), (800, 499), (800, 574), (0, 574)], "#b56b42")
polygon([(0, 541), (163, 516), (327, 546), (530, 517), (683, 527),
         (800, 512), (800, 604), (0, 604)], "#995c40")

rect(0, 587, 800, 129, "#b5764e")
polygon([(0, 601), (800, 584), (800, 610), (0, 631)], "#d99959")
polygon([(0, 667), (800, 624), (800, 650), (0, 690)], "#c78953")

# The bridge cuts diagonally across the bay, as in the reference.
polygon([(0, 668), (800, 607), (800, 613), (0, 675)], "#654536")

polygon([(0, 711), (165, 697), (343, 714), (552, 701), (800, 690),
         (800, 800), (0, 800)], "#514438")

# Two flat faces carry the tower's form.
polygon([(154, 405), (256, 395), (256, 800), (145, 800)], "#34362f")
polygon([(256, 395), (331, 406), (342, 800), (256, 800)], "#795238")
polygon([(175, 345), (257, 146), (257, 346)], "#514532")
polygon([(257, 146), (309, 347), (257, 346)], "#976932")
polygon([(175, 345), (257, 346), (257, 398), (180, 402)], "#45402f")
polygon([(257, 346), (309, 347), (309, 403), (257, 398)], "#826039")
polygon([(241, 154), (244, 110), (252, 96), (253, 54),
         (254, 96), (263, 110), (266, 154)], "#4a402d")

for x, top, width in [(152, 332, 19), (249, 326, 18), (313, 331, 17)]:
    polygon([(x - 3, 398), (x, top + 13), (x + width / 2, top),
             (x + width, top + 13), (x + width + 4, 398)], "#4b432e")

polygon([(145, 399), (256, 391), (336, 400), (331, 410), (151, 413)], "#594630")

for x in [180, 205, 230]:
    arch(x, 441, 13, 111, "#292e28")
for x in [270, 289, 308]:
    arch(x, 439, 12, 116, "#34372b")
polygon([(150, 568), (256, 563), (337, 569),
         (337, 574), (256, 568), (150, 573)], "#3d382c")

# The clock is a plain oval on the sunlit face.
cx, cy = 298, 648
ring = [(cx + 24 * cos(i * pi / 32), cy + 40 * sin(i * pi / 32)) for i in range(64)]
polygon(ring, "#92663c")

output = Path(__file__).resolve().parents[1] / "competition.svg"
output.write_text('<svg xmlns="http://www.w3.org/2000/svg" width="800" height="800">\n'
                  + "\n".join(elements) + "\n</svg>\n")
print(output)
