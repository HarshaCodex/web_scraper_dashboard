# 🚀 Job Scraper Dashboard 🚀

## ✨ Your Personal Job Listings Aggregator ✨

Tired of juggling multiple job boards? This user-friendly dashboard automatically scrapes remote job listings and displays them in one clean, simple interface. Say goodbye to browser tab chaos and hello to streamlined job hunting!

---

## 🌟 Features

-   **🤖 Automated Job Collection**: Scrapes job listings from `weworkremotely.com`.
-   **📋 Centralized Dashboard**: View all collected job listings in a single, convenient location.
-   **🔄 One-Click Refresh**: Instantly update the job listings with the latest opportunities.
-   **💻 Simple & Clean UI**: A straightforward and intuitive design built with Bootstrap.
-   **💾 Lightweight & Portable**: Stores job data in a simple `data.json` file, no database required!

---

## 🚀 Getting Started

### Prerequisites

-   Python 3.8+
-   `pip` (Python package manager)

### Installation & Setup

1.  **Clone the repository:**
    ```bash
    git clone <repository-url>
    cd web_scraper_dashboard
    ```

2.  **Install the required packages:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Run the application:**
    ```bash
    python app.py
    ```

4.  **View your dashboard!**
    -   Open your browser and navigate to `http://localhost:5000`.

---

## 🛠️ Tech Stack

-   **Backend**: Python, Flask
-   **Web Scraping**: BeautifulSoup, Requests
-   **Frontend**: HTML, Bootstrap
-   **Data Storage**: JSON

---

## 📁 Project Structure

```
web_scraper_dashboard/
├── app.py              # Main Flask application
├── web_scraper_dashboard/
│   ├── auto_scraper.py # Main scraping orchestrator
│   ├── extract_jobs.py # Logic for extracting job data
│   └── ...
├── templates/
│   └── index.html      # HTML template for the dashboard
├── data.json           # Stores the scraped job data
├── requirements.txt    # Python dependencies
└── README.md           # You are here!
```

---

## 🤝 Contributing

Contributions are welcome! If you have ideas for new features, find a bug, or want to improve the code, feel free to:

-   Open an issue to discuss your ideas.
-   Submit a pull request with your changes.

