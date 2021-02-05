from tkinter import *
import random
root = Tk()
root.geometry("700x1400")

#check function
def check():
	global word, incorrect_attempts, total_attempts, attempts_left, length
	guess = entry_box.get()
	
	if len(guess) != 1:
		attempts_label["text"] = f"""Total Attempts: {total_attempts}
Incorrect Attempts: {incorrect_attempts}
You have {attempts_left} attempts left.
Guess must be one letter."""
	
	elif guess not in word:
		incorrect_attempts += 1
		attempts_label["text"] = f"""Total Attempts: {total_attempts}
Incorrect Attempts: {incorrect_attempts}
You have {attempts_left} attempts left."""

	else:
		positions = []
		for i in range(length):
			if word[i] == guess:
				positions.append(i)
				
		for i in positions:
			labels[i]["text"] = guess 

	if incorrect_attempts == 6:
		submit_button["state"] = DISABLED
		win_label["text"] = f"Incorrect, the word was {word}!"
		
	guessed = True
	for i in labels:
		if i["text"] == " _ ":
			guessed = False

	if guessed == True:
		win_label["text"] = f"Correct, the word is {word}!"
		
#creating the frames
main_frame = Frame(root)
head_frame = Frame(root)
attempts_frame = Frame(main_frame)
entry_frame = Frame(main_frame)
submit_frame = Frame(main_frame)
word_frame = Frame(main_frame)
win_frame = Frame(main_frame)

main_frame.place(relx=0.5, rely=0.5, anchor=CENTER)
head_frame.place(relx=0.5, rely=0.3, anchor=CENTER)
attempts_frame.pack()
word_frame.pack()
entry_frame.pack()
submit_frame.pack()
win_frame.pack()

#implementing the logic
total_attempts = 6
incorrect_attempts = 0
attempts_left = total_attempts - incorrect_attempts

words = []
labels = []

file = open("words.txt", "r")
for line in file:
	line = line.lower()
	line = line.strip()
	words.append(line)
file.close()

num = random.randint(1, 101)
word = words[num]
length = len(word)
current_word = "_" * length
column = 0

#creating the layout
heading = Label(head_frame, text="Welcome To Hangman!", font=("Comic Sans MS", 14, "underline"))
heading.pack()

submit_button = Button(submit_frame, text="Submit", bg="sky blue", activebackground="pink", command=check)
submit_button.pack()

attempts_label = Label(attempts_frame, text=f"""Total Attempts: {total_attempts}
Incorrect Attempts: {incorrect_attempts}
You have {attempts_left} attempts left.""")
attempts_label.pack()

entry_label = Label(entry_frame, text="Enter a letter: ")
entry_box = Entry(entry_frame)

entry_label.grid(row=0, column=0)
entry_box.grid(row=0, column=1)

for i in current_word:
	labels.append(Label(word_frame, text=(" " + i + " ")))
	labels[column].grid(row=0, column=column)
	column += 1
	
win_label = Label(win_frame, text="")
win_label.pack()

root.mainloop()
