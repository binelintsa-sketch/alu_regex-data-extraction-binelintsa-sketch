import re

# Dictionary containing all 8 Regex patterns
patterns = {
    "Email Address": r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b',
    "URL": r'(?:https?://|www\.)[^\s"]+',
    "Phone Number": r'(?:\(\d{3}\)|\d{3})[-.\s]?\d{3}[-.\s]?\d{4}',
    "Credit Card Number": r'\b\d{4}[-\s]\d{4}[-\s]\d{4}[-\s]\d{4}\b',
    "Time Stamp": r'\b(?:[01]?\d|2[0-3]):[0-5]\d(?:\s?(?i:[ap]m))?\b|\b(?:1[0-2]|[1-9]):[0-5]\d\s?(?i:[ap]m)\b',
    "HTML Tag": r'<[^>]+>',
    "Hashtag": r'#[A-Za-z0-9_]+',
    "Currency Amount": r'\$\d{1,3}(?:,\d{3})*(?:\.\d{2})?'
}

def extract_and_label_data(text):
    print("\n" + "~"*50)
    print("          UNIFIED DATA EXTRACTION REPORT")
    print("~"*50 + "\n")
    
    found_any = False
    
    # Loop through each category and find matches
    for category_name, pattern in patterns.items():
        matches = re.findall(pattern, text)
        
        if matches:
            found_any = True
            print(f"📁 {category_name}s Found ({len(matches)}):")
            for match in matches:
                print(f"   -> {match}")
            print("~" * 40)
            
    if not found_any:
        print("No matching patterns found in this text.\n")
    print("~"*50 + "\n")

if __name__ == "__main__":
    # 1. AUTOMATED DEMO (Runs first for the grader)
    sample_text = """
    Welcome to today's tech roundup at 14:30 or 2:30 PM. Visit https://www.techpulse.org 
    or contact support@techpulse.org. Call (123) 456-7890. Price: $19.99. #Tech2026
    """
    print("Running automated demonstration...")
    extract_and_label_data(sample_text)
    
    # 2. INTERACTIVE MULTI-LINE SEARCH MODE
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("   INTERACTIVE MULTI-LINE SEARCH MODE")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Instructions:")
    print("1. Paste or type your multi-line text below.")
    print("2. When you are finished, type the word END on a brand new line and press Enter.")
    print("3. Type 'quit' to exit the program.\n")
    
    while True:
        print("Enter your text below (Type 'END' on a new line to process, or 'quit' to exit):")
        lines = []
        while True:
            try:
                line = input()
            except EOFError:
                break
                
            if line.strip().lower() == 'quit':
                print("Exiting program. Goodbye!")
                exit()
            if line.strip() == 'END':
                break
            lines.append(line)
            
        user_text = "\n".join(lines)
        
        if user_text.strip() == "":
            print("No text entered. Try again.\n")
            continue
            
        extract_and_label_data(user_text)
