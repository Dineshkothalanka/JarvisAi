"""
Main application entry point for Jarvis-like AI assistant.
"""

from voice_interaction import VoiceInteraction
from web_search import WebSearch
from resume_preparation import ResumePreparation
from job_search import JobSearch
from task_automation import TaskAutomation

def main():
    voice = VoiceInteraction()
    # Replace with your actual API key
    web_search = WebSearch(api_key="YOUR_GOOGLE_API_KEY")
    resume_prep = ResumePreparation()
    job_search = JobSearch()
    task_auto = TaskAutomation()

    voice.speak("Hello, I am Jarvis. How can I assist you today?")

    try:
        while True:
            command = voice.listen().lower()
            print(f"Command received: {command}")

            if 'search' in command or 'web search' in command:
                voice.speak("What do you want to search for?")
                query = voice.listen()
                results = web_search.search(query)
                for result in results[:3]:
                    voice.speak(result)

            elif 'resume' in command or 'make a resume' in command:
                voice.speak("Please provide your name.")
                name = voice.listen()
                voice.speak("Please provide your email.")
                email = voice.listen()
                voice.speak("Please provide your phone number.")
                phone = voice.listen()
                voice.speak("Please list your experiences, say 'done' when finished.")
                experiences = []
                while True:
                    exp = voice.listen()
                    if 'done' in exp.lower():
                        break
                    # Check for interrupt commands
                    if 'search' in exp.lower() or 'web search' in exp.lower() or 'job search' in exp.lower():
                        voice.speak("Interrupting resume creation to process new command.")
                        command = exp.lower()
                        break
                    experiences.append(exp)
                if 'done' not in exp.lower():
                    # If interrupted, continue processing new command
                    continue
                voice.speak("Please list your education details, say 'done' when finished.")
                education = []
                while True:
                    edu = voice.listen()
                    if 'done' in edu.lower():
                        break
                    # Check for interrupt commands
                    if 'search' in edu.lower() or 'web search' in edu.lower() or 'job search' in edu.lower():
                        voice.speak("Interrupting resume creation to process new command.")
                        command = edu.lower()
                        break
                    education.append(edu)
                if 'done' not in edu.lower():
                    # If interrupted, continue processing new command
                    continue
                resume_prep.create_resume(name, email, phone, experiences, education)
                resume_prep.save_resume("resume.docx")
                voice.speak("Your resume has been created and saved as resume.docx.")

            elif 'job search' in command:
                voice.speak("What job title are you looking for?")
                job_title = voice.listen()
                voice.speak("Which location?")
                location = voice.listen()
                jobs = job_search.search_jobs(job_title, location)
                for job in jobs[:5]:
                    voice.speak(job)

            elif 'reminder' in command:
                voice.speak("What should I remind you about?")
                message = voice.listen()
                voice.speak("In how many seconds?")
                delay = voice.listen()
                try:
                    delay_seconds = int(delay)
                    task_auto.set_reminder(message, delay_seconds)
                    voice.speak(f"Reminder set for {delay_seconds} seconds from now.")
                except ValueError:
                    voice.speak("Sorry, I did not understand the time.")

            elif 'open' in command:
                voice.speak("Please provide the application path.")
                app_path = voice.listen()
                response = task_auto.open_application(app_path)
                voice.speak(response)

            elif 'exit' in command or 'quit' in command:
                voice.speak("Goodbye!")
                break

            else:
                print(f"Unrecognized command: {command}")
                voice.speak("Sorry, I did not understand that command.")
    except KeyboardInterrupt:
        voice.speak("Goodbye!")
        print("Program terminated by user.")

if __name__ == "__main__":
    main()
