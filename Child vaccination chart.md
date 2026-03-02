```python
# Main dictionary to store all patient records
patient = {}  # Key: record number, Value: nested dictionary with patient details

# Counter to assign unique record numbers
record_number = 1

# Function to insert a patient record
def insert():
    global record_number  # Needed so we can update record_number outside the function
    
    print("\n--- Adding a New Patient ---")
    
    # Ask for patient's first and last name
    first_name = input("Enter patient's first name: ")
    last_name = input("Enter patient's last name: ")
    
    # Validate birth month input
    while True:
        try:
            birth_month = int(input("Enter birth month when vaccine was administered (1-12): "))
            if 1 <= birth_month <= 12:
                break
            else:
                print("Month must be between 1 and 12. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 12.")
    
    # Create a nested dictionary for the patient
    patient_record = {
        "First Name": first_name,
        "Last Name": last_name,
        "Birth Month": birth_month
    }
    
    # Add the nested dictionary to the main patient dictionary using a unique record number
    patient[record_number] = patient_record
    
    print(f"Patient record {record_number} added successfully!")
    
    # Increment record number for the next patient
    record_number += 1

# Insert multiple patients
insert()  # Add first patient
insert()  # Add second patient

# Verify that both records are in the dictionary
print("\n--- All Patient Records ---")
for rec_num, info in patient.items():
    print(f"Record {rec_num}: {info}")


    # https://www.youtube.com/watch?v=8Ybbwp6JQYU
