from pprint import pprint
import pyttsx3
import cloudmersive_virus_api_client
from cloudmersive_virus_api_client.rest import ApiException
import tkinter as tk
from tkinter import simpledialog
from tkinter import messagebox
import webbrowser

# Configure API key authorization: Apikey
configuration = cloudmersive_virus_api_client.Configuration()

# Use pyttsx3 to add a voice prompt
engine = pyttsx3.init()

# Function to check if the API key is properly formatted
def is_valid_api_key(api_key):
    # Add your own logic to check the format of the API key
    # For example, check if it's a valid UUID
    return len(api_key) == 36  # Placeholder logic; adjust as needed

# Ask the user for the API key through a voice prompt
engine.say("Please enter your API key.")
engine.runAndWait()

root = tk.Tk()
root.withdraw()  # Hide the main window

api_key = simpledialog.askstring("API Key", "Enter your API key:")

# Check if the API key is properly formatted
while not is_valid_api_key(api_key):
    engine.say("Invalid API key. Re-enter your API key?")
    engine.runAndWait()
    response = simpledialog.askstring("API Key", "Re-enter your API key:")
    if response.lower() == 'yes':
        api_key = simpledialog.askstring("API Key", "Re-enter your API key:")
    else:
        engine.say("Do you want to generate a new API key?")
        engine.runAndWait()
        generate_api_key = messagebox.askyesno("Generate API Key", "Do you want to generate a new API key?")
        if generate_api_key:
            # Redirect the user to the signup URL
            # engine.say("Redirecting to the Cloudmersive signup website.")

            # engine.say("Redirecting to the Cloudmersive signup website.")
            # engine.runAndWait()

            # Guide the user to the respective API and manage keys page for key generation
            engine.say("Please visit the Cloudmersive API website.")
              # Prompt the user to sign up
            engine.say("If you don't have an account, you will need to sign up for a Cloudmersive account.")
            engine.say("You can sign up by clicking on the 'Sign Up' or 'Create Account' button on the website.")
            engine.runAndWait()
            engine.say("Navigate to the 'Manage Keys' section to generate a new API key.")
            engine.say("You can find this option in the 'API Management' or 'Developer Console' area.")
            engine.runAndWait()
            engine.runAndWait()
          
            webbrowser.open("https://portal.cloudmersive.com/signup")
            exit()
        else:
            exit()

# Configure API key
configuration.api_key['Apikey'] = api_key

# Create an instance of the API class
api_instance = cloudmersive_virus_api_client.ScanApi(cloudmersive_virus_api_client.ApiClient(configuration))

def scan(input_file='EICAR TEST FILE.txt'):
    try:
        # Scan a file for viruses
        api_response = api_instance.scan_file(input_file)
        pprint(api_response)
        # Uncomment the 2 lines below to enable automatic virus delete
        # if "'clean_result': False" in str(api_response):
        # remove(input_file)
    except ApiException as e:
        print("Exception when calling ScanApi->scan_file: %s\n" % e)

# Continue with your code...
