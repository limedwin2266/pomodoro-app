**Pomodoro Timer App 🍅**
This is a simple Pomodoro Timer app built using Python and Tkinter. 
The Pomodoro technique is a time management method that breaks work into intervals, traditionally 25 minutes in length, separated by short breaks. After four work sessions, a longer break is taken.

**Features**
1. Start and Reset: Start the timer for a work session or a break, and reset the timer at any time.
2. Visual Countdown: Displays a countdown timer showing the remaining time for the current session (work or break).
3. Work and Break Phases: The timer alternates between work sessions and breaks:
- Work Session: 25 minutes (default).
- Short Break: 5 minutes (default).
- Long Break: 20 minutes (after four work sessions).
4. Progress Tracking: Tracks the number of completed work sessions with checkmarks (✔) on the screen.
5. Simple UI: Clean and user-friendly design with a tomato icon to represent the Pomodoro technique.

**How to Use**
Start Timer: Click the "Start" button to begin a work session. The timer will count down from 25 minutes.
Break Time: Once the work session ends, the app will automatically switch to a short break. After four work sessions, it will switch to a longer break.
Reset Timer: If you want to stop the timer or reset it, click the "Reset" button.

**Customization**
You can easily customize the following variables in the code:
- WORK_MIN: Set the length of a work session (in minutes).
- SHORT_BREAK_MIN: Set the length of a short break (in minutes).
- LONG_BREAK_MIN: Set the length of a long break (in minutes).

**Technologies Used**
- Python
- Tkinter (for GUI)
- math (for countdown calculations)
