import tkinter as tk
from tkinter import messagebox

# Store all workouts
workouts = []


# ---------------- ADD WORKOUT ----------------

def add_workout():
    exercise = exercise_entry.get()
    sets = sets_entry.get()
    reps = reps_entry.get()
    weight = weight_entry.get()

    if exercise == "" or sets == "" or reps == "" or weight == "":
        messagebox.showerror("Error", "Please fill all fields.")
        return

    try:
        sets = int(sets)
        reps = int(reps)
        weight = float(weight)

        if sets <= 0 or reps <= 0 or weight < 0:
            raise ValueError

    except ValueError:
        messagebox.showerror(
            "Error",
            "Sets and reps must be positive numbers."
        )
        return

    workout = {
        "exercise": exercise,
        "sets": sets,
        "reps": reps,
        "weight": weight
    }

    workouts.append(workout)

    messagebox.showinfo(
        "Success",
        "Workout added successfully!"
    )

    # Clear input fields
    exercise_entry.delete(0, tk.END)
    sets_entry.delete(0, tk.END)
    reps_entry.delete(0, tk.END)
    weight_entry.delete(0, tk.END)

    update_history()


# ---------------- WORKOUT HISTORY ----------------

def update_history():
    history_text.delete("1.0", tk.END)

    if len(workouts) == 0:
        history_text.insert(tk.END, "No workouts recorded yet.")
        return

    for i, workout in enumerate(workouts, start=1):

        history_text.insert(
            tk.END,
            f"{i}. {workout['exercise']} | "
            f"{workout['sets']} sets × "
            f"{workout['reps']} reps | "
            f"{workout['weight']} kg\n"
        )


# ---------------- ANALYTICS ----------------

def show_analytics():

    if len(workouts) == 0:
        messagebox.showinfo(
            "Analytics",
            "No workout data available."
        )
        return

    total_volume = 0

    for workout in workouts:

        volume = (
            workout["sets"]
            * workout["reps"]
            * workout["weight"]
        )

        total_volume += volume

    messagebox.showinfo(
        "Workout Analytics",
        f"Total Workouts: {len(workouts)}\n\n"
        f"Total Training Volume: {total_volume:.2f} kg"
    )


# ---------------- GUI ----------------

root = tk.Tk()

root.title("Gym Workout Tracker")
root.geometry("600x600")
root.resizable(False, False)


# Title
title_label = tk.Label(
    root,
    text="GYM WORKOUT TRACKER",
    font=("Arial", 22, "bold")
)

title_label.pack(pady=20)


# Input Frame
input_frame = tk.Frame(root)
input_frame.pack(pady=10)


# Exercise
tk.Label(
    input_frame,
    text="Exercise:"
).grid(row=0, column=0, padx=10, pady=8)

exercise_entry = tk.Entry(input_frame, width=30)
exercise_entry.grid(row=0, column=1, padx=10, pady=8)


# Sets
tk.Label(
    input_frame,
    text="Sets:"
).grid(row=1, column=0, padx=10, pady=8)

sets_entry = tk.Entry(input_frame, width=30)
sets_entry.grid(row=1, column=1, padx=10, pady=8)


# Reps
tk.Label(
    input_frame,
    text="Reps:"
).grid(row=2, column=0, padx=10, pady=8)

reps_entry = tk.Entry(input_frame, width=30)
reps_entry.grid(row=2, column=1, padx=10, pady=8)


# Weight
tk.Label(
    input_frame,
    text="Weight (kg):"
).grid(row=3, column=0, padx=10, pady=8)

weight_entry = tk.Entry(input_frame, width=30)
weight_entry.grid(row=3, column=1, padx=10, pady=8)


# Add Workout Button
add_button = tk.Button(
    root,
    text="Add Workout",
    width=20,
    command=add_workout
)

add_button.pack(pady=15)


# History Heading
tk.Label(
    root,
    text="Workout History",
    font=("Arial", 16, "bold")
).pack(pady=10)


# History Text Box
history_text = tk.Text(
    root,
    width=65,
    height=10
)

history_text.pack(pady=5)


# Analytics Button
analytics_button = tk.Button(
    root,
    text="Show Analytics",
    width=20,
    command=show_analytics
)

analytics_button.pack(pady=15)


# Exit Button
exit_button = tk.Button(
    root,
    text="Exit",
    width=20,
    command=root.destroy
)

exit_button.pack()


# Start application
root.mainloop()
