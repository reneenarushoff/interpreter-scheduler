NO_INTERPRETER = "No interpreter available"

def schedule (appt_info, interpreters):
    """
    Matches an appointment to an available interpreter based on language and date.
    
    Parameters:
        appt_info (dict): Dict containing appointment info (must include 'Language' and 'Date')
        interpreters (list): List of interpreter dictionaries with 'Language', 'Availability', and 'Name'
    
    Returns:
        str: The name of the matched interpreter, or "No interpreter available" if none found
    """
    for interpreter in interpreters:
       if (interpreter["Language"] == appt_info["Language"]) and (interpreter["Availability"]== appt_info["Date"]):
            # TODO: Add time range validation (Start_Time/End_Time)
            return interpreter["Name"]
    return NO_INTERPRETER