# AI-Powered-Personal-Assistant

**Importing Libraries:** The required libraries are imported, including speech_recognition, pyttsx3, wikipedia, webbrowser, datetime, and os.

**Text-to-Speech Initialization:** The pyttsx3 library is initialized to create an instance of the text-to-speech engine.

**speak() Function:** The speak() function takes a text input and uses the text-to-speech engine to convert it into speech output.

**listen() Function:** The listen() function uses the speech_recognition library to listen for audio input from the user's microphone. It converts the audio into text using the Google Speech Recognition API.

**run_personal_assistant() Function:** The main function that handles the execution of the personal assistant. It contains a loop that continuously listens for user input.

**User Commands:** Inside the loop, the user's query is processed. The code checks for specific commands or keywords such as "wikipedia," "open youtube," "open google," "time," and "quit."

If the query contains "wikipedia," the code extracts the search term and uses the wikipedia library to fetch a summary of the topic and speaks it using the speak() function.
If the query contains "open youtube," it opens the YouTube website using the webbrowser library.
If the query contains "open google," it opens the Google website using the webbrowser library.
If the query contains "time," it retrieves the current time and speaks it using the speak() function.
If the query contains "quit," it breaks the loop and exits the program.
If none of the specific commands are detected, the assistant responds with a default message using the speak() function.

**Execution:** The program runs the run_personal_assistant() function, which starts listening for user commands and responds accordingly.
