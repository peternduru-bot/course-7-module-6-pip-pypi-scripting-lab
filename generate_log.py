import datetime

def generate_log(log_entries):
    # 1. Raise ValueError if input is not a list
    if not isinstance(log_entries, list):
        raise ValueError("Input must be a list of log entries.")
    
    # 2. Get the current date in YYYYMMDD format
    current_date = datetime.datetime.now().strftime("%Y%m%d")
    filename = f"log_{current_date}.txt"
    
    # 3. Create and write content to the file
    with open(filename, "w", encoding="utf-8") as file:
        for entry in log_entries:
            file.write(f"{entry}\n")
            
    # 4. Print confirmation message including the filename
    print(f"Success: Log file created successfully as {filename}")