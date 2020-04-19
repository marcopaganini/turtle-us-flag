#!/usr/bin/python3
"""
flag.py - Draw an American Flag
Dec/2011 by Marco Paganini <paganini@paganin.net>

This is a simple program using python's 'turtle' module. It draws
a mathematically correct US flag. The relative sizes of all elements
in the flag were taken from the Wikipedia entry on the American Flag:
http://en.wikipedia.org/wiki/Flag_of_the_United_States

Note: this program is in no way optimized or elegant. I wrote it as a
request from my son, who asked for a "really complicated turtle program".
:)
"""

import turtle
import sys

def rectangle(tt, x, y, width, height, fcolor = None):
  """Draw a rectangle with the bottom left coords in x, y.
  Use 'fcolor' as fill color, if specified."""

  tt.penup()
  tt.setpos(x, y)
  tt.towards(1, 0)
  tt.pendown()

  if fcolor is not None:
    oldcolors = tt.color()
    tt.color(fcolor, fcolor)
    tt.begin_fill()

  for _ in range(2):
    tt.forward(width)
    tt.left(90)
    tt.forward(height)
    tt.left(90)

  if fcolor is not None:
    tt.end_fill()
    tt.color(oldcolors[0], oldcolors[1])


def star(tt, x, y, radius, fcolor = None):
  """Draw a star of radius 'radius', centered at x,y. If fcolor is
  set, the star will be filled with that color."""

  # Start at bottom left
  # See http://mathworld.wolfram.com/Pentagram.html for calculations
  unity = radius / 0.525731
  xdist = unity * 0.309017
  adist = unity * 0.381966
  rdist = unity * 0.200811
  ydist = unity * 0.224514

  tt.penup()
  tt.setpos(x - xdist, y - (rdist + ydist))
  tt.towards(x + 1, y)
  tt.pendown()

  if fcolor is not None:
    oldcolors = tt.color()
    tt.color(fcolor, fcolor)
    tt.begin_fill()

  for _ in range(5):
    tt.left(36)
    tt.forward(adist)
    tt.right(72)
    tt.forward(adist)
    tt.left(108)
  
  if fcolor is not None:
    tt.end_fill()
    tt.color(oldcolors[0], oldcolors[1])


def main():
  tt = turtle.Turtle()

  # Flag height is width / 1.9
  xsize = 640
  ysize = xsize / 1.9

  # Initial flag location. We assume that the viewport is centered on the turtle
  # at the start, so these offsets will produce a centered flag.
  xoffset = -(xsize / 2)
  yoffset = -(ysize / 2)

  # because ain't nobody got time for that...
  tt.speed('fastest')

  # Seven red stripes, Six white stripes.
  stripe_height = ysize / 13;
  sy = yoffset
  for _ in range(7):
    rectangle(tt, xoffset, sy, xsize, stripe_height, '#BE0D34')
    sy += stripe_height * 2

  # Union is six stripes high, 0.4 of the width.
  union_height = stripe_height * 7
  union_width = xsize * 0.4
  rectangle(tt, xoffset, stripe_height * 6 + yoffset, union_width, union_height, '#002663')

  # Stars.
  star_hspacing = union_width / 6
  star_vspacing = union_height / 5
  star_radius = (ysize * 0.0616) / 2
  sy_base = (stripe_height * 6) + (star_vspacing / 2) + yoffset

  # 5 rows with 6 stars.
  sy = sy_base
  for row in range(5):
    sx = star_hspacing / 2 + xoffset
    for col in range(6):
      star(tt, sx, sy, star_radius, "white")
      sx += star_hspacing
    sy += star_vspacing

  # 4 rows with 5 stars.
  sy = sy_base + star_vspacing / 2
  for row in range(4):
    sx = star_hspacing + xoffset
    for col in range(5):
      star(tt, sx, sy, star_radius, "white")
      sx += star_hspacing
    sy += star_vspacing

  # Border.
  rectangle(tt, xoffset, yoffset, xsize, ysize)

  # tt.exitonclick()

if __name__ == "__main__":
  main()
