Least Price Detector

Overview

Least Price Detector is a web-based application that enables users to find the best available price for a given product across multiple e-commerce platforms. The project combines web scraping, data handling, and a user-friendly interface to deliver a reliable price comparison tool.

Features

Real-Time Price Comparison: Retrieves product prices from popular e-commerce sites (Amazon, Flipkart, Snapdeal, Meesho).
User-Friendly Interface: Accepts product name input and displays the best available price and details.
Dynamic Scraping: Utilizes rotating headers and proxies for reliable data extraction.
REST API Integration: Flask-based backend to handle API requests between the frontend and the scraper.
Technologies Used

Backend: Python, Flask, Flask-CORS, BeautifulSoup for web scraping.
Frontend: HTML, CSS, JavaScript for a clean and responsive UI.
Database/Storage: None required; data is fetched in real-time.
Miscellaneous: Requests for HTTP handling, rotating user agents for efficient scraping.
Project Structure

Least-Price-Detector/
├── app.py                   # Main Flask application
├── scraper.py               # Scraping functions for each e-commerce platform
├── static/
│   ├── styles.css           # CSS for styling the frontend
├── templates/
│   ├── index.html           # Main HTML file for the frontend
├── script.js                # JavaScript for handling user inputs and API calls
└── README.md                # Project description and setup (this file)
Installation and Setup

Clone the Repository
git clone https://github.com/yourusername/Least-Price-Detector.git
cd Least-Price-Detector
Set Up a Virtual Environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install Dependencies
pip install -r requirements.txt
Run the Application Start the Flask server.
python app.py
The app should be running on http://127.0.0.1:5000.
Usage

Open the application in your browser (http://127.0.0.1:5000).
Enter the name of the product you wish to search.
Click on "Find Prices" to fetch and display the best available price from supported platforms.
Future Scope

Adding more platforms for a broader price comparison.
Improved error handling for robust functionality under server restrictions.
Building a mobile application for convenience on the go.
Integrating machine learning to predict price trends.
License

This project is open-source and available under the MIT License.

This README provides a comprehensive guide for understanding, setting up, and using the Least Price Detector project.
