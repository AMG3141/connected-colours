'''
Generally speaking very slow, even when not plotting starts and ends and when only searching for one colour.
I think it might be an idea to do a sweep of the whole image on the first frame, or on every e.g. 10th frame and otherwise just look in the vicinity of the objects we've already found and ``track'' them.
'''
import numpy as np
import matplotlib.pyplot as plt
from time import sleep
from datetime import datetime

def camera(numRows: int, numCols: int, numFrames: int) -> np.ndarray:
	video = np.zeros([numRows, numCols, numFrames], dtype = int)
	d = np.random.randint(-5, 6, 12)
	for i in range(numFrames):
		#video[i:(i + 10), i:(i + 15), i] = 1
		#video[(3 * i):(3 * i + 14), (2 * i):(3 * i), i] = 2
		#video[(2 * i):int(2.5 * i), (4 * i):int(5.2 * i), i] = 3

		video[(i + d[0]):(i + 20 + d[1]), (i + d[2]):(i + 20 + d[3]), i] = 1
		video[(i + d[4]):(i + 20 + d[5]), int(numCols / 2 - 10 + d[6]):int(numCols / 2 + 10 + d[7]), i] = 2
		video[int(numRows / 2 - 10 + d[8]):int(numRows / 2 + 10 + d[9]), (i + d[10]):(i + 20 + d[11]), i] = 3

	return video

def makeTestImage() -> np.ndarray:
	image = np.zeros([500, 500])
	image[50:100, 50:100] = 1
	image[148:270, 200:490] = 2
	image[343:490, 256:300] = 3
	return image

def plotStartsEnds(starts: list, ends: list):
	startsy, startsx = zip(*starts) # y's come first due to weirdness with images being indexed from top left corner
	endsy, endsx = zip(*ends)
	plt.scatter(startsx, startsy, label = "starts")
	plt.scatter(endsx, endsy, label = "ends")
	#plt.legend()

def coloursClose(target: int, pixel: int) -> bool:
	# TODO: do this based on hue (i think, want it to be independent of brightness). This is just a rough approximation
	return target == pixel

# TODO: if something is at the edge of the frame, I don't think it is able to see it
def searchForColour(image: np.ndarray, colour: int) -> tuple:
	# The starts and ends of each connected component on each line
	starts = []
	ends = []

	# Set to true when we detect the start of a component, set to false once component ends
	foundComponentOnLine = False
	for i in range(image.shape[0]):
		# TODO OPTIMISATION: If something was found on the previous line, start searching from roughly where it started
		#                    (i.e. start j early, will need to change how starts/ends are tracked i think)

		foundComponentOnLine = False
		for j in range(image.shape[1]):
			if coloursClose(colour, image[i][j]):
				if not foundComponentOnLine:
					starts.append((i, j))
					foundComponentOnLine = True
			else:
				if foundComponentOnLine:
					ends.append((i, j))
					foundComponentOnLine = False

	return starts, ends

def main():
	#im = makeTestImage()
	#starts, ends = searchForColour(im, 3)
	#plotStartsEnds(starts, ends)
	#plt.show()

	################################################

	vid = camera(316, 208, 200)
	start = datetime.now()
	
	if __debug__:
		plt.ion()
		plt.show()

	for i in range(vid.shape[2]):
		if __debug__:
			plt.imshow(vid[:, :, i])

		frame = vid[:, :, i]
		starts1, ends1 = searchForColour(frame, 1)
		starts2, ends2 = searchForColour(frame, 2)
		starts3, ends3 = searchForColour(frame, 3)
		print(i)

		if __debug__:
			for (starts, ends) in [(starts1, ends1), (starts2, ends2), (starts3, ends3)]:
				if len(starts) != 0 and len(ends) != 0:
					plotStartsEnds(starts, ends)

			input(i)
			plt.cla()
	
	################################################
	
	end = datetime.now()
	print(f"Runtime: {end - start}. Avg FPS: {vid.shape[2] / (end - start).total_seconds()}")

if __name__ == "__main__":
	main()
