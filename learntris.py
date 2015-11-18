#!/usr/bin/python
import sys

class Learntris:
	def __init__(self, width, depth):
		self.width = width
		self.depth = depth
		self.board = []

		self.score = 0
		self.linesCleared = 0

		self.shape_names = 'IOTJSZ'
		self.activeTetramino = None
	
		for i in range(self.depth):
			row = []
			for j in range(self.width):
				row.append('.')
			self.board.append(row)

	def read_stdin(self):
		line = sys.stdin.readline().rstrip()

		commands = filter(lambda x: x not in ' ', list(line))
		cmdLen = len(commands)
		i = 0

		while i < cmdLen:
			cmd = commands[i]
			if cmd == 'p':
				self.print_static_grid()
			elif cmd == 'g':
				self.read_grid()
			elif cmd == 'c':
				self.clear_board()
			elif cmd == 's':
				self.step()
			

			#Query controls
			elif cmd == '?':
				next_cmd = commands[i+1]
				if next_cmd == 's':
					print self.score
				if next_cmd == 'n':
					print self.linesCleared
			
			#Select active tetramino
			elif cmd in self.shape_names:
				self.activeTetramino = cmd

			#Display active tetramino
			# elif cmd == 't':

			elif cmd == 'q':
				return False
			i += 1

		return True

	def print_static_grid(self):
		for row in self.board:
			i = 0
			for cell in row:
				if i == 9:
					print cell
				else:
					print cell,
				i += 1

	def read_grid(self):
		#Read 22 lines of text from stdin
		#Pop matrix
		lineIndex = 0
		valid_chars = '.rgbcymo'

		while lineIndex < self.depth:
			line = sys.stdin.readline().rstrip()

			#split line, check for valid length
			linesplit = line.split(' ')

			if len(linesplit) != self.width:
				return
				#UH OHHHHHHHH

			for i, c in enumerate(linesplit):
				if i < self.width:
					if c.lower() not in valid_chars or len(c)>1:
						return
					self.board[lineIndex][i] = c

			lineIndex += 1

	def clear_board(self):
		del self.board[:]

		for line in range(self.depth):
			row = []
			for cell in range(self.width):
				row.append('.')
			self.board.append(row)

	def step(self):

		def clear_row(row):
			for cell in range(self.width):
				self.board[row][cell] = '.'

		block_chars = 'rgbcymo'

		rowIndex = 0
		for row in self.board:
			if '.' not in row:
				clear_row(rowIndex)
				self.score += 100
				self.linesCleared += 1
			rowIndex += 1




def start(width, height):
	learntris = Learntris(width, height)

	run_status = True
	while run_status:
		run_status = learntris.read_stdin()

start(10, 22)