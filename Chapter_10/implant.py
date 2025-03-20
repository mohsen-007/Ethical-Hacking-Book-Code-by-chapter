# Do ScrrenShot From Window 

from mss import mss
with mss() as sct:
	image = sct.shot()
