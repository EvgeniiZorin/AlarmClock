###############################################################################
#####   Alarm clock GUI   #####################################################
###############################################################################
"""
This script is easier to run as an exe file. To convert this script into an .exe file, please run: pyinstaller --onefile -w Alarm_clock_GUI.py
"""
###############################################################################
from tkinter import *
from PIL import ImageTk, Image
import datetime
import os
import time
import random
import webbrowser

root = Tk()
root.title('Program name')
root.iconbitmap('Media/danger.ico')
root.geometry('1700x800')
#root['bg'] = "grey"
#root.resizable(width=False, height=False)

frame1 = LabelFrame(root, text="Image viewer", padx=50, pady=50)
frame1.grid(row=0, column=0, padx=10, pady=10)

frame2 = LabelFrame(root, text="Youtube alarm clock", padx=50, pady=50)
frame2.grid(row=0, column=1, padx=10, pady=10)


my_img1 = ImageTk.PhotoImage(Image.open("Media/image1.jpg"))
my_img2 = ImageTk.PhotoImage(Image.open("Media/image2.jpg"))
my_img3 = ImageTk.PhotoImage(Image.open("Media/image3.jpg"))
my_img4 = ImageTk.PhotoImage(Image.open("Media/image4.jpg"))
my_img5 = ImageTk.PhotoImage(Image.open("Media/image5.jpg"))
image_list = [my_img1, my_img2, my_img3, my_img4, my_img5]
status = Label(frame1, text=f"Image 1 of {len(image_list)}", bd=1, relief=SUNKEN).grid(row=2, column=1, pady=10)

my_label = Label(frame1, image=my_img1)
my_label.grid(row=0, column=0, columnspan=3)

def forward(image_number):
	global my_label
	global button_forward
	global button_back

	my_label.grid_forget()
	my_label = Label(frame1, image=image_list[image_number-1])
	button_forward = Button(frame1, text=">>", command=lambda: forward(image_number+1))
	button_back = Button(frame1, text="<<", command=lambda: back(image_number-1))
	
	if image_number == 5:
		button_forward = Button(root, text=">>", state=DISABLED)
	
	my_label.grid(row=0, column=0, columnspan=3)
	button_back.grid(row=1, column=0)
	button_forward.grid(row=1, column=2)

	# Update status bar
	status = Label(frame1, text=f"Image {image_number} of {len(image_list)}", bd=1, relief=SUNKEN).grid(row=2, column=1, pady=10)

def back(image_number):
	global my_label
	global button_forward
	global button_back

	my_label.grid_forget()
	my_label = Label(frame1, image=image_list[image_number-1])
	button_forward = Button(frame1, text=">>", command=lambda: forward(image_number+1))
	button_back = Button(frame1, text="<<", command=lambda: back(image_number-1))
	
	if image_number == 1:
		button_back = Button(frame1, text="<<", state=DISABLED)

	my_label.grid(row=0, column=0, columnspan=3)
	button_back.grid(row=1, column=0)
	button_forward.grid(row=1, column=2)

	# Update status bar
	status = Label(frame1, text=f"Image {image_number} of {len(image_list)}", bd=1, relief=SUNKEN).grid(row=2, column=1, pady=10)

button_back = Button(frame1, text="<<", command=back, state=DISABLED)
button_exit = Button(frame1, text="EXIT", command=root.quit, padx=30)
button_forward = Button(frame1, text=">>", command=lambda: forward(2)) 

button_back.grid(row=1, column=0)
button_exit.grid(row=1, column=1)
button_forward.grid(row=1, column=2, pady=10)

#########################################################################################################

#Label(root, text="").grid(row=2, column=0)

Label(frame2, text="Set a time for the alarm").grid(row=3, column=0)


e = Entry(frame2, width=50)
e.grid(row=3, column=1)
#e.insert(0, "Enter your name in this field: ")


def myClick():
	
	#myLabel = Label(root, text="Holi, " + e.get())
	#myLabel.pack()
	alarm_input = e.get()
	alarm_time = [int(n) for n in alarm_input.split(":")]
	

	# Convert the alarm time from [H:M] or [H:M:S] to seconds
	seconds_hms = [3600, 60, 1] # Number of seconds in an Hour, Minute, and Second
	alarm_time_seconds = sum([a*b for a,b in zip(seconds_hms[:len(alarm_time)], alarm_time)])

	# Get the current time of day in seconds
	now = datetime.datetime.now()
	current_time_seconds = sum([a*b for a,b in zip(seconds_hms, [now.hour, now.minute, now.second])])

	# Calculate the number of seconds until alarm goes off
	time_diff_seconds = alarm_time_seconds - current_time_seconds

	# If time difference is negative, set alarm for next day
	if time_diff_seconds < 0:
		time_diff_seconds += 86400 # number of seconds in a day

	# Display the amount of time until the alarm goes off
	myLabel3 = Label(frame2, text=f"Current time is {now.hour}:{now.minute}")
	myLabel3.grid(row=4, column=0)
	myLabel4 = Label(frame2, text=f"Alarm set to go off in {datetime.timedelta(seconds=time_diff_seconds)}")
	myLabel4.grid(row=4, column=1)

	def final_message():
		
		myLabel6 = Label(frame2, text="Time to wake up").grid(row=5, column=0)
		if os.path.isfile("Media/youtube_alarm_videos.txt"):
			with open("Media/youtube_alarm_videos.txt", "r") as alarm_file:
				videos = alarm_file.readlines()
			webbrowser.open(random.choice(videos))
		else:
			webbrowser.open('https://www.youtube.com/watch?v=KEOFsQm6Je0')

	root.after(time_diff_seconds*1000, final_message)
	


	#time_diff_seconds3 = time_diff_seconds - time_elapsed


# Button to put entered value into myClick:

myButton = Button(frame2, text="Enter ", command=myClick, 
				  padx=50, pady=10,
				  fg="lightgreen", bg="darkgreen")
myButton.grid(row=3, column=2)


canvas = Canvas(frame2, height=300, width=250)
canvas.grid(row=6, column=0)

# frame = Frame(root, bg='red')
# frame.place(relwidth=0.7, relheight=0.7, relx=0.15, rely=0.15)

##################################################################

root.mainloop()