import json
import requests
import os

# ======================================================
# 1. CONFIGURATION
# ======================================================
CATALOG_URL = "https://raw.githubusercontent.com/Dravid005/samacheer-kalvi-pdf-downloader/main/src/book_catalog.json"

# ======================================================
# 2. HELPER FUNCTIONS (Download & Catalog)
# ======================================================
def get_book_catalog():
    print("⏳ Connecting to the Library Catalog...")
    try:
        response = requests.get(CATALOG_URL)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"❌ Error: Server returned {response.status_code}")
            return {}
    except Exception as e:
        print(f"❌ Connection Error: {e}")
        return {}

def download_from_google_drive(file_id, output_filename):
    url = f"https://drive.google.com/uc?export=download&id={file_id}"
    print(f"\n⬇️  Downloading: {output_filename}")
    
    try:
        response = requests.get(url, stream=True)
        if response.status_code == 200:
            total_size = 0
            with open(output_filename, 'wb') as file:
                for chunk in response.iter_content(chunk_size=1024):
                    if chunk:
                        file.write(chunk)
                        total_size += len(chunk)
            
            if total_size < 2000:
                print("⚠️ Warning: File is too small. Check your Google Drive ID.")
            else:
                print(f"✅ Success! Saved as: {output_filename}")
        else:
            print(f"❌ Error: Google Drive returned status {response.status_code}")
    except Exception as e:
        print(f"❌ Download failed: {e}")

# ======================================================
# 3. SMART NAMING LOGIC
# ======================================================
def generate_filename(std, term_val, subject, medium):
    # Clean inputs
    std = str(std).lower().strip()
    subject = subject.lower().strip()
    medium = medium.lower().strip()

    # Handle Term Logic (8-12 is always term0)
    if std not in ["6", "7"]:
        term_val = "0"
    
    languages = ["english", "tamil"]
    
    if subject in languages:
        # e.g., class-6-term1-english.pdf
        return f"class-{std}-term{term_val}-{subject}.pdf"
    else:
        # e.g., class-6-term1-science-english-medium.pdf
        return f"class-{std}-term{term_val}-{subject}-{medium}-medium.pdf"

# ======================================================
# 4. MAIN INTERFACE (THE UPGRADED MENU)
# ======================================================
def main():
    print("==========================================")
    print("   🐙 SAMACHEER SMART DOWNLOADER 2.0 🐙   ")
    print("==========================================")

    # 1. Load Catalog
    book_catalog = get_book_catalog()
    if not book_catalog:
        return

    # 2. Select Class
    std = input("\n👉 Enter Class (6-12): ").strip()
    
    # 3. Select Term (Only for 6 & 7)
    term_input = "0"
    if std in ["6", "7"]:
        print("\nSelect Term:")
        print("   1. Term 1")
        print("   2. Term 2")
        print("   3. Term 3")
        term_input = input("👉 Enter choice (1-3): ").strip()

    # 4. Select Subject (Menu Based)
    # Define lists based on class group
    if std in ["11", "12"]:
        subjects = ["Tamil", "English", "Maths", "Physics", "Chemistry", "Biology", "Computer Science", "Commerce", "Accountancy"]
    else:
        subjects = ["Tamil", "English", "Maths", "Science", "Social Science"]

    print(f"\nSelect Subject for Class {std}:")
    for i, sub in enumerate(subjects, 1):
        print(f"   {i}. {sub}")
    
    sub_choice = input(f"👉 Enter number (1-{len(subjects)}): ").strip()
    
    # Convert number to Subject Name
    try:
        subject_index = int(sub_choice) - 1
        selected_subject = subjects[subject_index] # Get the name, e.g., "Maths"
    except (ValueError, IndexError):
        print("❌ Invalid number. Defaulting to English.")
        selected_subject = "English"

    # 5. Smart Medium Selection
    # If it is Tamil or English, we FORCE the medium to be empty/default and skip the question.
    if selected_subject.lower() in ["tamil", "english"]:
        print(f"ℹ️  Subject is {selected_subject}. Skipping medium selection.")
        medium = "english" # Placeholder, won't be used in filename for languages
    else:
        print("\nSelect Medium:")
        print("   1. English Medium")
        print("   2. Tamil Medium")
        med_choice = input("👉 Enter choice (1-2): ").strip()
        medium = "tamil" if med_choice == "2" else "english"
# 6. Generate & Download
    target_filename = generate_filename(std, term_input, selected_subject, medium)
    print(f"\n🔎 Looking for: {target_filename}")

    if target_filename in book_catalog:
        drive_id = book_catalog[target_filename]
        
        # --- ADD THIS DEBUG LINE ---
        print(f"🆔 Found ID: {drive_id}") 
        # ---------------------------

        download_from_google_drive(drive_id, target_filename)
    else:
        print("❌ Book not found in catalog.")

if __name__ == "__main__":
    main()