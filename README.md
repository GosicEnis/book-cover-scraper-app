# 📚 Book Cover Web Scraper & Viewer

This project is a complete Python-based solution for scraping missing book cover images from OpenLibrary and displaying them in a user-friendly web interface using Flask.

---

## 🧠 Project Overview

The application automates the process of retrieving missing book covers for a list of books provided in a CSV file (`books.csv`). It consists of two key components:

1. **Web Scraping (`web_scrape.py`)**  
   - Scrapes OpenLibrary for each book that doesn't have a cover image.
   - Downloads and saves the image in the `static/covers/` directory.
   - Updates the CSV file with the filename of the downloaded image.

2. **Flask Web App (`app.py` + `books.html`)**  
   - Loads the `books.csv` data.
   - Displays a styled grid of book covers with title, author, published year, and genre on the `/books` route.

---

## 🗂️ Project Structure

- `books.csv` — Dataset with book info: title, author, genre, etc.
- `web_scrape.py` — Web scraper to fetch missing cover images
- `app.py` — Flask app to display books
- `static/`
  - `covers/` — Folder for downloaded cover images
   - `book-cover-placeholder.jpg` # Default image for missing covers
- `templates/`
  - `books.html` — HTML template for book display
---

## ⚙️ How It Works

### 🔍 `web_scrape.py`
- For every book in `books.csv` with an empty `cover` field:
  - It constructs a search query using the title
  - Uses `requests` and `BeautifulSoup` to scrape OpenLibrary
  - Downloads the first found cover image
  - Saves it locally in `static/covers/` and updates `books.csv`

### 🌐 `app.py` + `books.html`
- The Flask app reads the updated `books.csv`
- Sends book data to the HTML template
- The template (`books.html`) displays book covers and related info in a clean, styled layout
- If a cover is missing, it displays a placeholder image

---

## 🚀 How to Run the Project

### Step 1 – Install Dependencies

Make sure you have Python installed, then install the required libraries:

```bash
pip install flask pandas beautifulsoup4 requests
```

### Step 2 – Scrape Missing Covers

Run the scraper script to download missing book covers:

```bash
python web_scrape.py
```

⏱ Note: This may take a few minutes depending on how many covers are missing.

### Step 3 – Start the Flask App
To launch the web interface, run the following command:

```bash
flask --app app.py run
```

You will see a local URL in the terminal, something like:

```bash
Running on http://127.0.0.1:5000
```

Now open your browser and add /books to that URL:

```bash
http://127.0.0.1:5000/books
```

You’ll now see your library with all available book covers!

## 📸 Example Output

The web page displays:

- Book cover image (or placeholder)  
- Title  
- Author  
- Year of publication  
- Genre  

---

## 📌 Author

**Enis Gosić**
