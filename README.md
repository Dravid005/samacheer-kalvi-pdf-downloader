# 🐙 Samacheer Smart Downloader 2.0

A smart Python tool to download **Samacheer Kalvi (Tamil Nadu State Board)** textbooks directly from Google Drive. It features a "Smart Menu" system that automatically handles Subject, Medium, and Term logic for classes 6 to 12.

## 🚀 Features
* **Smart Menus:** Select subjects by number (e.g., Press `1` for Tamil). No typing errors!
* **Intelligent Logic:** Automatically skips "Medium" selection for language subjects (English/Tamil).
* **Google Drive Integration:** Downloads files directly from a secure Google Drive storage using a central catalog.
* **Live Catalog:** The app fetches the latest `book_catalog.json` from GitHub, so you don't need to update the code to get new books.

## 📂 Project Structure
* `src/book_downloader.py` - The main Python script that runs the magic.
* `src/book_catalog.json` - The "Brain" of the system. It maps file names to Google Drive IDs.
* `requirements.txt` - List of Python packages needed.

---

## 🛠️ Installation

1.  **Clone the Repository**
    ```bash
    git clone [https://github.com/Dravid005/samacheer-kalvi-pdf-downloader.git](https://github.com/Dravid005/samacheer-kalvi-pdf-downloader.git)
    cd samacheer-kalvi-pdf-downloader
    ```

2.  **Install Dependencies**
    You only need one package to run this tool:
    ```bash
    pip install -r requirements.txt
    ```

---

## 🏃‍♂️ How to Run

1.  Open your terminal in the project root folder.
2.  Navigate to the source folder:
    ```bash
    cd src
    ```
3.  Run the script:
    ```bash
    python book_downloader.py
    ```
4.  **Follow the prompts:**
    * Enter Class (6-12).
    * Select Term (only if Class 6 or 7).
    * Choose Subject from the numbered list.
    * Choose Medium (English/Tamil) - *Automatically skipped for Language subjects.*

The PDF will download instantly to your `src` folder.

---

## ➕ How to Add New Books (For Contributors)

We use a **Central Catalog** (`src/book_catalog.json`) to manage downloads. If you want to add a missing book:

1.  **Upload the PDF** to Google Drive.
2.  **Set Permissions:** Right-click file -> Share -> "Anyone with the link".
3.  **Get the ID:** Copy the link and extract the ID part (the text between `/d/` and `/view`).
4.  **Update `book_catalog.json`:**
    Add a new line with the correct filename format and the ID:
    ```json
    "class-10-term0-science-tamil-medium.pdf": "YOUR_GOOGLE_DRIVE_ID_HERE"
    ```
5.  **Filename Rules:**
    * **Classes 6-7:** `class-{std}-term{1/2/3}-{subject}-{medium}-medium.pdf`
    * **Classes 8-12:** `class-{std}-term0-{subject}-{medium}-medium.pdf`
    * *(Note: Language subjects do not have the `{medium}-medium` part)*

---

**Developed by:** [Dravid005](https://github.com/Dravid005)
