import datetime

import pyxel

class App():
	def __init__(self):
		pyxel.init(128, 64)
		self.t = 0
		pyxel.run(self.update, self.draw)
	def update(self):
		self.t = datetime.datetime(year=2023, month=1, day=1).timestamp() - \
			datetime.datetime.now().timestamp()
		self.t = -1
		self.string = str(int(self.t)) if 0.0 <= self.t else "Happy New Year!"
	def draw(self):
		pyxel.cls(0)
		pyxel.text(
			(pyxel.width - len(self.string) * pyxel.FONT_WIDTH) // 2, 
			(pyxel.height - pyxel.FONT_WIDTH) // 2, 
			self.string, pyxel.COLOR_YELLOW
		)

App()