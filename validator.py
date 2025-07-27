from pydantic import BaseModel, Field, field_validator, model_validator
from enum import Enum
from typing import Optional
from datetime import datetime, date
from dateutil.relativedelta import relativedelta
import json
from html import unescape
from difflib import get_close_matches

#Load Language Map
with open("lang_map.json", "r", encoding="utf-8") as f:
    LANG_MAP = json.load(f)

"""Validates all form entries
If no entry is passed in for a certain field, returns None
Returns as Pydantic mode instance, convert to json/dict in main (model_dump_json)"""
    
class TestAppt(BaseModel):
    #check if the appointment is one of the ones we have
    Appointment_ID: Optional[str] = Field(default=None, alias="Appointment_ID")
    Client: Optional[str] = Field(default=None, alias="Client")

    Language: Optional[str]=Field(default=None, alias="Language")
    
    Date: Optional[str]=Field(default=None, alias="Date")

    Start_Time: Optional[str]=Field(alias="Start_Time")
    End_Time: Optional[str]=Field(alias="End_Time")

    def model_post_init(self, __context):
        print(f"Validated input data for appointment: {self.Appointment_ID} for {self.Client}")

    @staticmethod
    def _validate_mmddyyyy(value: str, field_name: str) -> str:
        """Validate date as MM/DD/YYYY"""
        try:
            parsed = datetime.strptime(value, "%m/%d/%Y")
            return parsed.strftime("%m/%d/%Y")
        except ValueError:
            raise ValueError(field_name + " must be in MM/DD/YYYY format")
    
    @field_validator("Date", mode="before")
    @classmethod
    def format_appt_date(cls, value: str) -> str:
        try:
            parsed = datetime.strptime(value, "%m/%d/%Y").date()
        except ValueError:
            raise ValueError("Date must be in MM/DD/YYYY format")
            
        #Calculate date from two years from now
        curr = date.today()
        upper = curr + relativedelta(years=2) 
                
        if parsed < curr:
            raise ValueError("Date must be today or in the future")
        elif parsed > upper:
            raise ValueError(f"Date must not be beyond {upper.strftime('%m/%d/%Y')}")
                
        return parsed.strftime("%m/%d/%Y")

    
    @field_validator("Start_Time", "End_Time", mode="before")
    @classmethod
    def format_time(cls, value: str) -> str:
        try:
            #Try validating as standard format (HH:MM AM/PM) into date time
            parsed = datetime.strptime(value.strip(), "%I:%M %p")
        except ValueError:
            #Try military time
            try:
                parsed = datetime.strptime(value.strip(), "%H:%M")
            except ValueError:
                raise ValueError("Time must be in 24-hour format (HH:MM) or 12-hour format (HH:MM AM/PM)")
        #return Standard time
        return parsed.strftime("%I:%M %p")


    @field_validator("Language", mode="before")
    @classmethod
    def validate_lang(cls, value: str) -> str:
        """Match intake language with output from options"""
        cleaned = value.strip().lower()
        if cleaned in LANG_MAP:
            return LANG_MAP[cleaned]
        
        #Fuzzy match if not in map
        #Account for common misspellings (Ex: Napali -> Nepali)
        matches = get_close_matches(cleaned, LANG_MAP.keys(), n=1, cutoff=0.6)
        if matches:
            return LANG_MAP[matches[0]]

        raise ValueError(value + " language not recognized")