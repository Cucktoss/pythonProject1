import math
import tkinter as tk


def pyshader(func, w, h):
 scr = bytearray((0, 0, 0) * w * h)
 for y in range(h):
  for x in range(w):
   p = (w * y + x) * 3
   scr[p:p + 3] = [max(min(int(c * 255), 255), 0) for c in func(x / w, y / h)]
 return bytes('P6\n%d %d\n255\n' % (w, h), 'ascii') + scr
# Ваш код здесь:
def func(x, y):
 if (math.sqrt(((127.5/255-x)**2)+((127.5/255-y)**2)) > 100/255):
  x = 0
  y = 0
 return x,y,0
label = tk.Label()
img = tk.PhotoImage(data=pyshader(func, 255, 255)).zoom(2, 2)
label.pack()
label.config(image=img)
tk.mainloop()