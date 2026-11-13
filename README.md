# ALU Regex Data Extraction Tool

A robust Python-based utility developed to aggregate and extract structured data from unstructured web responses and strings using the raw power of **Regular Expressions**.

## 🚀 Project Overview
As part of a junior full-stack developer portfolio project, this application parses through messy strings and precisely isolates distinct types of sensitive or structured data. 

The application features **dual execution modes**: an automated pre-configured demonstration mode (for out-of-the-box evaluation) and an interactive search mode allowing users to input custom text dynamically.


## 📋 Supported Data Types & Regex Patterns

The application extracts and explicitly labels the following 8 data types:

1. **Email Addresses:** Captures standard and corporate formats (e.g., `user@example.com`, `firstname.lastname@company.co.uk`).
2. **URLs:** Captures secure protocols, standard protocols, and domains starting with `www.` (e.g., `https://www.example.com`, `www.subdomain.org/page`).
3. **Phone Numbers:** Handles multiple standard separators like parentheses, dashes, and periods (e.g., `(123) 456-7890`, `123-456-7890`, `123.456.7890`).
4. **Credit Card Numbers:** Identifies standard 16-digit financial card structures separated by spaces or hyphens (e.g., `1234-5678-9012-3456`).
5. **Time Stamps:** Supports both 24-hour format and 12-hour format with case-insensitive `AM`/`PM` indicators (e.g., `14:30`, `2:30 PM`, `11:45am`).
6. **HTML Tags:** Extracts standard markup elements and attributes (e.g., `<p>`, `<div class="example">`, `<img src="image.jpg">`).
7. **Hashtags:** Identifies social media tags and keywords (e.g., `#TechPulse2026`, `#WebDevelopment`).
8. **Currency Amounts:** Captures monetary values featuring thousands separators and decimal cent values (e.g., `$19.99`, `$1,234.56`).


## 🛠️ Project Structure

```text
alu_regex-data-extraction-binelintsa-sketch/
│
├── select.py       # Main Python script containing regex logic and CLI runner
└── README.md          # Project documentation and setup guide
