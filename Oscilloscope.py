#import matplotlib.pyplot as plt
#from matplotlib.animation import FuncAnimation
#import Adafruit_ADS1x15


ani = FuncAnimation(fig, update, interval=500)
plt.show()

fig, ax = plt.subplots()
ax.set_ylimit(-5000, 5000)
ax.set_title("OSCILLOSCOPE")
ax.set_ylabel("ADC OUTPUT")
ax.grid(True)

line, = ax.plot([], 'ro-', label="CHANNEL 0")
ax.legend(loc = "lower right")

def update(cnt):
	value = adc.get_last_result()
	print("CHANNEL 0: {0}".format(value))
	line.set_data(list(range(len(val))), val)
	ax.relim()
	ax.autoscale_view()
	val.append(int(value))
	if(cnt>50):
		val.pop(0)



adc = Adafruit_ADS1x15.ADS1115()

GAIN = 1
val = []
