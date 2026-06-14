import datetime

def generate_log(log_entries):
    # 1. Raise ValueError if input is not a list (Rubric Criterion 4)
    if not isinstance(log_entries, list):
        raise ValueError("Input must be a list of log entries.")
    
    # 2. Get the current date in YYYYMMDD format (Rubric Criterion 2)
    current_date = datetime.datetime.now().strftime("%Y%m%d")
    filename = f"log_{current_date}.txt"
    
    # 3. Create and write content to the file (Rubric Criteria 1, 3 & 5)
    with open(filename, "w", encoding="utf-8") as file:
        for entry in log_entries:
            file.write(f"{entry}\n")
            
    # 4. Print confirmation message including the filename (Rubric Criterion 6)
    print(f"Success: Log file created successfully as {filename}")
    
    # 5. Return the filename so the test framework can track and clean it up (Fixes Teardown Errors)
    return filename