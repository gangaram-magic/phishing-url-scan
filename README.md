# 🔐 ThreatGuard – Intelligent Phishing Detection Web App

*ThreatGuard* is a Flask-based web application developed as a final year project that aims to detect phishing websites and analyze file contents in a simplified yet efficient way. The application provides users with two key functionalities: URL threat detection and text extraction from uploaded documents. It is designed to help users identify whether a given URL is safe (benign) or harmful (phishing) by comparing it against a predefined dataset. Additionally, the application supports PDF and TXT file uploads, processes the content securely, and allows users to view and download extracted data.

The core feature of this system is phishing URL detection using a dataset named phishing_model.csv, which contains known phishing and benign URLs. The app reads this dataset and matches the user-provided input URL to classify it as phishing, benign, or unknown. On the file side, the system supports PDF decryption using pypdf, including password-protected files, and text extraction using Python. Extracted content is saved and available for download, offering a complete end-to-end experience.

The user interface is intuitive, mobile-friendly, and styled with dark-mode UI components. It includes loading animations and categorized result displays. Security has been considered by ensuring input validation and support for encrypted files. Though intended for academic demonstration, the project mimics real-world phishing detection techniques in a simplified form.

This project was built using:
- *Flask* for backend routing and HTML rendering
- *pypdf* for advanced PDF reading
- *Pandas* for data handling with the phishing dataset
- *HTML/CSS + Font Awesome* for frontend presentation

This tool is ideal for educational demonstrations, awareness initiatives, or further research in phishing detection. While the current model is dataset-based, it can be expanded into machine learning-based predictions in future iterations.
