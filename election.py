import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image

# Initialize vote counters
Modi_Votes = 0
Rahul_Votes = 0

# Create the main application window
root = tk.Tk()
root.title(" Basic Voting System")

# Set the window size to be wider
root.geometry("400x400")  # Width x Height

# Change background color to light blue
root.configure(bg='#ADD8E6')  # Light blue color

# Lock main window size
root.resizable(False, False)

# Load images
image1 = Image.open("image1.png")
image1 = image1.resize((150, 150), Image.Resampling.LANCZOS)
photo1 = ImageTk.PhotoImage(image1)

image2 = Image.open("image2.jpg")
image2 = image2.resize((150, 150), Image.Resampling.LANCZOS)
photo2 = ImageTk.PhotoImage(image2)

# Create functions to be called when buttons are clicked
def button1_click():
    global Modi_Votes
    Modi_Votes += 1

def button2_click():
    global Rahul_Votes
    Rahul_Votes += 1

# Create a function to show the results in a new window
def show_results():
    results_window = tk.Toplevel(root)
    results_window.title("Voting Results")
    results_window.geometry("400x400")  # Width x Height

    results_window.configure(bg='#90EE90')  # Light green color
    results_window.resizable(False, False)  # Lock results window size
    
    # Determine the winner and loser
    if Modi_Votes > Rahul_Votes:
        winner_name = "Narendra Modi"
        winner_votes = Modi_Votes
        loser_name = "Rahul Gandhi"
        loser_votes = Rahul_Votes
    elif Rahul_Votes > Modi_Votes:
        winner_name = "Rahul Gandhi"
        winner_votes = Rahul_Votes
        loser_name = "Narendra Modi"
        loser_votes = Modi_Votes
    else:
        winner_name = "Tie"
        winner_votes = Modi_Votes  # Both are the same in case of a tie
        loser_name = ""
        loser_votes = 0
    
    # Configure fonts
    winner_font = ('Helvetica', 20, 'bold')
    table_font = ('Helvetica', 12)
    
    # Create labels for winner and loser
    if winner_name == "Tie":
        winner_label = tk.Label(results_window, text="It's a Tie!", font=winner_font)
    else:
        winner_label = tk.Label(results_window, text=f"{winner_name} Wins!", font=winner_font)
    
    winner_label.pack(pady=10)
    
    if winner_name != "Tie":
        winner_image_label = tk.Label(results_window, image=photo1 if winner_name == "Narendra Modi" else photo2)
        winner_image_label.pack()
        
        winner_votes_label = tk.Label(results_window, text=f"Votes: {winner_votes}", font=winner_font)
        winner_votes_label.pack(pady=10)
    
    # Create a table to display winner and loser votes
    table_frame = ttk.Frame(results_window)
    table_frame.pack(pady=10)
    
    tree = ttk.Treeview(table_frame, columns=("candidate", "votes"), show="headings")
    tree.heading("candidate", text="Candidate")
    tree.heading("votes", text="Votes")
    tree.column("candidate", width=150)
    tree.column("votes", width=100)
    
    # Insert winner data
    tree.insert("", tk.END, values=(winner_name, winner_votes))
    
    # Insert loser data if there is a loser
    if loser_name:
        tree.insert("", tk.END, values=(loser_name, loser_votes))
    
    tree.pack()

# Create buttons
button1 = tk.Button(root, text="Narendra Modi", image=photo1, compound=tk.TOP, command=button1_click)
button2 = tk.Button(root, text="Rahul Gandhi", image=photo2, compound=tk.TOP, command=button2_click)
results_button = tk.Button(root, text="Results", command=show_results, bg="#FFC0CB", font=('Helvetica', 16, 'bold'))

# Use grid to center the buttons
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)

button1.grid(row=0, column=1, padx=10, pady=10)
button2.grid(row=0, column=2, padx=10, pady=10)
results_button.grid(row=1, column=1, columnspan=2, pady=10, ipadx=20, ipady=10)  # Increase button width and height

# Run the main loop
root.mainloop()
