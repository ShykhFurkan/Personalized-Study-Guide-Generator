import tkinter as tk
from tkinter import messagebox, filedialog

def generate_study_plan():
    subject = entry_subject.get()
    topics = entry_topics.get().split(",")
    time = entry_time.get()

    try:
        time = int(time)
    except ValueError:
        messagebox.showerror("Input Error", "Study hours must be a number!")
        return

    if not subject or not topics or time <= 0:
        messagebox.showerror("Input Error", "All fields must be filled correctly!")
        return

    total_topics = len(topics)
    time_per_topic = time / total_topics

    study_plan = f"Study Plan for {subject}:\n"
    for i, topic in enumerate(topics, 1):
        study_plan += f"{i}. {topic.strip()} - {time_per_topic:.2f} hours\n"

    text_output.delete(1.0, tk.END)
    text_output.insert(tk.END, study_plan)

def save_study_plan():
    study_plan = text_output.get(1.0, tk.END).strip()
    if not study_plan:
        messagebox.showwarning("Save Error", "No study plan to save!")
        return

    file_path = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
    )
    if file_path:
        with open(file_path, "w") as file:
            file.write(study_plan)
        messagebox.showinfo("Success", f"Study plan saved to {file_path}")

# Create Main App Window
root = tk.Tk()
root.title("Personalized Study Guide Generator")
root.geometry("500x500")

label_title = tk.Label(root, text="Study Guide Generator", font=("Arial", 16))
label_title.pack(pady=10)

label_subject = tk.Label(root, text="Enter Subject:")
label_subject.pack(pady=5)
entry_subject = tk.Entry(root, width=40)
entry_subject.pack()

label_topics = tk.Label(root, text="Enter Topics (comma-separated):")
label_topics.pack(pady=5)
entry_topics = tk.Entry(root, width=40)
entry_topics.pack()

label_time = tk.Label(root, text="Enter Available Study Hours:")
label_time.pack(pady=5)
entry_time = tk.Entry(root, width=10)
entry_time.pack()

btn_generate = tk.Button(root, text="Generate Study Plan", command=generate_study_plan)
btn_generate.pack(pady=10)

text_output = tk.Text(root, height=10, width=50)
text_output.pack(pady=10)

btn_save = tk.Button(root, text="Save Study Plan", command=save_study_plan)
btn_save.pack(pady=5)

# Run the App
root.mainloop()
