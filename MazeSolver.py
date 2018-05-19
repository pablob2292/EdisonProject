
#-------------Setup----------------

import Ed

Ed.EdisonVersion = Ed.V2

Ed.DistanceUnits = Ed.CM
Ed.Tempo = Ed.TEMPO_SLOW

#turn on obstacle detection
Ed.ObstacleDetectionBeam(Ed.ON)

#turn on line detection (border's maze)
Ed.LineTrackerLed(Ed.ON)

#set up variables
SideTurn = 0
obstacle = 0
mazeWidth = 2
turnAngle = 95
Speed = Ed.SPEED_1

def turnBlack():
	global SideTurn
	Ed.LeftLed(Ed.ON)
	Ed.RightLed(Ed.ON)
	Ed.PlayBeep()
	Ed.Drive(Ed.BACKWARD, Speed, mazeWidth+1)
	if SideTurn ==1:
		Ed.Drive(Ed.SPIN_RIGHT, Speed, turnAngle)
		SideTurn = 0
	else:
		SideTurn = 1
		Ed.Drive(Ed.SPIN_LEFT, Speed, turnAngle)

	obstaclePos = Ed.OBSTACLE_NONE
	Ed.LeftLed(Ed.OFF)
	Ed.RightLed(Ed.OFF)

def turnObs():
	global SideTurn
    #set obstacle with ir detection or line detection obstacle
	obstaclePos = Ed.ReadObstacleDetection()
		    
	if (obstaclePos > Ed.OBSTACLE_NONE):
		#turn on both LEDs and back up
		    
		Ed.LeftLed(Ed.ON)
		Ed.RightLed(Ed.ON)
		Ed.PlayBeep()
		Ed.Drive(Ed.BACKWARD, Speed, mazeWidth)
		#look at where the obstacle is and turn away from it (if obstacle ahead turn a random direction)
		obstaclePos = Ed.ReadObstacleDetection()
		if obstaclePos==Ed.OBSTACLE_LEFT:
			Ed.Drive(Ed.SPIN_RIGHT, Speed, turnAngle)
		elif obstaclePos==Ed.OBSTACLE_RIGHT:
			Ed.Drive(Ed.SPIN_LEFT, Speed, turnAngle)
		elif obstaclePos==Ed.OBSTACLE_AHEAD:
			if SideTurn ==1:
				SideTurn = 0
				Ed.Drive(Ed.SPIN_RIGHT, Speed, turnAngle)
			else:
				SideTurn = 1
				Ed.Drive(Ed.SPIN_LEFT, Speed, turnAngle)

		obstaclePos = Ed.OBSTACLE_NONE
	#after the obstacle has been avoided turn the LEDs off
		Ed.LeftLed(Ed.OFF)
		Ed.RightLed(Ed.OFF)

#loop forever
while True:
	Ed.Drive(Ed.FORWARD, Speed, Ed.DISTANCE_UNLIMITED)
	while Ed.ReadLineState()==Ed.LINE_ON_WHITE:
	    Ed.Drive(Ed.FORWARD, Speed, Ed.DISTANCE_UNLIMITED)
	    turnObs()
	turnBlack()
	
