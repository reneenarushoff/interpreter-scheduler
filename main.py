import json
import pandas as pd
from pydantic import BaseModel
from validator import TestAppt
from scheduler import schedule
from report_generator import generate_report


appointments = []

#Load appointment data
with open('appointments.json', 'r') as file:
    appt_data = json.load(file)

#Load interpreter data
with open('interpreters.json', 'r') as file:
    interp_data = json.load(file)


#Process and validate appointments
for appt in appt_data:
    test = TestAppt(**appt)

    test_dict = test.model_dump()
    interpreter = schedule(test_dict, interp_data)

    test_dict.update({"Interpreter": interpreter})
    appointments.append(test_dict)

#Generate validation report
appointment_df = pd.DataFrame(appointments)
generate_report(appointment_df)



# PROJECT ROADMAP / TODO ===
# Support interpreters who speak multiple languages (e.g., ["Spanish", "French"])
# Implement time range validation (check if Start_Time and End_Time fit interpreter availability)
# Mark interpreters as unavailable after assignment to prevent double-booking
# Build a learning-based "Availability Analyzer" to prioritize likely matches based on past data
