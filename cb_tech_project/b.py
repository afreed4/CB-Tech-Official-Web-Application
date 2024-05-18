import re

def extract_numeric_part(input_str):
    match = re.search(r'(\d{4})', input_str)
    if match:
        return match.group(1)
    else:
        return None
    
last_registration_id1 = "CB00012023"
last_registration_id2 = "CBT00012023"

print(extract_numeric_part(last_registration_id1))
print(extract_numeric_part(last_registration_id2))    
