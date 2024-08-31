#!/usr/bin/env python3

APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
]

class Person:
    APPROVED_JOBS = [
        "Admin", "Customer Service", "Human Resources", "ITC", "Production",
        "Legal", "Finance", "Sales", "General Management",
        "Research & Development", "Marketing", "Purchasing"
    ]

    def __init__(self, name="Unknown", job="Unemployed"):
        self.name = name
        self.job = job

    # Name property
    def get_name(self):
        return self._name

    def set_name(self, value):
        if isinstance(value, str) and 1 <= len(value) <= 25:
            self._name = value.title()  # Convert to title case before saving
        else:
            print("Name must be string between 1 and 25 characters.")
            self._name = "Unknown"  # Default to a safe value

    name = property(get_name, set_name)

    # Job property
    def get_job(self):
        return self._job

    def set_job(self, value):
        if value in Person.APPROVED_JOBS:
            self._job = value
        else:
            print("Job must be in list of approved jobs.")
            self._job = "Unemployed"  # Default to a safe value

    job = property(get_job, set_job)

