# backend.py
import hashlib
import pandas as pd
import random

# Sample medicine pool
medicine_pool = [
    {"Medicine": "Paracetamol", "Dosage": "500mg", "Timing": "Morning & Night"},
    {"Medicine": "Amoxicillin", "Dosage": "250mg", "Timing": "After Food (Twice Daily)"},
    {"Medicine": "Vitamin D3", "Dosage": "1000 IU", "Timing": "Morning"},
    {"Medicine": "Cetirizine", "Dosage": "10mg", "Timing": "Night"},
    {"Medicine": "Metformin", "Dosage": "500mg", "Timing": "Morning & Evening"},
    {"Medicine": "Ibuprofen", "Dosage": "400mg", "Timing": "After Food (Thrice Daily)"},
    {"Medicine": "Azithromycin", "Dosage": "500mg", "Timing": "Morning (Before Food)"},
    {"Medicine": "Calcium", "Dosage": "600mg", "Timing": "Night"},
    {"Medicine": "Pantoprazole", "Dosage": "40mg", "Timing": "Morning (Empty Stomach)"},
    {"Medicine": "Levocetirizine", "Dosage": "5mg", "Timing": "Evening"}
]

# Hash function for file
def get_file_hash(file):
    file_content = file.read()
    return hashlib.md5(file_content).hexdigest()

# Generate random schedule
def generate_schedule(n=5):
    return pd.DataFrame(random.sample(medicine_pool, n))
