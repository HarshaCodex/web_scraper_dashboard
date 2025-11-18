# Web Scraper Dashboard

A user-friendly application that automatically collects job listings from multiple sources and displays them in an easy-to-use dashboard.

## 📋 Overview

This project helps job seekers and recruiters gather job opportunities from various websites in one place. Instead of visiting multiple job boards individually, the Web Scraper Dashboard automatically collects and organizes job links for you.

## ✨ Features

- **Multi-source Job Collection**: Scrapes job listings from multiple job boards and websites
- **Centralized Dashboard**: View all job listings in one convenient location
- **Easy Filtering**: Search and filter jobs by title, location, and other criteria
- **Regular Updates**: Automatically refreshes job listings periodically
- **User-Friendly Interface**: Simple and intuitive design for all skill levels

## 🚀 Getting Started

### Prerequisites

Before you begin, make sure you have:
- Python 3.8 or higher installed
- pip (Python package manager)
- A text editor or IDE (VS Code, PyCharm, etc.)

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd web_scraper_dashboard
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   python app.py
   ```

4. **Access the dashboard**
   - Open your web browser and go to `http://localhost:5000`

## 📖 How to Use

1. **View Jobs**: The dashboard displays all scraped job listings automatically
2. **Search**: Use the search bar to find specific job types or companies
3. **Filter**: Narrow down results by location, salary range, or job category
4. **Apply**: Click on any job link to view full details and apply

## 🛠️ Technical Stack

- **Backend**: Python, Flask (web framework)
- **Scraping**: BeautifulSoup, Requests
- **Frontend**: HTML, CSS, JavaScript
- **Database**: SQLite (for storing job data)
- **Task Scheduling**: APScheduler (for automatic updates)

## 📁 Project Structure

```
web_scraper_dashboard/
├── app.py              # Main application file
├── scraper.py          # Web scraping logic
├── requirements.txt    # Python dependencies
├── templates/          # HTML templates
├── static/             # CSS and JavaScript files
├── database.db         # SQLite database
└── README.md           # This file
```

## 🔧 Configuration

- **Update Frequency**: Jobs are refreshed every 6 hours (configurable)
- **Job Sources**: Add or remove job sources in `scraper.py`
- **Database Location**: Configure database path in `app.py`

## ⚙️ Common Tasks

### Add a New Job Source

Edit `scraper.py` and add a new scraper function following the existing pattern.

### Change Update Schedule

To modify how frequently jobs are refreshed, look for the scheduler configuration in `app.py` and adjust the time interval accordingly.

## 📝 Troubleshooting

**Issue**: Dashboard not loading
- **Solution**: Ensure Python is running and the server hasn't crashed. Check terminal for error messages.

**Issue**: No jobs appearing
- **Solution**: Wait a few moments for scraping to complete. Check internet connection and ensure websites are accessible.

**Issue**: Slow performance
- **Solution**: Try clearing the database or reducing the number of job sources.

## 📚 Learning Resources

- [Python Web Scraping Guide](https://realpython.com/beautiful-soup-web-scraper-python/)
- [Flask Documentation](https://flask.palletsprojects.com/)
- [BeautifulSoup Tutorial](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)

## 📄 License

This project is licensed under the MIT License - see LICENSE file for details.

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest new features
- Submit pull requests

## 📧 Contact

For questions or suggestions, please reach out or open an issue in the repository.

---

**Last Updated**: 2025
