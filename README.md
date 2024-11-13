**PulseAI Voice-Activated Assistant**
PulseAI is a voice-activated AI assistant developed in Python. It uses speech recognition to interact with users and perform various tasks like opening websites, providing conversational responses, fetching information from Wikipedia, playing songs(Beta), taking screenshots, and remembering user notes. Designed for a more personalized experience, PulseAI uses your name and responds based on the time of day.

**Features**
Voice Commands: Listens to user commands, interprets them, and takes appropriate actions.
Greeting: Customizes greetings based on the time of day.
Website Navigation: Opens popular websites by name (e.g., Google, YouTube, Wikipedia).
Information Retrieval: Fetches summaries from Wikipedia for "what is" queries.
Screenshot Capture: Takes a screenshot and saves it to the user’s Pictures directory.
Memory: Remembers information upon request and recalls it when asked.
Conversational Responses: Provides responses for casual conversations.
Music Search: Finds and plays songs based on Google search.
Date and Time: Reads the current date and time upon request.
**Requirements**
To use PulseAI, make sure you have the following Python packages installed:
pip install pyttsx3 SpeechRecognition wikipedia-api pyautogui googlesearch-python

Also, PulseAI is configured to use Brave Browser for web searches. Ensure Brave is installed, or modify the path in the code to your preferred browser.

**Usage**
Initialize:

Run the program
Enter your name when prompted to personalize the experience.

**Commands:**

Greet: Just say "Hello," "Hi," or "Good Morning," etc.
Ask the Time or Date: Use "What time is it?" or "What’s today’s date?"
Open Websites: Say "Open [website name]" (e.g., "Open Google").
Wikipedia Search: Say "What is [topic]" to get a Wikipedia summary.
Take a Screenshot: Just say "Take a screenshot."
Remember Notes: Say "Remember that [note]" to save information.
Recall Notes: Use "Do you remember?" to hear stored information.
Play a Song: Say "Play [song name]" to search for a song on Google.
End Session: Say "Power off" to exit PulseAI.
Error Handling:

If speech recognition fails or the request cannot be completed, PulseAI will inform you with a spoken error message.
**File Structure**
main.py: The main file containing the code for the assistant.
data.txt: Stores notes or information you ask PulseAI to remember.


**Code Overview**
Initialization: Configures the pyttsx3 engine and registers Brave Browser.
Main Functions:
speak(): Text-to-speech for spoken responses.
command(): Listens for user commands.
greet(): Provides time-based greetings.
song_google(): Searches for a song on Google.
Loop Execution: The main loop listens for commands and checks them against a set of conditions for executing specific tasks.

**Customization**
You can customize PulseAI by:

Adding more websites to the websites dictionary.
Expanding conversational_responses with additional responses.
Adjusting the speech rate or voice type in the speak() function.


**Troubleshooting**
No Response to Commands: Ensure your microphone is working and configured correctly.
Incorrect Recognition: If speech recognition accuracy is low, try speaking more clearly or adjusting recog.pause_threshold in the command() function.
Missing Wikipedia Summaries: Make sure you have an internet connection for fetching data from Wikipedia.

**License**
This project is open-source and available under the MIT License.
