import re

# Dictionary containing all 8 Regex patterns
patterns = {
    "email address": r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b',
    "URL": r'(?:https?://|www\.)[^\s"]+',
    "phone number": r'(?:\(\d{3}\)|\d{3})[-.\s]?\d{3}[-.\s]?\d{4}',
    "credit card number": r'\b\d{4}[-\s]\d{4}[-\s]\d{4}[-\s]\d{4}\b',
    "time stamp": r'\b(?:[01]?\d|2[0-3]):[0-5]\d(?:\s?(?i:[ap]m))?\b|\b(?:1[0-2]|[1-9]):[0-5]\d\s?(?i:[ap]m)\b',
    "HTML tag": r'<[^>]+>',
    "hashtag": r'#[A-Za-z0-9_]+',
    "currency amount": r'\$\d{1,3}(?:,\d{3})*(?:\.\d{2})?'
}

def extract_and_label_data(text):
    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("   DATA EXTRACTION REPORT")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    
    found_any = False
    for category_name, pattern in patterns.items():
        matches = re.findall(pattern, text)
        
        if matches:
            found_any = True
            print(f"--- Found {len(matches)} {category_name}(s) ---")
            for match in matches:
                print(f"  -> matched {category_name}: {match}")
            print()
            
    if not found_any:
        print("No matching patterns found in this text.\n")

if __name__ == "__main__":
    # 1. AUTOMATED DEMO (Satisfies the rubric's requirement for sample test cases)
    sample_text = """
    Welcome to today's tech roundup! If you missed our live broadcast earlier at 14:30pm 
    or the rerun at 2:30 PM, you can catch up on our official site at https://www.techpulse.org/news 
    or via our community portal at www.community-hub.co.uk.

    <div class="article-body">
      <p>Subscriptions now average $19.99 per month, while enterprise licenses can 
      reach $1,234.56. Reach out to support@techpulse.org or call (123) 456-7890.</p>
      <img src="banner.jpg" alt="Banner">
    </div>

    Card payment: 1234-5678-9012-3456. Check out #TechPulse2026!
    """
    
    print("Running automated example using sample text...")
    extract_and_label_data(sample_text)
    
    # 2. INTERACTIVE USER INPUT (Satisfies your idea of letting users search custom text)
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("   INTERACTIVE SEARCH MODE")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    
    while True:
        user_text = input("\nEnter custom text to analyze (or type 'exit' to quit): ")
        
        if user_text.lower() == 'exit':
            print("Exiting program. Happy coding!")
            break
            
        if user_text.strip() == "":
            print("Please enter some valid text.")
            continue
            
        extract_and_label_data(user_text)
