# parameters for detection
vpy = 224  # y vanishing point
#turn_slope = 15
turn_slope = 0
threshold = 200
bandheight = 8  # height of vertical band of pixels to look at

# WHEEL_TICK_LENGTH = 0.02 * 32/40.
# NUM_ENCODERS = 4

WHEEL_DIAMETER = 0.0666
DRIVE_RATIO = 84./27. * 2.1  # 27t pinion
#DRIVE_RATIO = 84./25. * 2.1
#DRIVE_RATIO = 84./25. * 1.9
MOTOR_POLES = 3
WHEEL_TICK_LENGTH = WHEEL_DIAMETER*3.1415 / DRIVE_RATIO / MOTOR_POLES
NUM_ENCODERS = 1
STEER_DIRECTION = -1

CONE_RADIUS = 44.5/3.1415/200.  # cone radius in meters
#NOISE_ANGULAR = 0.2
#NOISE_LONG = 10
#NOISE_LAT = 0.5

NOISE_ANGULAR = 2.75
NOISE_LONG = 50
NOISE_LAT = 0.25

# "temperature" for particle filter resampling
# (depends on magnitude of activations, which are summed pixel intensity values)
PF_TEMP = 200e-6

# not used by particle filter, just visualization
V_THRESHOLD = 30

# 2.6889650239916953 lon 38.60174828208218 lat 85.65356704908227

#BOGON_THRESH = .21**2  # minimum radians^2 to a real landmark
#BOGON_THRESH = .1**2  # minimum radians^2 to a real landmark
BOGON_THRESH = .31**2  # minimum radians^2 to a real landmark
