# EvCharging-Final
Project Summary: EV Charging Station Finder and Slot Booking
Project Overview:
The EV Charging Station Finder and Slot Booking project is a Python-based application designed to help electric vehicle (EV) users locate nearby charging stations and book available charging slots. The project integrates with the Open Charge Map API to retrieve real-time information about EV charging stations based on the user’s location. Users can search for stations, view details, and simulate booking a charging slot at their chosen station.

Key Features:
EV Charging Station Finder:

Users input their current latitude and longitude.
The application retrieves and displays nearby EV charging stations within a specified radius.
For each station, details such as the name, address, and distance from the user are displayed.
Slot Booking Simulation:

Users can select a charging station from the list.
The application presents available time slots for the selected station.
Users can choose a time slot to simulate booking a charging session.
User Interface:

The project currently features a command-line interface (CLI) for interaction.
Users are guided through the process of finding stations and booking slots with simple prompts.
Technical Details:
Programming Language: Python
Dependencies:
requests: Used to make HTTP requests to the Open Charge Map API for fetching charging station data.
Project Structure:
finder.py: Handles the retrieval of nearby EV charging stations.
booking.py: Simulates the booking of charging slots and provides mock available slots.
ui.py: Manages user interactions, displaying stations, and facilitating the booking process.
main.py: The main entry point that integrates all modules and runs the application.
Development Environment:
IDE: Visual Studio Code (VS Code)
Virtual Environment: Used to manage dependencies and isolate the project environment.
Setup Instructions:
Clone the Repository: (Or create a new project folder)
Install Dependencies:
Add required packages to requirements.txt.
Run pip install -r requirements.txt to install the dependencies.
Run the Application:
Execute main.py to start the application.
Follow the prompts to find EV charging stations and book slots.
Future Enhancements:
Real Slot Booking: Integrate with real APIs that support slot booking at EV charging stations.
Graphical User Interface (GUI): Develop a more user-friendly interface using Tkinter or a web-based UI with Flask.
Database Integration: Store user bookings and charging station data for offline access and history tracking.
Conclusion:
This project provides a foundational tool for EV users to easily find and book charging stations. It demonstrates practical use of APIs, user interaction handling, and simulates a real-world application that could be expanded into a fully functional product with further development.
