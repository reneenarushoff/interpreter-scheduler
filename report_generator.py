import pandas as pd

def validate_appointment_result(appointment):
    errors = []
    
    if not appointment.get("Client"):
        errors.append("Missing Client")

    if not appointment.get("Language"):
        errors.append("Missing Language Needed")

    if not appointment.get("Date"):
        errors.append("Missing Date")

    if not appointment.get("Start_Time") or not appointment.get("End_Time"):
        errors.append("Missing Time")

    if appointment.get("Interpreter") == "No interpreter available":
        errors.append("Unable to be Scheduled")

    return ', '.join(errors) if errors else "Valid"

def generate_report(appointment_df: pd.DataFrame, output_path: str = "validation_report.csv"):
    """ Generate report for DataFrame containg appointment data, 
        Adds Validation Result column to report and prints summary"""
        
    appointment_df["Validation Result"] = appointment_df.apply(validate_appointment_result, axis=1)
    print(appointment_df)
        
    appointment_df.to_csv(output_path, index=False)
    print(f" Validation report saved to: {output_path}")

    errors_df = appointment_df[appointment_df["Validation Result"] != "Valid"]
    if not errors_df.empty:
        print("\n Validation Errors:")
        print(errors_df[["Appointment_ID", "Client", "Language", "Start_Time", "End_Time", "Interpreter", "Validation Result"]])
    else:
        print("\n All appointments are valid!")

 
    