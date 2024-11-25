Personalized Study Guide Generator
A Python-based GUI application that helps users create a customized study guide by allocating 
time for specific subjects and topics. With this tool, users can easily organize their study 
plans based on their available time and save the plan for future reference.

Features
User-friendly graphical interface using Tkinter.
Allows users to input:
Subject name.
Topics (comma-separated).
Total available study hours.
Automatically calculates the time allocation per topic.
Displays the study plan on the screen.
Provides an option to save the study guide as a .txt file.

How It Works
Enter the subject name in the Subject field.
List the topics to be studied, separated by commas (e.g., Topic 1, Topic 2, Topic 3).
Specify the total number of study hours available.
Click "Generate Study Plan" to create a personalized study guide.
Optionally, click "Save Study Plan" to export the guide as a .txt file.

Installation
Prerequisites
Python 3.x must be installed on your system. Download it from python.org.
Dependencies
This project uses Python's standard library, so no additional dependencies are required. 
However, you can install optional libraries for added features:
1.To add image support (optional):
  pip install pillow
2.To export study guides as PDFs (optional):
  pip install pypdf2
  pip install reportlab

Usage
1.Clone this repository or download the code files.
  git clone https://github.com/your-username/study-guide-generator.git
  cd study-guide-generator
2.Run the Python script:
  python study_guide_generator.py


Example Output
 Input:
  =>Subject: Mathematics
  =>Topics: Algebra, Geometry, Calculus, Trigonometry
  =>Available Study Hours: 4
 Generated Study Plan:
  Study Plan for Mathematics:
   1. Algebra - 1.00 hours
   2. Geometry - 1.00 hours
   3. Calculus - 1.00 hours
   4. Trigonometry - 1.00 hours


Save Functionality
=>Click the "Save Study Plan" button to export your study plan to a .txt file. 
You’ll be prompted to choose a location and filename.


Extending the Project
Here are some ways to extend or improve this project:

Add difficulty levels for topics to allocate time dynamically.
=>Enable PDF export for study plans.
=>Include a slider for selecting priority or focus areas.
=>Add a calendar integration for dividing topics across days.


License
This project is licensed under the MIT License. You are free to use, modify, and 
distribute it.

Contributing
Contributions are welcome! Feel free to fork this repository and submit a pull request 
with your enhancements or fixes.

Contact
For questions or feedback, please contact:
Email: shykhfurkan@gmail.com
