Introduction
In today’s digitally driven learning environment, university students often face challenges in balancing academic demands and emotional well-being. Many struggle with organizing deadlines, managing stress, and maintaining consistent motivation throughout the semester. This assignment explores the development of a web-based application that supports both academic planning and mental health for students. Through user-centered design techniques such as personas, scenarios, conceptual modeling, and interface sketching, this project aims to create a tool that helps students stay organized, track their mental state, and receive timely support. The web application is intended to be accessible, easy to use, and focused on improving students' academic performance while promoting mental wellness.
Part A: Discovering Requirements 
PERSONA 1: SIPHO – THE OVERWHELMED FINAL-YEAR STUDENT
•	Name: Sipho Mthembu
•	Age: 22
•	Gender: Male
•	Degree Program: BSc in Computer Science
•	Year of Study: Final Year
•	Location: Durban, South Africa
•	Pain Points:
o	Constantly forgets deadlines for assignments and tests
o	Feels mentally drained due to constant pressure
o	No system to manage both academic and emotional load
•	Goals:
o	Organize academic deadlines in one place
o	Receive reminders before tasks are due
o	Track emotional well-being and get helpful tips
•	Tech Comfort: Skilled with computers and web tools

PERSONA 2: THANDEKA – THE FIRST-YEAR STUDENT ADJUSTING TO UNIVERSITY LIFE
•	Name: Thandeka Dube
•	Age: 18
•	Gender: Female
•	Degree Program: BA in Psychology
•	Year of Study: First Year
•	Location: Johannesburg, South Africa
•	Pain Points:
o	Has difficulty adjusting to academic routines
o	Feels anxious and sometimes overwhelmed
o	Needs help organizing tasks and staying emotionally grounded
•	Goals:
o	Build good academic habits from the start
o	Receive structure and reminders for daily tasks
o	Feel supported and emotionally balanced
•	Tech Comfort: Comfortable using websites and online platforms

Scenario 1: Sipho’s Story
Sipho is juggling final-year projects and often forgets deadlines. After using the web app, he logs in daily to check his calendar. The app sends him reminders two days before due dates and lets him check in on his mood every morning. Over time, Sipho finds himself more organized and less anxious, knowing both his academic tasks and mental health are being supported.

Scenario 2: Thandeka Story
As a new student, Thandeka struggles with remembering lectures and submitting work. The web app helps her log all her academic tasks and set reminders. She also uses the mood tracker and gets calming quotes and tips whenever she feels stressed. With this system in place, Thandeka begins to feel more confident and connected in her new academic environment.
Part B: Conceptual Model 
1. Key Features of the Web App
•	Dashboard: View academic tasks, upcoming events, and mood overview
•	Calendar: Add deadlines, lectures, or study sessions
•	Mood Tracker: Log emotional state daily using emojis or words
•	Reminders: Automated email or on-site notifications
•	Wellness Tips: Suggestions based on mood history

2. Interaction Types
Feature	Interaction Type
Add task/mood entry	Click, Type, Submit Form
View calendar/mood graph	Click, Hover, Scroll
Receive notifications	On-screen alerts
wellness tips	Click, Navigate

3. Metaphor: “Your Academic Wellness Dashboard”
The app acts like a personal dashboard, helping students monitor both their academic journey and emotional well-being, much like how a car dashboard shows both speed and fuel. The app ensures that students stay aware and balanced throughout their studies.

4. Conceptual Model Diagram
           

                        
                                        
 ▼                             ▼                     ▼                        ▼
Calendar          Mood Check-In      Tasks/Reminders       Tips & Wellness
View/Update    (Form-based)             (Deadlines)            (Based on mood)

Short Explanation (under the diagram)
The conceptual model above presents a student-centered web app with a homepage dashboard that connects core features: calendar tracking, mood logging, task management, and wellness support. The user interacts through clicking, typing, and browsing to add or view tasks and mood entries. The web-based design makes the platform accessible from any device, allowing students to manage both their academic and emotional needs in one central place.

Part C: Interface Sketching and Django Wireframe![WhatsApp Image 2025-04-13 at 12 24 52](https://github.com/user-attachments/assets/d7be31d9-d21a-45f7-a197-77bbea9cb20b)
![WhatsApp Image 2025-04-13 at 12 28 34](https://github.com/user-attachments/assets/be441c79-ec67-4776-87b9-29be75108f90)

    
Part D: Evaluation Planning
1. USABILITY & UX GOALS
•	Usability Goal 1: Efficiency
Users should be able to set academic tasks and track their mental health in under 3 minutes, ensuring quick access to core features.
•	Usability Goal 2: Learnability
First-time users should be able to navigate and use key features (e.g., adding tasks, completing a mental check-in) without needing external help or a tutorial.
•	UX Goal: Emotional Support & Empowerment
Users should feel supported and more in control of their academic and emotional journey after interacting with StudyBloom, leading to a positive emotional response and continued use.

2. USER TESTING QUESTIONS
1.	How easy was it to add a new academic task or deadline?
2.	Were you able to find and complete a mental wellness check-in without confusion?
3.	How did the design make you feel while using the app?
4.	What features did you find most helpful, and what was missing or unclear?

3. EVALUATION METHOD: THINK-ALOUD PROTOCOL
Why it's relevant:
The think-aloud method allows us to observe users in real-time as they interact with StudyBloom, encouraging them to verbalize their thoughts. This helps identify usability pain points, confusing navigation paths, and emotional reactions to the interface and experience. Since StudyBloom blends task management with emotional support, understanding user thought processes is essential for refining both functionality and emotional impact.
Part E: Reflection
Working on StudyBloom has been a challenging but rewarding journey that taught me a lot about user-centered design. I learned that designing with the user in mind is not just about creating something that looks good, but about truly understanding the needs, goals, and pain points of the people who will be using the product. Through personas, scenarios, and feedback loops, I gained a deeper appreciation for the importance of empathy and active listening in the design process. Building a tool that helps students manage both their academic responsibilities and mental health required me to think beyond basic functionality I had to consider emotional impact and accessibility as well.
One of the most difficult parts of this project was applying conceptual modeling. It was challenging to break down user needs and translate them into abstract components and relationships before any actual interface design. Figuring out how mental wellness tracking, academic planning, and user feedback would work together took several iterations. At times, I felt unsure whether the model truly reflected user behavior or just my assumptions. It required constant revision and validation, which pushed me to refine my thought process and be more critical about design decisions.
Sketching and developing wireframes using Django came with its own set of challenges. To be honest, I had to restart the project around 11 times. Django wasn’t cooperating with me either the framework broke down mid-way or I ran into compatibility issues. At times, it felt like I was going in circles. But each restart forced me to think smarter, simplify where necessary, and stay focused on the core features. Even though the journey was frustrating, I’m glad I pushed through. In the end, I was able to get the most important features up and running like task scheduling and mental wellness check-ins  and that felt like a huge win.
This project taught me perseverance, the real value of user feedback, and how to turn a design vision into a working prototype. It wasn’t perfect, but it was honest work, and I’m proud of the outcome.
